
#Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, պահպանումը բառարանում և ցուցակում,
#ապա ցույց կտա օգտատերերին ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։
#Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:

###########
#TO DO
###########

datbase = {
    "ID":{1},
    "Name":['test'],
    "LastName":['test2'],
    "Email":['test@gmail.com'],
    "Password":['pass'],
    "Phone":[000]
}
input_name = input("Enter the name: ")
input_pass = input("Enter the password: ")

#for key, value in datbase:
if input_name in datbase["Name"] and  input_pass in datbase["Password"]:
    for key, value in datbase.items():
        print(f"{key} - {value}")

#1. Movie Recommendation System (Dictionaries + Sets)
#Given a dictionary of users and the movies they have watched, suggest movies that their friends have watched but they haven’t.

user_movies = {
    "Alice": {"Inception", "Titanic", "Avatar"},
    "Bob": {"Inception", "The Matrix", "Avatar", "Interstellar"},
    "Charlie": {"Titanic", "The Godfather", "Inception"},
    "David": {"The Dark Knight", "The Godfather", "Interstellar"}
}

ls_movies = []

for key,value in user_movies.items():
	ls_movies.extend(user_movies[key])

ls_movies = set(ls_movies)
for key,value in user_movies.items():
	suggest_list = ls_movies - set(user_movies[key])
	print(f"Suggest list for {key} is '{suggest_list}'")


#2. Word Frequency Analyzer (Dictionaries)
#Given a paragraph of text, count how many times each word appears and find the most common words.


input_paragraph = list(input("Enter the paragraph: ").split())
dict_1 = {}

for i in input_paragraph:
	i = i.replace(".","")

for i in set(input_paragraph):
	dict_1[i] = input_paragraph.count(i)

max_num = 0
word = ''

for key, value in dict_1.items():
	if max_num < dict_1[key]:
		max_num = dict_1[key]
		word = key

print(f"Word '{word}' appears {max_num} times!")


#3. Social Media Friend Suggestion (Dictionaries + Sets)
#Suggest friends for a user by finding friends of friends who are not already direct friends.

friend_network = {
    "Alice": {"Bob", "Charlie"},
    "Bob": {"Alice", "David"},
    "Charlie": {"Alice", "Eve"},
    "David": {"Bob", "Eve"},
    "Eve": {"Charlie", "David"},
    "Frank": {"Grace"},
    "Grace": {"Frank"}
}

user_name = input("Enter the user name: ")

direct_friends = set(friend_network[user_name])
suggested_friends = []
for key in friend_network.keys():
	if user_name != key and key not in direct_friends:
		suggested_friends.append(key)




print(f"Friend suggestions for {user_name}: {suggested_friends}")



#4. Unique Product Categories (Dictionaries + Sets)
#Given a list of purchased products and their categories, return the unique product categories bought.

purchased_products = {
    "Laptop": "Electronics",
    "Headphones": "Electronics",
    "T-shirt": "Clothing",
    "Jeans": "Clothing",
    "Coffee Maker": "Home Appliances",
    "Blender": "Home Appliances",
    "Smartphone": "Electronics",
}

ls  = []
for key, value in purchased_products.items():
	ls.append(value)

print(set(ls))