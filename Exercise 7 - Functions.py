my_list= [*range(5)]
x=lambda func:pow(func,2)

for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
                print(x(my_list[i]))





