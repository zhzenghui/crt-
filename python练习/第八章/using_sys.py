#Filename : using_sys.py

import sys
import using_name

print 'The command line arguments are:'
for i in sys.argv:
    print i
print '\n\n The PYTHONPATH is',sys.path, '\n'
