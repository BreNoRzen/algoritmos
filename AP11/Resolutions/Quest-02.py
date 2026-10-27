n_robos = int(input('N robos: '))
lista_robos = []


for i in range(n_robos):
    identificador = f"R{i+1}"
    etapa_1 = int(input(f'[{identificador}] etapa 1 em (S): '))
    etapa_2 = int(input(f'[{identificador}] etapa 2 em (S): '))
    etapa_3 = int(input(f'[{identificador}] etapa 3 em (S): '))
    

    dados_robo = (identificador, etapa_1, etapa_2, etapa_3)
    lista_robos.append(dados_robo)

print("\n--- Resultados Individuais ---")

for robo in lista_robos:
    id_robo = robo[0]
    t1 = robo[1]
    t2 = robo[2]
    t3 = robo[3]
    
    tempo_total = t1 + t2 + t3
    print(f"Robô {id_robo}: tempo total de {tempo_total} segundos.")


vencedor = lista_robos[0]
v_t1, v_t2, v_t3 = vencedor[1], vencedor[2], vencedor[3]
menor_tempo_total = v_t1 + v_t2 + v_t3


maior_venc = v_t1
if v_t2 > maior_venc:
    maior_venc = v_t2
if v_t3 > maior_venc:
    maior_venc = v_t3
etapa_mais_lenta_vencedor = maior_venc

for robo in lista_robos:
    id_r = robo[0]
    t1, t2, t3 = robo[1], robo[2], robo[3]
    total = t1 + t2 + t3
    
    maior_atual = t1
    if t2 > maior_atual:
        maior_atual = t2
    if t3 > maior_atual:
        maior_atual = t3
    etapa_lenta_atual = maior_atual
    
    if total < menor_tempo_total:
        menor_tempo_total = total
        etapa_mais_lenta_vencedor = etapa_lenta_atual
        vencedor = robo
    
    elif total == menor_tempo_total:
        if etapa_lenta_atual < etapa_mais_lenta_vencedor:
            menor_tempo_total = total
            etapa_mais_lenta_vencedor = etapa_lenta_atual
            vencedor = robo

print("\n--- Resultado Final ---")
print(f"Vencedor: {vencedor[0]}")
print(f"Tempo total: {menor_tempo_total}")
print(f"Etapa mais lenta: {etapa_mais_lenta_vencedor}")
