list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
#print(list1,tuple1,set1,dict1) #prints all
listed_key =list(dict1)
listed_values =list(dict1.values())
x =len(listed_key)
y =len(listed_values)

for i in range(len(listed_key)):
        for j in range(listed_values):

            print(listed_key[i])
            print(listed_values[j])
            break




