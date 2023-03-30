
string = input()
len1 = len(string) - len(string.replace('f', ''))
if len1 == 1:
    print(string.index('f'))
elif len1 > 1:
    print(string.index('f'), string.rindex('f'))
