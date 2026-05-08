cont1= 0
cont2= 0
cont3= 0

for i in range(1, 11):
    rega= int(input("insira o numero"))
    if rega>0:
        cont1= cont1+1
    elif rega<0:
        cont2= cont2+1
    elif rega==0:
        cont3= cont3+1
print("temos ",cont1,"números positivos bro")
print("e tambem",cont2 ,"negativos broski")
print("não se esqueça que temos",cont3,"tambem")
