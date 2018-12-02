#Lists
friends = ["kevin", "karen", "Jim", "Oscar", "toby"]
friends[1] = "Mike" #to change an item in the list
print(friends) #to access the whole list
print(friends[0]) #to access a item form the list
print(friends[-2]) #to access a item form the list in reverse but index starts form -1
print(friends[1:3]) #to access a list from index 1 to 2
print(friends[1:]) #to access everything from 1 and so on


#List Functions
lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin", "karen", "Jim", "Oscar", "toby"]
#friends.extend(lucky_numbers) #to add two lists together
friends.append("Creed") #to add another item to the list
friends.insert(1,"Kelly") #to insert a string in the desired index
friends.remove("Jim") #to remove a string
friends.pop() #removes a string off the list
#friends.clear() #to clear a list
friends.sort() #sorts the list alphabetically
friends.count("Jim") #counts the number of jim in the list
lucky_numbers.reverse() #t reverse a list
friends2 = friends.copy() #to copy a list to a new one

print(friends)
print(friends.index("Oscar")) #to check if a string exits in the list
