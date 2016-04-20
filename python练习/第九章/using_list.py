#Filename : using_list.py

#This is my shopping list
shoplist = ['apple','mango','carrot','banana']

print 'I have',len(shoplist),'item to purchase.'
print 'These items are:',#Notice the comma at end of the line 
for item in shoplist:
    print item
    
print '\nI also have to buy rice'
shoplist.append('rice')
print 'My shopping list is now',shoplist
print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is',shoplist
print 'The first item I will buy is',shoplist
olditem = shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shopping list is now',shoplist

shoplist[0] = 'xiao'
print 'My shopping list is now',shoplist

shoplist.insert(0,'yang')
print 'My shopping list is now',shoplist

shoplist1 = ['yuan','new','say']
shoplist.extend(shoplist1)
print 'My shopping list is now',shoplist