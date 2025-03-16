"""
Write a program that takes a sentence and creates a dictionary where each word is a key, and the value is the number of times that word appears. Use a sample sentence and break it into words to fill the dictionary. 
Example: For the sentence "the cat and the hat", the dictionary should be {"the": 2, "cat": 1, "and": 1, "hat": 1}.
"""


input_list = list(input("Enter the sentence: ").split())
dict_1 = {}

for i in set(input_list):
	dict_1[i] = input_list.count(i)
print(dict_1)

"""
Create a dictionary to store student names as keys and their scores as values.
Use a few sample names and scores to populate the dictionary.
Print out each student’s name and score on a new line.
"""

input_names = list(input("Enter the names: ").split())
input_scores = list(input("Enter the score: ").split())
dict_1 = {}

for i in range(len(input_names)):
	dict_1[input_names[i]] = input_scores[i]

print(dict_1)


"""
Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}).
Use this dictionary to convert a list of numbers into words and print each word on a new line.
"""

dict_1 = {1:'one',2:'two', 3:'three', 4:'four', 5:'five'}

list_1 = [1,2,3,4,5]

for i in list_1:
	print(dict_1[i])

"""
Create a dictionary to represent a store’s inventory with items as keys and quantities as values.
Print the quantity of a specific item (e.g., "Apples").
Update the quantity of an item and print the dictionary to show the change.
"""

inventory = {"Apple":5,"Banana":4,"Peach":3}

for key,value in inventory.items():
	print(f"{key} - {value}")
	value -= 1
	print(f"{key} - {value}")


#Write a program that takes a sentence and uses a set to find all unique words. Print each unique word on a new line.

input_sentence = list(input("Enter the sentence: ").split())

for i in set(input_sentence):
	print(i)


#Given two lists of numbers, use sets to find and print the common elements between them.

ls1 = [1, 2, 3, 4, 5]
ls2 = [4, 5, 6, 7, 8]

print(set(ls1) & set(ls2))

"""
Given a list of numbers, use a set to find any duplicates in the list and print them.
You can add numbers to a set one by one and check if they are already present.
Example: For the list [1, 2, 2, 3, 4, 4, 5], the output should be {2, 4}.
"""

ls1 = [1, 2, 2, 3, 4, 4, 5]

s1 = set(ls1)
s2 = set()

for i in s1:
	if ls1.count(i) > 1:
		s2.add(i)

print(s2)

"""
Use a set to create a list of vocabulary words from a paragraph.
Break the paragraph into individual words, add each word to the set, and print the final set of unique words.
Example: For the paragraph "Python is fun. Python is powerful.", 
the output should be {"Python", "is", "fun", "powerful"}.
"""

input_paragraph = list(input("Enter the paragraph: ").split())

for i in input_paragraph:
	i.replace(".","")

print(set(input_paragraph))


#Հայտարարել երկու set: Տպել դրանց միավորումը, հատումը, սիմետրիկ տարբերությունը:

first_set = {1,2,3,4}
second_set = {3,4,5}
print(first_set.union(second_set))
print(first_set.intersection(second_set))
print(first_set.symmetric_difference(second_set))

#Հայտարարել երկու զանգված: Երկու զանգվածներն էլ նույնն են՝ բացառությամբ որ մի զանգվածը պարունակում է մեկ էլեմենտ ավելի շատ: Գտնել այդ էլեմենտը:

ls1 = [1,2,2,3,4,5,6,7,8]
ls2 = [1,2,2,3,20,4,5,6,7,8]

x = set(ls1) & (set(ls2))
print(list((x | set(ls2)) - x))


#Գրել ծրագիր որը կստանա երկու set և կվերադարձնի True, եթե մեկը մյուսի ենթաբազմություն է, False հակառակ դեպքում:

input_set_1 = set(input())
input_set_2 = set(input())

if input_set_1.issubset(input_set_2):
    print(True)
else:
    print(False)


#Հայտարարել set` բաղկացած ամբողջ թվերից: Set-ում եղած բոլոր կենտ թվերը ջնջել, և ավելացնել տվյալ քանակությամբ զույգ թվեր:

int_set = {1,2,3,4,5,6,7,8}
int_set_c = int_set.copy()
n  = []
if max(int_set_c) % 2 == 0: 
    max_num = max(int_set_c)
else:
    max_num = max(int_set_c)+1
for i in int_set:
    if i % 2 != 0:
        int_set_c.remove(i)
        
        n.append(max(int_set_c)+2*i)
ls = set(n)
print(int_set_c.union(n))