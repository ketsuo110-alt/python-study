1.lista= []
contador= 0
for i in range(10):
    valores= int(input("insira o numero"))
    lista.append(valores)

pesquisa= int(input("insira o número que quer ver: "))
for i in lista:
    if i== pesquisa:
      contador+=1
    
print(f"o {pesquisa} aparece {contador} vezes  ")





2.listanum= [ ]
contadordeadul= 0
contadordemenor= 0
contadoridoso= 0
for i in range(15):
    idades= int(input("insira as idades: "))
    listanum.append(idades)
    if idades>=18 and idades<=59:
        contadordeadul+=1
    elif idades< 18:
        contadordemenor+=1
    else:
        contadoridoso+=1

print(f"Quantidade de Adultos:{contadordeadul}| Quantidade de Menores de idade: {contadordemenor}| Quantidade de idosos {contadoridoso}")



3.lista= []
contador1= 0
contadorde2= 0
contador3= 0
contador4= 0
contador5= 0
for i in range (10):
    valores= int(input("insira o valor: "))
    if valores>5:
        print("apenas entre 1 e 5")
    lista.append(valores)

for i in lista:
    if i==1:
        contador1=+1
    elif i==2:
        contador2=+1
    elif i==3:
        contador3=+1
    elif i==4:
        contador4=+1
    elif i==5:
        contador5=+1

print(f"o numero 1 repete {contador1}vezes  o numero 2 repete  {contador2} o numero 3 repete, {contador3} o numero 4 repete {contador4} o numero 5 repete {contador5}")





5.def situação(media):
    if media>=7:
     return "aprovado"
    else:
       return"reprovado"

notas= []

for i in range(4):
    print(f"Notas do aluno {i+1}")
    colunas=[]
    for j in range(3):
       valores= float(input(f"insira a nota do aluno {i+1}:"))
       colunas.append(valores)
    notas.append(colunas)
   
media = sum(colunas) / len(colunas)
for id in notas:
    algo= situação(media)
    print(f"aluno {i+1} esta {algo} e sua media{media}:2f")


6.lista = []

for i in range(4):
    colunas=[]
    for j in range(5):
     valor= input("insira o numero: ")
     colunas.append(valor)
     colunas.append(lista)
     maiornum= max(valor)



maiornum= max(valor)

print("o maior num é :", maiornum)

7. 




8.


9.def vencedor( veia):
    for i in veia:
        if veia[i] == veia[i]:
            return "vencedor"
        elif veia[0][0] == veia [0][1] == veia[0][2]:
            return f"venceu{veia[0][1]}"
        elif veia [0][0] == veia [1][0] == veia [2][0]:
            return f"venceu{veia[0][0]}"
        elif veia [0][2]== veia [1][2]== veia == [2][2]:
            return f"venceu{veia[2][2]}"
        
        

veia= [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]


for i in veia:
    valor= input("insira o seu input (o X começa) em indice e coluna : ")
    for j in veia: 
        valor2 = input("insira o do O agora dnv indice e coluna : ")
        if valor2 == [0][0]:
            veia.insert[0][0]("O")
        elif valor2 == [0][1]:
            veia.insert[0][1]("O")
        elif valor2 == [0][2]:
            veia.insert[0][2]("O")
        elif valor2 == [1][0]:
            valor.insert[1][0]("O")
        elif valor2== [1][1]:
            valor.insert[1][1]("O") 
        elif valor2 == [1][2]:
            valor.insert[1][2]("O")
        elif valor2 == [2][0]:
            veia.insert[2][0]("O")
        elif valor2 == [2][1]:
            veia.insert[2][1]("O")
        elif valor2== [2][2]:
            veia.insert[2][2]("O") 
    if valor == [0][0]:
        veia.insert[0][0]("x")
    elif valor == [0][1]:
        veia.insert[0][1]("x")
    elif valor == [0][2]:
        veia.insert[0][2]("x")
    elif valor == [1][0]:
        valor.insert[1][0]("x")
    elif valor== [1][1]:
        valor.insert[1][1]("x") 
    elif valor == [1][2]:
        valor.insert[1][2]("x")
    elif valor == [2][0]:
        veia.insert[2][0]
    elif valor == [2][1]:
        veia.insert[2][1]("x")
    elif valor== [2][2]:
        veia.insert[2][2]("x")

winner =vencedor(veia)


