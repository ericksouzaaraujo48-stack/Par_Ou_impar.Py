def selecionar_numero():
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
            return n
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")



def numero_par_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"

def main():
    numero = selecionar_numero()
    resultado = numero_par_impar(numero)
    print(f"O número {numero} é {resultado}.")
if __name__ == "__main__":
    main()