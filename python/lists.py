#Create a list
L = "Joe is the ultimate zombie killer"

# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# List slicing
L[3:5]

# Use extend to add elements to list
L = [ "Unfiltered", 007]
L.extend(['pop', 10])
L

# Use append to add elements to list
L = [ "Unfiltered", 007]
L.append(['pop', 10])
L

# Use extend to add elements to list
L = [ "Unfiltered", 007]
L.append(['pop', 10])
L

# Use append to add elements to list
L.append(['a','b'])
L

#As lists are mutable, we can change them. For example, we can change the first element as follows:
# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

#We can convert a string to a list using split.
# Split the string, default is by space
'hard rock'.split()
# Split the string by comma
'A,B,C,D'.split(',')

#When we set one variable B equal to A, both A and B are referencing the same list in memory:
# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

#Initially, the value of the first element in B is set as "hard rock". If we change the first 
# element in A to "banana", we get an unexpected side effect. As A and B are referencing the 
# same list, if we change list A, then list B also changes. If we check the first element of 
# B we get "banana" instead of "hard rock":

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A
B = A[:]
B

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

