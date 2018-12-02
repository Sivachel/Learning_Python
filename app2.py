#Working with strings
print("Giraffe \nacademy") #inserts as new line
print("Giraffe \"academy") #use blackslash for escape character


phrase = "python"
print(phrase + "is cool")

#Calling fucntions to modify strings
phrase = "python"
print(phrase.upper()) #all upper case
print(phrase.lower()) #all lower case
print(phrase.isupper()) #boolean check
print(phrase.upper().isupper()) #uppercase and boolean check
print(len(phrase)) #length of the string
print(phrase[0]) #access the character in that index
print(phrase.index("y")) #tells  the index of the letter in the string
print(phrase.replace("python", "csharp")) #tells  the index of the letter in the string

#Working with numbers
print(2) #can print any number including decimals, negative numbers
print(2 + (5*3)) #can do complicated maths problem
my_num = 5
print(my_num) #will print this
print(str(my_num) +" is my favourite number") #needs to converted to string when using with a string

#Some maths function
print(abs(my_num)) #gives the absoulte value
print(pow(3,2)) #power of any numbers
print(max(7,8)) #prints largest number

#to use more external code use import funtion
from math import *
print(floor(3.2))
print(ceil(3.2))
print(sqrt(2))
