n_partidas = int(input('N partidas: '))
lista_pontuacao = []

for i in range(n_partidas):
    identificador = f"R{i+1}"
    pontuacao = int(input(f'pontuacao da {identificador}: '))
    dado_partida = (identificador, pontuacao)
    lista_pontuacao.append(dado_partida)

# Se a lista estiver vazia, prevenimos erros
if len(lista_pontuacao) > 0:
    melhor_tamanho = 1
    melhor_inicio = 0  # Índice inicial da melhor sequência
    
    tamanho_atual = 1
    inicio_atual = 0   # Índice onde a sequência atual começou
    
    # Percorremos a lista a partir do segundo elemento (índice 1)
    for i in range(1, len(lista_pontuacao)):
        # Comparamos a pontuação atual com a anterior usando o índice [1] da tupla
        if lista_pontuacao[i][1] > lista_pontuacao[i-1][1]:
            tamanho_atual += 1
        else:
            # A sequência quebrou! Vamos ver se a que terminou era a maior até agora
            if tamanho_atual > melhor_tamanho:
                melhor_tamanho = tamanho_atual
                melhor_inicio = inicio_atual
            
            # Reiniciamos a contagem para uma nova sequência a partir daqui
            inicio_atual = i
            tamanho_atual = 1
            
    # Verificação final caso a maior sequência termine exatamente no último elemento da lista
    if tamanho_atual > melhor_tamanho:
        melhor_tamanho = tamanho_atual
        melhor_inicio = inicio_atual

    # Extraímos os valores que compõem essa maior sequência para exibir
    valores_sequencia = []
    for i in range(melhor_inicio, melhor_inicio + melhor_tamanho):
        valores_sequencia.append(lista_pontuacao[i][1])

    print("\n--- Resultados ---")
    print(f"Maior sequência: {valores_sequencia}")
    print(f"Comprimento: {melhor_tamanho}")
    # Como as partidas no enunciado começam em 1, somamos 1 ao índice do Python
    print(f"Posição inicial: {melhor_inicio + 1}")