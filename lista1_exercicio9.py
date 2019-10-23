peso=float(input())
altura=float(input())
imc=peso/(altura**2)
print ("{0:.2f}".format(imc))
if imc < 18.5:
    print("Baixo peso")
if imc >= 18.5 and imc < 24.9:
    print("Peso normal")
if imc >= 24.9 and imc <29.9:
    print("Sobrepeso")
    peso_minimo_necessario = float(peso - (24.9*(altura**2)))
    print("{0:.2f}".format(peso_minimo_necessario))
if imc >= 29.9 and imc <34.9:
    print("Obesidade Grau I")
    peso_minimo_necessario = float(peso - (24.9*(altura**2)))
    print("{0:.2f}".format(peso_minimo_necessario))
if imc >= 34.9 and imc <39.9:
    print("Obesidade Grau II")
    peso_minimo_necessario = float(peso - (24.9*(altura**2)))
    print("{0:.2f}".format(peso_minimo_necessario))
if imc >= 39.9:
    print("Obesidade Grau III")
    peso_minimo_necessario = float(peso - (24.9*(altura**2)))
    print("{0:.2f}".format(peso_minimo_necessario))
