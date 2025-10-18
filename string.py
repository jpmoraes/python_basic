nome = "Joao Pedro"

nome1 = nome[0:4]

print(nome1)

if 'o' and 'a' in nome1:
    print('OK')


nome = "Joao Pedro"

listnome = nome.split()

print(listnome[0])

data = "11/10/2025"
listdata = data.split('/')
dia = listdata[0]

print(dia)

chamada = ", ".join(listnome)

print(chamada.upper())