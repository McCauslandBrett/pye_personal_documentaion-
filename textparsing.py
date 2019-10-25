# split on space
l = 'hello world'.split()
print(l)

# split on character
l = 'hello-world'.split('-')
print(l)

# strip 
l = 'hello world'
l = l.strip('')
print(l)

# note: Doesnt work on '-' or ' ' must do this
l = 'hello-world'
l = l.strip('-')
print(l)

string = 'android is awesome'

print(string.strip('an'))
print(string)

