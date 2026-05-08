vhoras= float(input("informe o valor da hora: "))
horas= float(input("informe a quantidade de horas trabalhadas: "))

salariobrut= horas*vhoras
inss= salariobrut * 0.10
fgts= salariobrut* 0.11
valordescontos= fgts+inss
salarioliq= salariobrut - inss - fgts

if salariobrut<= 900:
    print("Salário Bruto: ",  salariobrut)
    print("IR:  ","isento")
    print("FGTS:  ", fgts)
    print("Total descontos: ", valordescontos)
    print("Salário líquido:  ", salarioliq)

elif salariobrut<= 1500:
    result=  salariobrut* 0.05
    valordescontos2= inss+fgts+result
    salarioliq2= salariobrut-result-fgts-inss
    print("Salário Bruto: ",  salariobrut)
    print("IR:  ", result)
    print("Total descontos: ", valordescontos2)
    print("Salário líquido:  ", salarioliq2)
elif salariobrut<= 2500:
    result2= salariobrut* 0.1
    valordescontos3=  inss+fgts+result2
    salarioliq3= salariobrut- inss- fgts- result2
    print("Salário Bruto: ",  salariobrut)
    print("IR:  ", result2)
    print("Total descontos: ", valordescontos3)
    print("Salário líquido:  ", salarioliq3)
elif salariobrut>2500: 
    result3= salariobrut* 0.2
    valordescontos4= inss+fgts+result3
    salarioliq4= salariobrut-inss-fgts-result3
    print("Salário Bruto: ",  salariobrut)
    print("IR:  ", result3)
    print("Total descontos: ", valordescontos4)
    print("Salário líquido:  ", salarioliq4)
    



