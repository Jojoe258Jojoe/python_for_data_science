#to open a file, we use open
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
#with automatically closes the file
#r represents the mode with which we wish to open the file, in this case it's read

# Verify if the file is closed
file1.closed


# Read first four characters, we specify it by passing the value 4 in read
with open(example1, "r") as file1:
    print(file1.read(4))


#We can also read one line of the file at a time using the method readline():
# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

#We can also pass an argument to  readline()  to specify the number of charecters 
#we want to read. However, unlike  read(),  readline() can only read one line at most.
with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

#We can use a loop to iterate through each line:
# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

#We can use the method readlines() to save the text file to a list
# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()



#writing files using the write method
#we have to specify w iin the parentheses asa shown below
"""We can open a file object using the method write() to save the text file
 to a list. To write to a file, the mode argument must be set to w. 
 Let’s write a file Example2.txt with the line: “This is line A”"""
# Write line to file
exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file, we can read to confirm that it worked
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

# Write the strings in the list to text file
with open('/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

#However, note that setting the mode to w overwrites all the existing data in the file.
with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

#Appending Files
"""We can write to files without losing any of the existing data as follows by setting the mode 
argument to append: a. you can append a new line as follows:"""
# Write a new line to text file
with open('/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

#a+ : Appending and Reading. Creates a new file, if none exists. 
with open('/Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

"""Opening the file in w is akin to opening the .txt file, moving your cursor to 
the beginning of the text file, writing new text and deleting everything that 
follows. Whereas opening the file in a is similiar to opening the .txt file, 
moving your cursor to the very end and then adding the new pieces of text.
It is often very useful to know where the 'cursor' is in a file and be able to control 
it. The following methods allow us to do precisely this -

.tell() - returns the current position in bytes
.seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. 
From can take the value of 0,1,2 corresponding to beginning, relative to current position and end"""
with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

# Copy file to another
with open('/Example2.txt','r') as readfile:
    with open('/Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

