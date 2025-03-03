#Write a program that prompts the user to create an empty list. Then, the user should be able to add elements to the list using three different methods: append(), extend(), and insert().
#Use append() to add a single element to the end of the list.
#Use extend() to add multiple elements (from another list or iterable) at the end of the list.
#Use insert() to add an element at a specific index in the list.
#Use remove() to remove a specific element by its value.
#Use pop() to remove an element at a specific index.
#The user should be able to add elements of different types (e.g., int, float, str) to the list.
#Demonstrate adding elements using all three methods.


ls = []
print("Commands list:")
print("Append")
print("Extend")
print("Insert")
print("Remove")
print("Pop")
print("Exit")


input_command = ""

active = 1

while active or input_command != "exit":
	input_command = input("Please enter the command: ")
	if str.lower(input_command) == "append":
		input_element = input("Please enter the one element: ")
		if input_element.isalpha():
			ls.append(input_element)
			print(ls)
		elif input_element.isdigit():
			input_element = int(input_element)
			ls.append(input_element)
			print(ls)
		else:
			input_element = float(input_element)
			ls.append(input_element)
			print(ls)
	elif str.lower(input_command) == "extend":
		input_element = (input("Please enter the elements: ").split())
		for i in range(len(input_element)-1):
			if input_element[i].isalpha():
				pass
			elif input_element[i].isdigit():
				input_element[i] = int(input_element[i])
			else:
				input_element[i] = float(input_element[i])
		ls.extend(input_element)
		print(ls)
	elif str.lower(input_command) == "insert":
		input_element = input("Please enter the one element: ")
		input_position = int(input("Please enter the postion of element: "))
		if input_element.isalpha():
			ls.insert(input_position,input_element)
			print(ls)
		elif input_element.isdigit():
			input_element = int(input_element)
			ls.insert(input_position,input_element)
			print(ls)
		else:
			input_element = float(input_element)
			ls.insert(input_position,input_element)
			print(ls)
	elif str.lower(input_command) == "remove":
		if len(ls) != 0:
			print(f"What element you want to remove - {ls} ")
			input_element = input("Please enter the element: ")
			ls.remove(input_element)
			print(ls)
		else:
			print("Your list is empty!")
	elif str.lower(input_command) == "pop":
		if len(ls) != 0:
			print(f"What element you want to remove - {ls} ")
			input_element = input("Please enter the element: ")
			if input_element.isalpha():
				pass
			elif input_element.isdigit():
				input_element = int(input_element)
			else:
				input_element = float(input_element)
			ls.pop(ls.index(input_element))
			print(ls)
		else:
			print("Your list is empty!")
	elif str.lower(input_command) == 'exit':
		break
	else:
		print('Wrong command!')
		break