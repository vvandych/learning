
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days"
replacement = "Eyjafjallajokull"
marker='EY'
marker_end=len(marker)
start=line.find(marker)
part_a=line[:start]
part_b=line[start+marker_end:]
replaced=part_a+replacement+part_b
print replaced




word = "madam"
# test case 2
# word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###
alphabet='abcdefghijklmnopqrstuvwxyz'
a=(alphabet.find(word[0])-alphabet.find(word[-1]))
b=-1
c=1
if  b<a<c:
    is_palindrome=0
else:
    is_palindrome=(-1)
print is_palindrome