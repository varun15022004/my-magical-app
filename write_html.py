import os
import re

# Get the directory of the script
dir_path = os.path.dirname(os.path.abspath(__file__))

# File paths
index_path = os.path.join(dir_path, 'index.html')
styles_path = os.path.join(dir_path, 'styles.css')
script_path = os.path.join(dir_path, 'script.js')
output_path = os.path.join(dir_path, 'my-magical-day.html')

print("Compiling modular files into a single standalone app...")

# Read modular files
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(styles_path, 'r', encoding='utf-8') as f:
    css = f.read()

with open(script_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace stylesheet link with inline styles
html = re.sub(
    r'<link\s+[^>]*href=["\']styles\.css["\'][^>]*>',
    f'<style>\n{css}\n</style>',
    html
)

# Replace script src link with inline script content
html = re.sub(
    r'<script\s+[^>]*src=["\']script\.js["\'][^>]*>\s*</script>',
    f'<script>\n{js}\n</script>',
    html
)

# Write the compiled version
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Standalone file successfully written to:', output_path)
print('File size:', os.path.getsize(output_path), 'bytes')
