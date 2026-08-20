# Verificador de Par ou Ímpar

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey)

Um programa simples em Python que solicita um número inteiro ao usuário e informa se ele é **par** ou **ímpar**, com tratamento de erros para entradas inválidas.

---

## Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Como Executar](#-como-executar)
- [Detalhamento do Código](#-detalhamento-do-código)
- [Exemplo de Saída](#-exemplo-de-saída)
- [Sobre o Autor](#-sobre-o-autor)

---

## Sobre o Projeto

Este programa foi desenvolvido como atividade da disciplina **Garantia da Qualidade de Software (Gestão e Qualidade de Software)**, ministrada pelo professor **Daniel Henrique Matos de Paiva**.

O objetivo principal do algoritmo é **verificar se um número inteiro fornecido pelo usuário é par ou ímpar**. O programa também trata entradas inválidas (como letras ou símbolos), pedindo repetidamente um valor até que um número inteiro válido seja digitado.

---

## Como Executar

### Pré-requisitos

- Ter o [Python 3](https://www.python.org/downloads/) instalado (versão 3.10 ou superior recomendada).

### Passo a passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/gqs-algoritmo-02-py.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd gqs-algoritmo-02-py
   ```

3. Execute o programa pelo terminal:
   ```bash
   python main.py
   ```
   > Em alguns sistemas (Linux/Mac) pode ser necessário usar `python3` em vez de `python`.

4. Digite um número inteiro quando solicitado e pressione **Enter**.

---

## Detalhamento do Código

O código está estruturado em três funções principais, seguindo boas práticas de organização e legibilidade:

| Função                  | Responsabilidade                                                                 |
|--------------------------|-----------------------------------------------------------------------------------|
| `selecionar_numero()`    | Solicita um número via `input()` e valida a entrada usando `try/except`          |
| `numero_par_impar(n)`    | Recebe um número e usa uma estrutura condicional `if/else` para classificá-lo    |
| `main()`                 | Função principal que orquestra a chamada das demais funções e exibe o resultado |

### Principais comandos e conceitos utilizados

- **`input()`** — captura o número digitado pelo usuário (como texto).
- **`int()`** — converte o texto digitado em um número inteiro.
- **`try/except ValueError`** — trata o erro caso o usuário digite algo que não seja um número inteiro, evitando que o programa quebre.
- **`while True`** — cria um laço de repetição que só é interrompido quando uma entrada válida é fornecida (`return`).
- **Estrutura condicional `if/else`** — verifica se o resto da divisão por 2 (`n % 2`) é igual a zero para determinar se o número é par ou ímpar.
- **`print()` com f-string** — exibe o resultado final formatado no console.
- **`if __name__ == "__main__":`** — garante que a função `main()` só seja executada quando o arquivo é rodado diretamente (boa prática em Python).

### Código-fonte (`main.py`)

```python
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
```

---

## Exemplo de Saída

### Caso 1 — Entrada válida (número par)

```
Digite um número inteiro: 8
O número 8 é Par.
```

### Caso 2 — Entrada válida (número ímpar)

```
Digite um número inteiro: 7
O número 7 é Impar.
```

### Caso 3 — Entrada inválida seguida de entrada válida

```
Digite um número inteiro: abc
Entrada inválida. Por favor, digite um número inteiro.
Digite um número inteiro: 12
O número 12 é Par.
```

---

## Sobre o Autor

Desenvolvido por Erick Souza Miranda Araujo, RA: 325130051

Projeto criado como parte da atividade **Lista de Exercícios II**, da disciplina de Garantia da Qualidade de Software.

---

<p align="center">Feito com 🐍 e muito ☕</p>
