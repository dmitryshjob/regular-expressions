import re
from pprint import pprint
import csv

# доб = '(доб\S\s\d+)' 
# email = (\w+\@\w+\.\w+) 
# Ф\И  = (^[А-ё]\w+)\D([А-ё]\w+)\D
# тел = (\+7|8)\s?\(?(\d{3})\)?[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d{2})

# (^[А-ё]\w+)\D([А-ё]\w+)[\,\s]*([А-ё]*)[\,]*([А-ё]*)\,*([cа-ё\s]*)
# \s\W\s 

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

PHONE_PATTERN = r'(\+7|8)\s?\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})[\s\(]*([доб\.\s]*\d*)[\,\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6'

new_list = list()
for item in contacts_list:
    lists = ' '.join(item).split(' ')
    result = [lists[0], lists[1], lists[2], item[3], item[4],re.sub(PHONE_PATTERN, PHONE_SUB, item[5]),item[6]]
    new_list.append(result)    

for list_data in new_list:
    for data_replacement in new_list:
        if list_data[0] == data_replacement[0] and  list_data[1] == data_replacement[1]:
            if list_data[2] == '':
                list_data[2] = data_replacement[2]
            if list_data[3] == '':
                list_data[3] = data_replacement[3]
            if list_data[4] == '':
                list_data[4] = data_replacement[4]
            if list_data[5] == '':
                list_data[5] = data_replacement[5]
            if list_data[6] == '':
                list_data[6] = data_replacement[6]


new_data = list()
for list_data in new_list:
  if list_data not in new_data:
    new_data.append(list_data)    
 
with open("phonebook.csv", "w",encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter='|')
  datawriter.writerows(new_data)
