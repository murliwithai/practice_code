text=("  I am Ram... ") 

print(text)

print("capitalized :",text.upper()) #upper() method converts all the characters in the string to uppercase.

print("lowercase :",text.lower())#lower() method converts all the characters in the string to lowercase.

print("split string :",text.split())#split() method splits the string into a list of substrings based on a specified delimiter (default is whitespace).

print("replaced :",text.replace("Ram", "Shyam"))#replace() method replaces all occurrences of a specified substring with another substring in the string.

print("stripped whitespace :",text.strip())#strip() method removes leading and trailing whitespace from the string.

print("length of splitted text string :",len(text.strip()))#len() function returns the number of characters in the string, including spaces.

print("length of original text string is :", len(text)) # This will give the length of the original string text, which includes the leading and trailing whitespace. The length will be greater than the length of the stripped string because of the extra spaces.

print("index of ram:",text.find("Ram"))#find() method returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1.

words=text.strip().split() 

print("this will find the words in the string :",words) 

print("this will find the length of the list of words :",len(words))#  finds the length of the list of words, which is the number of words in the string.

city="delhi"
age=21

print(f"i am {age} years old and i live in {city}") #f-string is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and their values are inserted into the string.  
             