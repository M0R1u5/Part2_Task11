string = input('Enter any word: ')

if string.count(' ') == 0:
    print(len(string))
else:
    print(str(len(string) - string.count(' ')))