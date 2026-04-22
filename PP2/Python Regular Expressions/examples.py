import re

# RegEx functions    
# findall - returns a list containing all matches 
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# txt = "The rain in Spain"
# x = re.search("\s",txt)
# print(x.start()) #start output the index of the first such match
# a = re.split("\s", txt,)
# b = re.findall("a",txt)
# c = re.sub("\s","*",txt)
# d = re.match("\s",txt) #checking if string begins with such match


#Metacharacters
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group
   
# txt = "The rain in Spain"
# # x = re.search("^The.*Spain$",txt)
# # a = re.search("^The.+Spain$",txt)
# # b = re.search("^The.?rain$",txt)
# # print(a, x,b, sep="\n")
# # x = re.findall("rain|Portugal",txt)
# print(x)

#Flags
# re.ASCII	re.A	Returns only ASCII matches	
# re.DEBUG		Returns debug information	
# re.DOTALL	re.S	Makes the . character match all characters (including newline character)	
# re.IGNORECASE	re.I	Case-insensitive matching	
# re.MULTILINE	re.M	Returns only matches at the beginning of each line	
# re.NOFLAG		Specifies that no flag is set for this pattern	
# re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
# re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable
txt = "The rain in Spain"