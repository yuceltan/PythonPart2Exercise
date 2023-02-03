import random

def random_list_summer():
    random_number=random.randint(-100,100)
    return random_number


randomList=[]
x=0
for i in range(0,15):
   randomList.append(random_list_summer())
   Sum=sum(randomList)

print("First element of list is:",randomList[0])
print("Sum of all elements:",Sum)