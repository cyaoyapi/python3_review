"""
	This program is executed with a list of words(in command line).
	It ultimately displays words larger than 10 characters.
"""

from sys import argv, exit 

print(f"The name of the ongoing program is : {argv[0]}")
print("=====================================================================")
print("List of given words :")
if len(argv) < 2:
	print("Error : there are not given words as arguments!")
	exit("===Try again!===")
else:
	big_words = []
	for i in range(1, len(argv)): # It's better to use 'enumerate' here.It's Just an exercise. 
		print(f"{i} => {argv[i]}")
		big_words.insert(i, argv[i]) # We can use directly 'append' here.
print("List of words more larger than 10 characters :")
# We don't realy need the variable big_words and certain part of the following code. 
# It'is just for exercising and testing.
for word in big_words[:]:
	if len(word) < 10:
		big_words.remove(word)
	else:
		print(word)
print("Just to verify the content of the big_words list :")
print(big_words)
exit("===End, Good Bye!===")
