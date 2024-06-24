import sys, re
from util import *

print('<html><head><title>...</title><body>')
title = False
with open('test_input.txt') as file:
    for block in blocks(file):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            print('<h1>')
            print(block)
            print('</h1>')
            title = False
        else:
            print('<p>')
            print(block)
            print('</p>')
print('</body></html>')
