#Um singelo projeto pessoal calculadora em python, desenvolvido por Alan teixeira freires em 02/01/2026.

def mostrar_creditos():
    print("-" * 30)
    print("      CALCULADORA DO ALAN")
    print("    Versão 1.0 - Jan/2026")
    print("-" * 30)

mostrar_creditos()

class calculadora:
    def __init__(self):
        pass
    def somar(self, n1, n2):
        return n1 + n2
    def subtrair(self, n1, n2):
        return n1 - n2
    def multiplicar(self, n1, n2):
        return n1 * n2
    def dividir(self, n1, n2):
        if n2 == 0:
            return "Erro! Divisão por zero."
        return n1 / n2

calc = calculadora()

while True:
    print("\n--- Calculadora Python ---")
    print("1. Somar | 2. Subtrair | 3. Multiplicar | 4. Dividir | 0. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Obrigado por usar a calculadora!")
        break  
    
    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {calc.somar(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {calc.subtrair(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {calc.multiplicar(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {calc.dividir(num1, num2)}")
    else:
        print("Opção inválida! Tente novamente.")