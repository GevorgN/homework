#Write a program to create a list and a tuple with some elements. Print them and display their types.

ls = [1, 25 , 47, 15]
tp = (1, 2, 47, 15)

print(ls)
print(f"ls type is {type(ls)}")
print(tp)
print(f"tp type is {type(tp)}")

#Write a program to count the occurrences of a specific element in a list and tuple.
print("Please write element for checking.")
check = int(input())
print(ls.count(check))
print(tp.count(check))

#Write a program to find and print the maximum and minimum values in a list and a tuple.

print(max(ls))
print(max(tp))
print(min(ls))
print(min(tp))

#Write a program to access elements from a nested list and a nested tuple.

ls_nested = [[1,2],[4,5]]
tp_nested = ((2,3),(6,7))
print(ls_nested[0][0])
print(ls_nested[1][1])
print(tp_nested[0][0])
print(tp_nested[1][1])

#Write a program to find the sum of all elements in a list and a tuple.

print(sum(ls))
print(sum(tp))

#Write a program to reverse a list and a tuple.
print(ls[::-1])
print(tp[::-1])
