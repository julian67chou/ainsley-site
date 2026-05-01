import os, re

base = '/workspace/ainsley-clone'
existing = set(os.listdir(f'{base}/assets/images/news/'))
print(f'Existing images ({len(existing)}): {existing}')

for f in sorted(os.listdir(base)):
    if not f.startswith('news_detail_') or not f.endswith('.html'):
        continue
    
    with open(f'{base}/{f}', 'r', encoding='utf-8') as fh:
        text = fh.read()
    
    # Find img referencing news folder
    m = re.search(r'src="assets/images/news/([^"]+)"', text)
    if m:
        img_file = m.group(1)
        if img_file not in existing:
            old = re.search(r'<div class="news_img">.*?</div>', text, re.DOTALL)
            if old:
                text = text.replace(old.group(0), '')
                with open(f'{base}/{f}', 'w', encoding='utf-8') as fh:
                    fh.write(text)
                print(f'REMOVED: {f} - {img_file}')
            else:
                print(f'NONEWS_IMG: {f} - {img_file}')
        else:
            print(f'OK: {f} - {img_file}')
    else:
        print(f'NO_IMG: {f}')
