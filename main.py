str1 = input()
str2 = input()
str3 = input()

dict_replace = {}
j = 0
list_ch = []


def add_char(str1_i, str2_ch):
    if dict_replace.get(str1_i):
        list_char = dict_replace.get(str1_i)
        list_char.append(str2_ch)
    else:
        list_char = [str2_ch]
    dict_replace[str1_i] = list_char
    if dict_replace.get(str2_ch):
        list_char = dict_replace.get(str2_ch)
        list_char.append(str1_i)
    else:
        list_char = [str1_i]
    dict_replace[str2_ch] = list_char


for i in str1:
    ch = str2[j]
    add_char(i, ch)
    while ch in str1:
        k = str1.index(ch)
        ch1 = str2[k]
        add_char(i, ch1)
        ch = ch1
    j = j + 1

for i in dict_replace:
    list_ch = dict_replace.get(i)
    list_ch.sort();
    dict_replace[i] = list_ch

final_string = ""

for i in str3:
    list_ch = dict_replace.get(i)
    ch2 = list_ch[0]
    final_string = final_string + ch2

print(final_string)
input()
