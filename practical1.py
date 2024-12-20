#                            practical : 1.1



# a> implement following operation using python tuple concept.
#__________________________________________________________________________

# - create tuples with different data types(integer, float, string and mixed).
#  string tuples
stringtuple = ("a for apple " , "b for ball " , "c for charusat" ," d for D2D")
print(stringtuple)

# interger tuples
integertuple = (1,2,3,4,5,6,7)
print(integertuple)

# float tuple
floattuple = (2.3,2.5,1.3,5.3)
print(floattuple)

#mix tuple
mixtuple = ("hey" , 23 , 2.4 )
print(mixtuple)

# __________________________________________________________________________

# - access tuple elements using positive indices.
# positive index access
ptuple = ("a for apple " , "b for ball " , "c for charusat" ," d for D2D")
print(ptuple[2])

# nagative index access 
ntuple = ( "a for apple " , "b for ball " , "c for charusat" ," d for D2D")
print(ntuple[-1])

#__________________________________________________________________________
 
# - perform tuple slicing to extract specific portions of the tuple.

sliceingtuple = (1,2,3,4,5,6,7,8,9,10)
print(sliceingtuple[2:5]) # prinit the valuse from index 3 to 5
print(sliceingtuple[:7]) # print valuse from index 0 to 7
print(sliceingtuple[::2]) # ever 2 element from the tuple
print(sliceingtuple[-3:-1]) # it will select elemt from last


#__________________________________________________________________________
# count occurrence of  an element and find the index of an element in a tuple.










