import os



def merging_files(list_files):
    num_lines={}
    for files in list_files:
        with open(files, encoding='utf-8') as f:
            num_lines[files]=len(f.readlines())
    sorted_lines={key: value for key, value in sorted(num_lines.items(), key=lambda x: x[1],reverse = True)}
    print(sorted_lines)
    with open('fulltext.txt','w', encoding = 'utf-8') as fulltext_file:
        for key , value in sorted_lines.items():
            fulltext_file.write(key +'\n')
            fulltext_file.write(str(value)+'\n')
            with open(key ,'r', encoding='utf-8') as f:
                fulltext_file.write(f.read())
                fulltext_file.write('\n')

list_files=['text1.txt', 'text2.txt', 'text3.txt']

print(merging_files(list_files))




 


