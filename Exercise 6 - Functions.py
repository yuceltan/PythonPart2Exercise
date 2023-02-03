def fibonacci():
    x =0
    j =1
    for i in range(0,5):
        print(x)
        out=x+j
        x=j
        j=out
        i+=1

fibonacci()