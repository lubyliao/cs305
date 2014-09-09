""" A program that answers the question:

    Which language is the 17th most popular at 
    http://pt.sourceforge.jp/softwaremap/trove_list.php?form_cat=160 ?

A language is more popular (than another) if there are more projects
hosted using the language.
"""

#1. Fetch the data, and store it 

import re
import os 
os.system('lynx -nolist -dump http://pt.sourceforge.jp/softwaremap/trove_list.php?form_cat=160 > lang_list')

f = open('lang_list')
lines = f.readlines()

#2. Process data.  Get rid of lines until we reach the first language ALGOL 68 
while lines:
    del lines[0]
    if 'ALGOL' not in lines[0]:
        continue
    break

#3. Collect all languages in lang_list
lang_list = []
while True:
    lang_list.append(lines[0])
    del lines[0]
    if 'Zope' in lines[0]:
        lang_list.append(lines[0])
        break

#4. Trim off white spaces
lang_list = [lang.strip() for lang in lang_list]

#5. Extract (num, lang) from each line using reg exp matching
lang_num_list = []
for lang_num in lang_list:
    m = re.search(r'(\w+.*) +\((\d+)', lang_num)
    num = m.group(2)
    lang =m.group(1)
    lang_num_list.append((int(num), lang))

#6. Sort and reverse
lang_num_list.sort()
lang_num_list.reverse()
print(lang_num_list)
