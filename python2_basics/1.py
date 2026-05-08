x = int(input("insira a numero: "))
y = int(input("insira o numero: "))
z = int(input("insira o numero: "))

if x< y < z:
    print(z, y, x)
elif y<x<z:
        print(z, x, y)
elif z<y<x:
      print(x, y, z)
elif x<z<y:
      print(y, z , x)
    