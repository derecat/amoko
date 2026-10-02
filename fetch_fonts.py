import re, os, subprocess

os.chdir('/var/minis/workspace/amoko')
css = open('fonts.css').read()
urls = re.findall(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', css)
print(f'{len(urls)} urls to fetch')

for u in urls:
    name = os.path.basename(u.split('?')[0])
    dest = os.path.join('fonts', name)
    if not os.path.exists(dest):
        subprocess.run(['curl', '-s', '-o', dest, u], check=True)
        print('fetched', name)
    else:
        print('exists', name)

# rewrite urls to local relative paths
new = re.sub(r'url\(https://fonts\.gstatic\.com/[^)]+\)',
             lambda m: 'url(./fonts/' + os.path.basename(m.group(0).split('?')[0]) + ')',
             css)
open('fonts-local.css', 'w').write(new)
print('fonts-local.css written')
