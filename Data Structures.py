list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
print(len(list1),len(tuple1),len(set1),len(dict1)) #lenghts of all types question 1
print(list1[0],tuple1[0]) # question 2
print(dict1["lion"])# question 3

list1[1] = "rabbit"
print(list1)# question 4

listed= list(tuple1)
listed[1]="rabbit"
print(listed)# question 5

list1.append("rabbit")
print(list1) # question 6

list1.remove("rabbit")
print(list1) # question 7








