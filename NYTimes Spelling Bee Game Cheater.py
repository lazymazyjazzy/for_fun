#NYTimes Spelling Bee Game Cheater

'''
The game basically gives you 6 letters and 1 center letter.

Center letter must be in every word, and word length must be longer than
4.

You can use every letter as many times you wish, and every game has 1 word
that includes every letter at least once in the given letters.

You can enter the website below, and play the game;
https://www.nytimes.com/puzzles/spelling-bee

The fake version without subscription for trial;
https://nytimes-spellingbee.com
'''

'''
Make sure to download and install NLTK(Natural Language Toolkit) it helps
users to work with human language data.
'''
from nltk.corpus import words

#All letters in the game are gathered with the user input. Since they change every day.
letters = []
let_num = 1
for i in range(7):
    i = input("Please provide the letter number " + str(let_num) + ": ")
    let_num += 1
    if i[0].isalpha():
        letters.append(i[0])

#Center letter is selected seperately since it should be in every word.
center_letter = input("Please provide the center letter from the list you entered: ")

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

#Unique words will be gathered in a set by the for loop below.
uniq_words = set()

#For loop for gathering words > 4 letters and includes the center letter.
for word in converted_list:
    if set(word).issubset(letters):
        if center_letter in word and len(word) >= 4:
            uniq_words.add(word)

print("\n")
print("The total number of generated meaningful words: ")        
print(len(uniq_words))
print("\n")

#Showing all words one by one in order to play the game easily.
counter = 1
for i in uniq_words:
    print(str(counter) + ":" + str(i))
    counter += 1

'''Note that some words created by NLTK cannot be found in the game list due to
language limitations, street slang, proper names and nouns etc.

Still try everything and most of them will be accepted by Spelling Bee.
'''