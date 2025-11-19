# 1. Organizando Caixas Empilhadas
# Um depósito precisa verificar quantas caixas estão empilhadas. O sistema recebe o número de caixas em cada pilha (ex.: [3, 5, 2]) e deve calcular o total de caixas. Use recursão para percorrer a lista.
# 👉 Exemplo: Entrada [3, 5, 2] → Saída 10.

def caixasEmpilhadas(lista: list, contador: int) -> int:
    contador += 1
    return lista[contador] + (caixasEmpilhadas(lista, contador)) if contador < len(lista) else 0

print(caixasEmpilhadas([3, 5, 2], -1)) 

# 2. Calculando Descontos Progressivos
# Uma loja aplica descontos progressivos em produtos: o primeiro item tem 10%, o segundo 20%, o terceiro 30%, e assim por diante. Crie uma função recursiva que receba uma lista de preços e retorne o valor total a ser pago.
# 👉 Exemplo: [100, 200, 300] → Saída 100*0.9 + 200*0.8 + 300*0.7.

def descontos(lista: list, desconto: int, contador: int) -> int:
    contador += 1
    desconto -= 0.1
    return (lista[contador] * desconto) + descontos(lista, desconto, contador) if contador < len(lista) else 0

print(descontos([100, 200, 300], 1, -1))

# 3. Subindo uma Escada
# Um atleta pode subir a escada dando 1 ou 2 passos de cada vez. Dado o número de degraus, crie uma função recursiva que retorne de quantas formas diferentes ele pode subir.
# 👉 Exemplo: Entrada 4 → Saída 5.

def escadas(entrada: int) -> int:
    if entrada == 1:
        return 1
    elif entrada == 2:
        return 2
    else:
        return escadas(entrada - 1) + escadas(entrada - 2)
    
print(escadas(5))

# 4. Explorando Diretórios
# Um sistema de backup precisa contar quantos arquivos existem em um conjunto de pastas, que podem conter outras pastas recursivamente. Simule isso com listas aninhadas, onde uma string é um arquivo e uma lista é uma pasta.
# 👉 Exemplo: ["a.txt", ["b.txt", "c.txt"]] → Saída 3.

def diretorios(linhas: list) -> int:
    contador = 0
    for i in linhas:
        if isinstance(i, str):
            contador += 1
        elif isinstance(i, list):
            contador += diretorios(i)
    return contador

print(diretorios(["a.txt", ["b.txt", "c.txt"], [["b.txt", "c.txt"], "b.txt", "c.txt"]]))

# 5. Contagem Regressiva com Alerta
# Um foguete faz uma contagem regressiva antes de decolar. Implemente uma função recursiva que imprima os números de n até 0 e ao final escreva "Decolar!".
# 👉 Entrada: 5 → Saída: 5, 4, 3, 2, 1, 0, Decolar!.

def contagemRegressiva(entrada: int) -> str:
    string = ""
    string += f"{entrada}, " + contagemRegressiva(entrada - 1) if entrada > 0 else f"{entrada}, Decolar!."
    return string

print(contagemRegressiva(5))

# 6. Verificação de Palíndromo
# Um sistema de mensagens precisa verificar se a palavra enviada é um palíndromo. Crie uma função recursiva que retorne True ou False.
# 👉 Exemplo: "radar" → True.

def palindromo(palavra: str, posicao: int = 0) -> bool:
    if palavra[posicao] == palavra[-posicao]:
        posicao += 1
        palindromo(palavra, posicao)
    else:
        return False
    return True
        
print(palindromo("radar"))

# 7. Fatorial com Explicação Passo a Passo
# Um professor pediu que você mostre como o fatorial é construído. Crie uma função recursiva que mostre cada multiplicação até o resultado final.
# 👉 Entrada: 5 → Saída: "5 * 4 * 3 * 2 * 1 = 120".

def fatorial(entrada: int) -> str | tuple[str, int]:

    if entrada == 1:
        return "1,1"
    
    Anterior = fatorial(entrada - 1)
    stringAnterior, valorAnteriorSTR = Anterior.split(",")

    valorAtual = int(valorAnteriorSTR) * entrada
    
    stringSaida = f"{entrada} * {stringAnterior}"

    return f"{stringSaida}, {valorAtual}"

fator = fatorial(5).split(", ")
print(f"{fator[0]} = {fator[1]}")

# 8. Soma dos Dígitos de um Número
# Um caixa eletrônico precisa verificar a soma dos dígitos de um número de conta. Crie uma função recursiva que faça essa soma.
# 👉 Entrada: 987 → Saída: 24.

def digitos(num: str, contador: int = 0) -> int:
    return int(num[contador]) + digitos(num, contador + 1) if contador < len(num) else 0

print(digitos("987"))

# 9. Sequência de Fibonacci para Estoque
# Um agricultor descobriu que a reprodução dos coelhos segue a lógica da sequência de Fibonacci. Crie uma função recursiva que dado um mês, informe quantos pares de coelhos existirão.
# 👉 Entrada: 6 → Saída: 8.

def fibonacciCoelhos(entrada: int) -> int:
    if entrada < 0:
        return 0
    elif entrada == 1:
        return 1
    else:
        return fibonacciCoelhos(entrada - 1) + fibonacciCoelhos(entrada - 2)

print(fibonacciCoelhos(4))

# 10. Quebra de Moedas
# Uma máquina precisa devolver troco, mas só tem moedas de 1 e 2 reais. Crie uma função recursiva que calcule de quantas formas diferentes é possível devolver um troco de valor n.
# 👉 Entrada: 4 → Saída: 3 formas (2+2, 2+1+1, 1+1+1+1).

def trocos(entrada: int) -> str:
    if entrada == 1:
        return 1
    elif entrada == 2:
        return 2
    else:
        return trocos(entrada - 2) + 1
    
print(trocos(4))