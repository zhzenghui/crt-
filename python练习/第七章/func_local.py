#Filename : func_local.py

def func(x):
    print 'x is',x
    x = 2
    print 'changed local x to',x
    
x = 30
func(x)
print 'x is still',x