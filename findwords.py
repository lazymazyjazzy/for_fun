#Creating Meaningful Words by 7 Letters Game

'''
Make sure to download and install NLTK(Natural Language Toolkit) it helps
users to work with human language data.
'''
import random
from nltk.corpus import words

letters = ["t","u","x","e","a","l","n"]

converted_list = words.words() #gathering all words in English by ntlk.
print("All words are gathered.")
'''
The dictionary provided by nltk includes capitalized letters, 
with a for loop all letters are lowered. 

With a list comprehension we created a dictionary only includes the
words which length lower than 8. For faster searching and optimization. 
'''
for i in range(len(converted_list)):
    converted_list[i] = converted_list[i].lower()

converted_list2 = [num for num in converted_list if len(num) < 8]
print("Dictionary created with words that have lengths lower than 8.")
'''
Function for converting randomly created lists into strings.
'''
def listToString(s): 
    str1 = "" 
    return (str1.join(s))

'''
Random word creators for each case from 2 to 7.
'''
def two_gen(let_list):
    return listToString(random.choices(let_list,None,k=2))
    
def three_gen(let_list):
    return listToString(random.choices(let_list,None,k=3))

def four_gen(let_list):
    return listToString(random.choices(let_list,None,k=4))

def five_gen(let_list):
    return listToString(random.choices(let_list,None,k=5))

def six_gen(let_list):
    return listToString(random.choices(let_list,None,k=6))

def seven_gen(let_list):
    return listToString(random.choices(let_list,None,k=7))

'''
Random Words Set Generators;
They create all possible words.
'''
two_letters = set()

while True:
    two_letters.add(two_gen(letters))
    if len(two_letters) == 7**2:
        break
print("Words with 2 letters are created.")  

three_letters = set()

while True:
    three_letters.add(three_gen(letters))
    if len(three_letters) == 7**3:
        break
print("Words with 3 letters are created.")    

four_letters = set()

while True:
    four_letters.add(four_gen(letters))
    if len(four_letters) == 7**4:
        break
print("Words with 4 letters are created.")    

five_letters = set()

while True:
    five_letters.add(five_gen(letters))
    if len(five_letters) == 7**5:
        break
print("Words with 5 letters are created.")    

six_letters = set()

while True:
    six_letters.add(six_gen(letters))
    if len(six_letters) == 7**6:
        break
print("Words with 6 letters are created.")    

seven_letters = set()

while True:
    seven_letters.add(seven_gen(letters))
    if len(seven_letters) == 7**7:
        break
print("Words with 7 letters are created.")    

'''
Using .union method for sets, all words from 2 to 7 gathered as one set.
'''
generated_words = two_letters.union(three_letters, four_letters, five_letters, six_letters, seven_letters)
print("All generated words are listed and iteration begins...")

'''
Lastly, generated words are checked within the all words by for loop 
which take about 15 min.
'''
meaningful_words = set()

for i in generated_words:
    if i in converted_list2:
        meaningful_words.add(i)
        print(len(meaningful_words))

print("The total number of generated meaningful words: ")        
print(len(meaningful_words))
print("Generated meaningful words are: ")
print(meaningful_words)
