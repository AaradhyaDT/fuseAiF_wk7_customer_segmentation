import nbformat
from pathlib import Path
import re
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
fixed = False
for i, cell in enumerate(nb.cells):
    if cell.cell_type != 'code':
        continue
    # find print statements where opening quote is followed by a newline before closing quote
    if re.search(r"print\('\n", cell.source) or re.search(r"print\('(?:\\n)?[^']*\n", cell.source):
        print('Inspecting cell', i)
        print('--- source snippet ---')
        print(cell.source)
        print('--- end snippet ---')
        # Replace broken multi-line print patterns with escaped newline
        cell.source = re.sub(r"print\('\n(.*?)'\)", lambda m: f"print('\\n{m.group(1)}')", cell.source, flags=re.S)
        # Also replace lines split across newline without closing quote
        cell.source = cell.source.replace("print('\nData types:'\n", "print('\\nData types:')\n")
        cell.source = cell.source.replace("print('\nFirst 5 rows:'\n", "print('\\nFirst 5 rows:')\n")
        cell.source = cell.source.replace("print('\nMissing values:'\n", "print('\\nMissing values:')\n")
        cell.source = cell.source.replace("print('\nDescriptive statistics:'\n", "print('\\nDescriptive statistics:')\n")
        fixed = True
if fixed:
    nbformat.write(nb, path)
    print('Notebook patched.')
else:
    print('No broken print patterns found.')
