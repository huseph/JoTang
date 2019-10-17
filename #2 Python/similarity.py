'''
* count words
* by Huseph
'''
import re
punctuation = '!,;:?"\''

def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip().lower().split()


with open('test1.txt', 'r') as f:
    f1 = removePunctuation(f.read())
with open('test2.txt', 'r') as f:
    f2 = removePunctuation(f.read())

dict1 = {}
dict2 = {}

for words in f1:
    if words not in dict1:
        dict1[words] = 1
    else:
        dict1[words] += 1

for words in f2:
    if words not in dict2:
        dict2[words] = 1
    else:
        dict2[words] += 1

list1= sorted(dict1.items(),key=lambda x:x[1],reverse=True)
list2= sorted(dict2.items(),key=lambda x:x[1],reverse=True)

print('the ten most frequent words in test1 is: ', [list1[i][0] for i in range(10)])
print('the ten most frequent words in test2 is: ', [list2[i][0] for i in range(10)])



