def add_it_up(x):
    a=[]
    b=0
    for i in range(x):
        a.append(i)
        b+=i
    return print(a,b)
        


m=int(input("Ingrese un numero"))
add_it_up(m)
