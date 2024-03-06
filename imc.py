# módulo_img
import estado_imc as calcular



peso = 0
altura = 0.0
nome = ""

nome = input("Digite seu nome: ")

erro = True

while erro:
    try:
        peso =  int(input("Digite seu peso: "))
        erro = False
    except:
        print("Valor inválido!")


erro = True
while erro:
     try:
        altura = float(input("Digite sua altura: "))
        erro = False
     except:
         print("Valor da altura está incorreto")


calcular.calcular_imc(peso, altura)




