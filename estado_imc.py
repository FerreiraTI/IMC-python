# Módulo estado_imc

def definir_estado_imc(imc):
    estado = ""
    if imc < 18.5:
        estado = "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        estado = "Peso ideal"
    elif imc >= 25 and imc < 30:
        estado = "Levemente acima do peso"
    elif imc >= 30 and imc < 35:
        estado = "Obesidade grau 1"
    elif imc >= 35 and imc < 40:
        estado = "Obesidade grau 2"
    else:
        estado = "Obesidade grau 3"

    print(f"O IMC dessa pessoa é: {imc: .2f} - {estado}.")

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    definir_estado_imc(imc)







def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    definir_estado_imc(imc)

