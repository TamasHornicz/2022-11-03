import random

lista = []


for i in range (20):
    lista.append(random.randint(0, 9)) 

print("Eredmények: ", ' '.join(map(str, lista))) 


print("Legnagyobb helység: ",max(lista))



lista = sorted(lista) 
while lista[0] == 0:
    lista.remove(lista[0])

kivonas = max(lista) - min(lista)
print("Külömbség: ",kivonas)


viz = 0
for i in lista:
    if i == 0:
        viz += 1

szárazfold = 20 - viz

if szárazfold > 10:
    print("Több a szárazföld")
elif viz > 10:
    print("Több a viz")
else:
    print("Ugyanannyi")