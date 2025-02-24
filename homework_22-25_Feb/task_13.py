"""Write a program that takes a sentence and splits it into words, then joins the
words back into a sentence with hyphens (-) between them."""

print("Please enter the sentence")

str_1 = str(input())
print("-".join((str_1.split(" "))))
