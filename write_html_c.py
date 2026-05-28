import os, re

src = r'C:\Users\asus\AppData\Local\Temp\opencode\write_html.py'
with open(src, 'r', encoding='utf-8') as f:
    script = f.read()

match = re.search(r"^content = r'''(.*)'''", script, re.DOTALL | re.MULTILINE)
if not match:
    print("ERROR: could not extract content")
    exit(1)

content = match.group(1)

target = r'C:\Users\asus\AppData\Local\Temp\opencode\my-magical-day.html'
with open(target, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Written: {target}, size: {os.path.getsize(target)} bytes')
