##We can also input a stride value as follows, with the '2' indicating that we are selecting every second variable:
name= "tinyefuza"
#stride
# Get every second element. The elments on index 1, 3, 5 ...
name[::2]
# Get every second element in the range from index 0 to index 4
name[0:5:2]

# Print the string for 3 times
print(3* name)

#indexing
# Print the first element in the string
print(name[0])
#negative indexing
# Print the last element in the string
print(name[-1])

#slicing
# Take the slice on variable name with only index 0 to index 3
name[0:4]

# Concatenate strings
name = "Joe"
name = name + " is the ultimate zombie kiler"
name

#escape sequencies
# New line escape sequence
print("Joe\n is the ultimate zombie killer" )
print("Joe is the ultimate\\ zombie killer" )
# Tab escape sequence
print("Joe is the\t ultimate zombie killer" )
# r will tell python that string will be display as raw string
print(r" The BodyGuard \t is the best album" )   #python will therefore not consider it as a new tab

#strip() function removes trailing and leading whitespace
name.strip()


# Convert all the characters in string to upper case
a = "Joe is the ultimate zombie killer"
print("before upper:", a)
b = a.upper()
print("After upper:", b)
c= a.lower()
print("all lower:" c)
d= a.title()
print("capitalise each word:" d)

"""The method replace replaces a segment of the string, i.e. a substring with a new string. 
We input the part of the string we would like to change. The second argument is what we would
 like to exchange the segment with, and the result is a new string with the segment changed:"""
b = a.replace('JoJoe', 'Banger')
b

"""The method find finds a sub-string. The argument is the substring you would like to find, 
and the output is the first index of the sequence. We can find the sub-string he or Guard."""
# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "JoJoe is in town, Najjanankumbi, street 007, plot 2003"
name.find('street')

#The method Split splits the string at the specified separator, and returns a list.
#Split the substring into list
split_string = (name.split())
split_string

#ReGex
import re
s1 = "JoJoe is in town, Najjanankumbi, street 007, plot 2003"
# Define the pattern to search for
pattern = r"Najjanankumbi"
# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)
# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")


#The match.group() method is used in Python's re module to retrieve the 
# part of the string where the regular expression pattern matched.
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)
if match:
#match.group() retrieves the substring 1234567890 from the text, which is the part that matched the pattern.
    print("Phone number found:", match.group())      
else:
    print("No match")

#\w 
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches:", matches)

#\re.findall
s2 = "JoJoe is the ultimate zombie killer"
# Use the findall() function to find all occurrences of the "st" in the string
result = re.findall("st", s2)
# Print out the list of matched words
print(result)

# Use the split function to split the string by the "\s"
#r"\s": This is a regular expression pattern that matches any whitespace character (spaces, tabs, newlines, etc.).
#s2: This is the string that you want to split.
split_array = re.split(r"\s", s2)
# The split_array contains all the substrings, split by whitespace characters
print(split_array)

#The <code>sub</code> function of a regular expression in Python is used to replace all occurrences of a pattern in a string
# with a specified replacement.
# Define the regular expression pattern to search for
pattern = r"ultimate zombie killer"
# Define the replacement string
replacement = "legend in the room"
# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 