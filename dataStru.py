# Tuple (cannot change)
a = ('1', 2, 3)
print(a)

# List
mylist = [1,2,3]
print("zeroth value: %d" % mylist[0])
mylist.append(4)
print("list lenght: %d" % len(mylist))
for value in mylist:
    print(value)

# Dictionaries
mydict = {'a':1,'b':2,'c':3}
print("A value: %d" % mydict['a'])
mydict['a'] = 11
print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys())
print("Values: %s" % mydict.values())
for key in mydict.keys():
	print(mydict[key])
