def leiaInt(num):
    while True:
        digitos = input("Informe os dígitos do cartão: ")
        if digitos.isnumeric():
            return digitos
        else:
            print('ERRO!')


digitos = leiaInt("Informe os dígitos do cartão: ")

caracteres = int(len(digitos))
tamanho = caracteres/2

lista = []
resto = []

i = caracteres
while (tamanho > 0):
    i -= 2
    lista.append(int(digitos[i]) * 2)
    resto.append(int(digitos[i+1]))
    tamanho -= 1

tamanho = int(caracteres/2)
j = 0
soma = 0
while (j < tamanho):
    if (lista[j] >= 10):
        s = lista[j] - 10
        soma = (s + 1) + soma
        lista[j] = 0
    j = j + 1

resultado = sum(lista) + soma
final = str(resultado + sum(resto))

if (final[0] == '0'):
    print('INVALID!')
elif (caracteres >= 13 and final[1] == '0'):
    if (caracteres == 15):
        print('AMERICAN EXPRESS!')
    elif (str(digitos[0]) == '4' and (caracteres == 13 or caracteres == 16)):
        print('VISA!')
    elif (caracteres == 16):
        print('MASTERCARD!')
else:
    print('INVALID!')