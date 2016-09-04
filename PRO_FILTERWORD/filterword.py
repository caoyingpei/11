with open('filtered_words.txt') as fp:
    filter_set=fp.readlines()
filter_set = [ a.strip() for a in filter_set ]

print(filter_set)
while 1:
    print('plz input your word:')
    a=input()
    for i in filter_set:
        a = a.replace(i, len(i)*'*')
    print(a)
