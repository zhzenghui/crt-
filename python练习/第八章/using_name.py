#Filename : using_name.py
#import mymodule
#mymodule.sayhi()
#print 'version',mymodule.version

from mymodule import *
sayhi()
print 'version',version

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'