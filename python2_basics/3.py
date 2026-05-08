sal= float(input("insira seu salário: "))

valor1= sal * 0.2
result1= valor1 + sal

valor2= sal * 0.15
result2= sal + valor2

valor3= sal * 0.1
result3= sal + valor3


if sal<= 280.00:
    print(sal)
    print("20%")
    print("valor do aumento:", valor1)
    print("apos o reajuste:",result1)
elif sal== 280.00 and sal<= 700.00:
    print(sal)
    print("15%")
    print("valor do aumento:", valor2)
    print("após o reajuste:", result2 )
elif sal==700.00 and sal<= 1500.00:
    print(sal)
    print("10%")
    print("valor do aumento:", valor3)
    print("apos o reajuste: ", result3)
    
