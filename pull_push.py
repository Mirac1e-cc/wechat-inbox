# -*- coding: utf-8 -*-
"""公众号草稿自动推送（在服务器上由计划任务定时运行）
流程：拉取 GitHub 仓库 wechat-inbox 最新内容 -> 未推过的包逐个推入草稿箱 -> 记录状态
密钥：secret.txt（先找脚本同目录，再找 wechat-push-bundle 子目录）。已推记录：state.json
仓库布局：packages/<包名>/article.json + 正文 html + images/
article.json: {"articles":[{"title","author","digest","html","thumb","content_source_url"}]}
"""
import os, sys, json, time, zipfile, shutil, subprocess, urllib.request, base64

HERE = os.path.dirname(os.path.abspath(__file__))
APPID = 'wxff2966afc8e8d46c'
BASE = 'https://api.weixin.qq.com'
ZIP_URL = 'https://github.com/Mirac1e-cc/wechat-inbox/archive/refs/heads/main.zip'
STATE = os.path.join(HERE, 'state.json')
WORK = os.path.join(HERE, '.cache')

def now():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def log(msg):
    print('[%s] %s' % (now(), msg))
    sys.stdout.flush()

def http_get_json(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))

def post_json(url, payload):
    req = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode('utf-8'))

def upload(url, path):
    out = subprocess.run(['curl', '-s', '--max-time', '60', '-F', 'media=@' + path, url],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return json.loads(out.stdout)

def find_secret():
    for cand in [os.path.join(HERE, 'secret.txt'),
                 os.path.join(HERE, 'wechat-push-bundle', 'secret.txt')]:
        if os.path.exists(cand):
            return open(cand, encoding='utf-8').read().strip()
    raise RuntimeError('找不到 secret.txt')

def load_state():
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE, encoding='utf-8'))
        except Exception:
            return {}
    return {}

def save_state(st):
    json.dump(st, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def fetch_repo():
    if os.path.isdir(WORK):
        shutil.rmtree(WORK)
    os.makedirs(WORK)
    zpath = os.path.join(WORK, 'repo.zip')
    subprocess.run(['curl', '-sL', '--max-time', '120', '-o', zpath, ZIP_URL],
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not os.path.exists(zpath) or os.path.getsize(zpath) < 200:
        raise RuntimeError('仓库压缩包下载失败（GitHub 没连上或仓库不存在）')
    zf = zipfile.ZipFile(zpath)
    zf.extractall(WORK)
    roots = [d for d in os.listdir(WORK) if os.path.isdir(os.path.join(WORK, d))]
    if not roots:
        raise RuntimeError('压缩包里没有目录')
    return os.path.join(WORK, roots[0])

def decode_b64_files(pkg_dir):
    # 仓库里图片以 .b64 文本存放（推送通道只收文本），就地解码出原文件
    for root, dirs, files in os.walk(pkg_dir):
        for name in files:
            if name.endswith('.b64'):
                src = os.path.join(root, name)
                dst = src[:-4]
                if not os.path.exists(dst):
                    data = open(src, 'rb').read()
                    open(dst, 'wb').write(base64.b64decode(data))

def push_package(pkg_dir, secret):
    decode_b64_files(pkg_dir)
    spec = json.load(open(os.path.join(pkg_dir, 'article.json'), encoding='utf-8'))
    tok = http_get_json(BASE + '/cgi-bin/token?grant_type=client_credential&appid=' + APPID + '&secret=' + secret)
    if 'access_token' not in tok:
        raise RuntimeError('取通行证失败 ' + json.dumps(tok, ensure_ascii=False))
    at = tok['access_token']
    img_dir = os.path.join(pkg_dir, 'images')
    thumbs = set()
    for a in spec['articles']:
        thumbs.add(a.get('thumb', ''))
    url_map = {}
    if os.path.isdir(img_dir):
        for name in sorted(os.listdir(img_dir)):
            if name.endswith('.b64'):
                continue
            rel = 'images/' + name
            if rel in thumbs:
                continue
            r = upload(BASE + '/cgi-bin/media/uploadimg?access_token=' + at, os.path.join(img_dir, name))
            if 'url' not in r:
                raise RuntimeError('正文图上传失败 ' + name + ' ' + json.dumps(r, ensure_ascii=False))
            url_map[rel] = r['url']
    articles = []
    for a in spec['articles']:
        r = upload(BASE + '/cgi-bin/material/add_material?access_token=' + at + '&type=thumb',
                   os.path.join(pkg_dir, a['thumb']))
        if 'media_id' not in r:
            raise RuntimeError('封面上传失败 ' + json.dumps(r, ensure_ascii=False))
        html = open(os.path.join(pkg_dir, a['html']), encoding='utf-8').read()
        for rel, u in url_map.items():
            html = html.replace(rel, u)
        articles.append({
            'title': a['title'],
            'author': a.get('author', '刀哥'),
            'digest': a.get('digest', ''),
            'content': html,
            'content_source_url': a.get('content_source_url', ''),
            'thumb_media_id': r['media_id'],
            'need_open_comment': 0,
            'only_fans_can_comment': 0,
        })
    r = post_json(BASE + '/cgi-bin/draft/add?access_token=' + at, {'articles': articles})
    if 'media_id' not in r:
        raise RuntimeError('建草稿失败 ' + json.dumps(r, ensure_ascii=False))
    return r['media_id']

def main():
    try:
        secret = find_secret()
    except Exception as e:
        log('启动失败：%s' % e)
        return
    try:
        root = fetch_repo()
    except Exception as e:
        log('拉取仓库失败：%s' % e)
        return
    pkg_root = os.path.join(root, 'packages')
    if not os.path.isdir(pkg_root):
        log('仓库里还没有 packages 目录，无事可做')
        return
    state = load_state()
    todo = [d for d in sorted(os.listdir(pkg_root))
            if os.path.isdir(os.path.join(pkg_root, d)) and d not in state]
    if not todo:
        log('没有待推的新包')
        return
    for pkg_id in todo:
        try:
            mid = push_package(os.path.join(pkg_root, pkg_id), secret)
            state[pkg_id] = {'media_id': mid, 'pushed_at': now()}
            save_state(state)
            log('已推入草稿箱：%s media_id=%s' % (pkg_id, mid))
        except Exception as e:
            log('推送失败 %s：%s' % (pkg_id, e))

if __name__ == '__main__':
    main()
