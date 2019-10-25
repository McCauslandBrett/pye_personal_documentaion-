# -*- coding: utf-8 -*-
"""
Spyder Editor

Documentation By Brett
"""

#list 
def lst_driver():
    lst = []
   
    
#dictionaries    
def dct_driver():
    dct = {}
  
    
#tuples  
def tup_driver():
    tup = {'a',1}
    #insertion
 
    



"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
comments: 
    -Index range [0-(N-1)]
    -sort() no return value.Changes org lst  
     If you want the org lst, use sorted()
    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
#list
    
# list insertion
lst = []
lst.append('a')
lst.insert(1,'b')
lst.insert(4, 'f') # since there is no 4 item it just insersts in back

# list combining
breeds = ['FrenchBulldog', 'pootle', 'GermanShepard']
breeds1 = ['begal', 'lab']
breeds.extend(breeds1)

a =['a', 'a', 'a']
b= ['b', 'b']
a += b


# list deletion
lst.remove('a') #Return:None
pop_value = lst.pop(2)
pop_value = lst.pop() #Return/remove the last element in the list
lst.clear()



# list accessors
pets = ['dog', 'cat', 'rabbit']
access = pets[0]
access = pets.index('dog')

#list copy

#   Shallow copy 
og_lst = ['a', 'b', 'c', 'd']
new_lst = og_lst
new_lst.remove('a')


#   Deep copy
og_lst = ['a', 'b', 'c', 'd']
new_lst = og_lst.copy()
new_lst.remove('a')

slicelst = ['cat', 'parrot']
#deep copy using slicing
slicenew_lst = slicelst[:]
slicenew_lst.append('a')

# list iteration
og_lst = ['a', 'b', 'c', 'd']
count = len(og_lst)
print(count)
for i in range(0,count):
    print(i)
    print(og_lst[i])

"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
comments: 
    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
#dictionary

# dictionary creation
dct = {}
# loop threw all keys and values
for x, y in dct.items():
  print(x, y)



# dictionry insertion
dct['f'] = 'f'

# dictionary deletion

# dictionary mutators

# dictioary copy

# dictionary sorted

"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
comments: 
    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

"""
#tuples

# tuples creation
tup = {'a',1}
# tuples insertion
# tuples deletion
# tuples mutators
# tuples copy
# tuples sorted

"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
comments: 
    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
#matrix






