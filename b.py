l0 = [2,5,6]


#l1 = []
#for el in l0:
#    l1.append(el*el)

#print(l1)

l1 = [el*el for el in l0]
print(l1)
#l1 contiene elementi pari di l0 elevati al quadrato
#posso farlo con un ciclo oppure con una list comprehension

l1 = [el*el for el in l0 if el % 2 == 0]
print(l1)

def check_even_odd(a: int):
    if a%2:
        print("Even")
    else:
        print("Odd")

#funzione even odd che si può fare con una lambda expression
even_odd = lambda a: "Even" if a % 2 == 0 else "Odd"
l = [1,2,3]
for el in l:
    check_even_odd(el)


def add_one(a:int) -> int:
    return a+1

l = [1,2,3]
l1 = []
for el in l:
    l1.append(add_one(el))

#Fa la stessa cosa del ciclo sopra ma in maniera più compatta
l = map(add_one,l)