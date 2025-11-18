# 1. Cadastro de Contatos em TXT
# Enunciado: Armazene cada contato em uma linha no formato nome;telefone1,telefone2,.... Implemente operações: ADD, DEL, FIND, LIST. Grave e leia do mesmo arquivo.
# Entrada (exemplo): ADD Ana;11-9999-1234, ADD Bia;11-8888-0000, FIND Ana
# Saída (exemplo): Ana;11-9999-1234.

def cadastroTXT(textoComandos: str) -> str:
    def separarComandoDados(texto: str) -> list:
        textoSeparado = texto.split()
        if textoSeparado[0] == "ADD":
            dadosSeparados = textoSeparado[1].split(";")
            return textoSeparado[0], dadosSeparados[0], dadosSeparados[1], dadosSeparados[2] if len(dadosSeparados) == 3 else None
        elif textoSeparado[0] == "LIST":
            return textoSeparado[0], None, None, None
        else:
            return textoSeparado[0], textoSeparado[1], None, None
        
    def salvarTXT(texto: str) -> None:
        with open("cadastros.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.writelines(texto)
    
    def lerTXT(texto: str | None) -> None:
        with open("cadastros.txt", "r", encoding="UTF-8") as arquivo:
            resultado = arquivo.readlines()
        
        if texto:
            for i in resultado:
                info = i.split(";")
                if info[0].lower() == texto.lower():
                    print("".join(i.replace("\n", '')))
        else:
            for j in resultado:
                print("".join(j.replace("\n", '')))

    def apagarTXT(nome: str) -> None:
        with open("cadastros.txt", "r", encoding="UTF-8") as arquivo:
            resultado = arquivo.readlines()

        for k, valor in enumerate(resultado):
            informacoes = valor.split(";")
            if informacoes[0] == nome:
                resultado.pop(k)
        
        with open("cadastros.txt", "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(resultado)
        
    textoComandosFormatado = textoComandos.split(", ")
    for parte in textoComandosFormatado:
        comando, nome, telefone1, telefone2 = separarComandoDados(parte)

        if comando == "ADD":
            salvarTXT(f"{nome};{telefone1}\n" if telefone2 == None else f"{nome};{telefone1};{telefone2}\n")
        elif comando == "LIST":
            lerTXT(None)
        elif comando == "DEL":
            apagarTXT(nome)
        elif comando == "FIND":
            lerTXT(nome)
        
cadastroTXT("ADD Ana;11-9999-1234, ADD Bia;11-8888-0000, ADD alice;13-98811-3565;13-3471-8373, FIND Ana, DEL Ana, LIST")

# 2. Relatório de Vendas (CSV)
# Enunciado: Dado um vendas.csv com colunas data, produto, qtd, preco, calcule faturamento total, por produto e por mês (AAAA-MM). Gere um arquivo relatorio.txt.
# Entrada (exemplo): linhas como 2025-03-01,caneta,10,2.50
# Saída (exemplo): em relatorio.txt, total=..., caneta=..., 2025-03=....

def criadorDeRelatorio(csv: str, relatorio: str) -> None:
    with open(csv, "r", encoding="UTF-8") as arquivo:
        csvLido = arquivo.readlines()

    total = 0
    totalAuxiliar = 0
    dicioRelatorioProduto = {}
    dicioRelatorioData = {}

    for linha in csvLido:
        partesLinha = linha.split(",")
        totalAuxiliar += int(partesLinha[2]) * float(partesLinha[3])
        total += totalAuxiliar
        data = partesLinha[0]
        produto = partesLinha[1]

        if not produto in dicioRelatorioProduto.keys():
            dicioRelatorioProduto[produto] = totalAuxiliar
        else:
            dicioRelatorioProduto[produto] += totalAuxiliar

        if not data in dicioRelatorioData.keys():
            dicioRelatorioData[data] = totalAuxiliar
        else:
            dicioRelatorioData[data] += totalAuxiliar
    
    with open(relatorio, "w", encoding="UTF-8") as arquivoNovo:
        for key in dicioRelatorioData.keys():
            arquivoNovo.writelines(f"{key}={dicioRelatorioData[key]:.2f}\n")

        for key in dicioRelatorioProduto.keys():
            arquivoNovo.writelines(f"{key}={dicioRelatorioProduto[key]:.2f}\n")

        arquivoNovo.writelines(f"total={total:.2f}")
        
criadorDeRelatorio("Lista05/vendas.csv", "relatorio.txt")

# 3. Leitura de Log e Contagem de Severidades
# Enunciado: Leia um arquivo de log onde cada linha começa com INFO|WARN|ERROR|DEBUG. Conte ocorrências por nível e liste as 5 mensagens ERROR mais recentes.
# Entrada (exemplo): várias linhas
# Saída (exemplo): INFO=15, WARN=4, ERROR=2, DEBUG=20, últimos ERROR: [...].

def logSeveridades(txt: str) -> str:
    with open(txt, "r", encoding="UTF-8") as arquivo:
        texto = arquivo.readlines()
    
    erros = []
    qntInfo = 0
    qntWarn = 0
    qntDebug = 0
    
    for l in texto:
        linhaNova = l.split("|")

        if linhaNova[0] == "INFO":
            qntInfo += 1
        elif linhaNova[0] == "WARN":
            qntWarn += 1
        elif linhaNova[0] == "DEBUG":
            qntDebug += 1
        else:
            erro = linhaNova[2].removesuffix("\n")
            erros.append(erro)
    
    return f"INFO={qntInfo}, WARN={qntWarn}, ERROR={len(erros)}, DEBUG={qntDebug}, últimos ERROR: {[elemento for elemento in erros[-6:-1]]}"

print(logSeveridades("Lista05/log.txt"))

# 4. Busca e Índice Invertido (TXT)
# Enunciado: Dado um texto grande, crie um índice invertido (palavra → posições). Permita consultas por termo, retornando em quais posições/linhas ele aparece. Salve o índice em JSON.
# Entrada (exemplo): arquivo livro.txt
# Saída (exemplo): "algoritmo": [12, 45, 46].

def indiceInvertido(text: str, palavra: str) -> str:
    with open(text, "r", encoding="UTF-8") as arquivo:
        meuTexto = arquivo.read()
    
    dicionarioPalavras = {}
    textoEmPalavras = meuTexto.split()

    for ind, palavrinha in enumerate(textoEmPalavras):
        if not palavrinha.lower() in dicionarioPalavras.keys():
            dicionarioPalavras[palavrinha.lower()] = [ind]
        else:
            dicionarioPalavras[palavrinha.lower()].append(ind)
    
    for p in dicionarioPalavras.keys():
        if p == palavra.lower():
            return f'"{palavra}": {dicionarioPalavras[palavra]}'
    return "Nada encontrado"
            
print(indiceInvertido("Lista05/textinho.txt", "algoritmos"))

# 5. Frequência de Palavras com Stopwords
# Enunciado: Leia um .txt, remova pontuação e stopwords (arquivo stopwords.txt), e gere um top_20.csv com as 20 palavras mais frequentes e suas contagens.
# Entrada (exemplo): texto.txt e stopwords.txt
# Saída (exemplo): top_20.csv com palavra,contagem.

def frquenciaPalavras(txt: str, stopwords: str) -> str:
    with open(txt, "r", encoding="UTF-8") as arquivoTxt:
        with open(stopwords, "r", encoding="UTF-8") as arquivoStop:

            stop = arquivoStop.readlines()
            txtzinho = arquivoTxt.read()
    
    textoPartido = txtzinho.split()
    
    dicionarioContagem = {}
    for part in textoPartido:
        if not part in dicionarioContagem.keys():
            dicionarioContagem[part] = 1
        else:
            dicionarioContagem[part] += 1

    dicionarioOrdenado = sorted(dicionarioContagem.items(), key=lambda item: item[1], reverse=True)

    with open("top_20.csv", "w", encoding="UTF-8") as arquivo:
        for contador, tupla in enumerate(dicionarioOrdenado, start=1):
            if contador <= 20:
                arquivo.writelines(f"{tupla[0]},{tupla[1]}\n")

frquenciaPalavras("Lista05/.txt", "Lista05/stopwords.txt")

# 6. Controle de Presença (CSV)
# Enunciado: Um arquivo presenca.csv tem colunas aluno, data, presente(0/1). Gere um relatório com faltas acumuladas por aluno e percentual de presença.
# Entrada (exemplo): Ana,2025-03-10,1
# Saída (exemplo): Ana: 80% presença (faltas=2/10).

def controlePresenca(presenca: str, relatorio: str) -> None:
    with open(presenca, "r", encoding="UTF-8") as arquivo:
        listaPresenca = arquivo.readlines()

    dicioAux = {}
    for prt in listaPresenca:
        separado = prt.split(",")
        if not separado[0] in dicioAux.keys():
            dicioAux[separado[0]] = [1, 1 if separado[2] == "1" else 0]
        else:
            listaTemp = dicioAux[separado[0]]
            dicioAux[separado[0]] = [1 + listaTemp[0], 1 + listaTemp[1] if separado[2] == "1" else listaTemp[1]]
    
    with open(relatorio, "w", encoding="UTF-8") as arquivo:
        for ky, vlue in dicioAux.items():
            arquivo.writelines(f"{ky}: {(vlue[1] / vlue[0]) * 100:.0f}% presença (faltas={vlue[1]}/{vlue[0]})\n")

controlePresenca("Lista05/presenca.csv", "relatoriozin.txt")

# 7. Programa que copia conteúdo de um arquivo para outro
# Escreva um programa que abra um arquivo de texto existente (por exemplo, entrada.txt) e copie todo o seu conteúdo para um novo arquivo chamado saida.txt.

# Entrada: um arquivo entrada.txt já existente com algumas linhas de texto.
# Saída: criação do arquivo saida.txt com o mesmo conteúdo.

# Exemplo de entrada (entrada.txt):
# Python é divertido.
# Aprender programação é importante.

# Exemplo de saída (saida.txt):
# Python é divertido.
# Aprender programação é importante.

def copiaTexto(caminho1: str, caminho2: str) -> None:
    with open(caminho1, "r", encoding="UTF-8") as arquivo:
        textoOriginal = arquivo.read()

    with open(caminho2, "w", encoding="UTF-8") as arquivo:
        arquivo.write(textoOriginal)

copiaTexto("Lista05/entrada.txt", "Lista05/saida.txt")

# 8. Programa que insere texto ao final de um arquivo
# Faça um programa que peça ao usuário para digitar uma frase e a salve no final de um arquivo chamado anotacoes.txt. O programa deve manter o que já estava no arquivo, adicionando apenas a nova frase.

# Entrada: "Hoje estudei algoritmos."
# Saída (anotacoes.txt após execução):

# [conteúdo já existente no arquivo]
# Hoje estudei algoritmos.

def adicionaTxt(caminhoExistente: str, frase: str) -> None:
    with open(caminhoExistente, "a", encoding="UTF-8") as arquivo:
        arquivo.write(frase)

adicionaTxt("Lista05/entrada.txt", "\nEu amo o Palmeiras!")

# 9. Programa que lê números de um arquivo e calcula a média
# Crie um programa que leia números inteiros salvos em um arquivo numeros.txt (um número por linha) e calcule a média aritmética desses valores.

# Entrada (numeros.txt):
# 10
# 20
# 30
# 40

# Saída no console:
# A média dos números é 25.0

def somaTxt(caminhoEscolhido: str) -> str:
    with open(caminhoEscolhido, "r", encoding="UTF-8") as arquivo:
        nums = arquivo.readlines()

        nums = list(map(lambda x: int(x), nums))

    return f"A média dos números é {sum(nums)/len(nums)}"

print(somaTxt("Lista05/numeros.txt"))

# 10. Programa que substitui palavras em um arquivo
# Escreva um programa que leia um arquivo de texto chamado mensagem.txt e substitua todas as ocorrências da palavra "erro" por "acerto", salvando o resultado em um novo arquivo chamado mensagem_corrigida.txt.

# Entrada (mensagem.txt):
# O aluno cometeu um erro.
# Outro erro foi encontrado.

# Saída (mensagem_corrigida.txt):
# O aluno cometeu um acerto.
# Outro acerto foi encontrado.

def substituicao(caminho: str, palavraEscolhida: str, substituicao: str) -> None:
    with open(caminho, "r", encoding="UTF-8") as arquivo:
        textos = arquivo.readlines()

    for tex in textos:
        linh = tex.split()
        for n, li in enumerate(linh):
            if li == palavraEscolhida:
                linh.pop(n)
                linh.insert(n, substituicao)

        with open("Lista05/mensagem_corrigida.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.writelines(f"{' '.join(linh)}\n")

substituicao("Lista05/mensagem.txt", "erro", "acerto")