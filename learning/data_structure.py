# List
mylist = [1,2,3]
print("Zeroth Value: %d" % mylist[0])
mylist.append(4)
print("List Length: %d" % len(mylist))
for value in mylist:
    print(value)

# Dictionary
# Dictionaries are mappings of names to values, like key-value pairs. Note the use of the curly bracket and colon notations when define the dictionary.
mydict = {'a':1,'b':2,'c':3}
print("A value %d" % mydict['a'])
mydict['a'] = 11
print("A value %d" % mydict['a'])