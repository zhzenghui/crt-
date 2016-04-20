#Filename : break.py

while True:
    s = raw_input('Enter sonmeThing : ')
    if s == 'quit':
        break
    print 'Length of the string is',len(s)
print 'Done'