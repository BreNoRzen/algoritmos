n_dias = int(input('N dias: '))
lista = []
soma = 0

for i in range(n_dias):
    consumo_diario = int(input('consumo diario: '))
    soma += consumo_diario
    lista.append(consumo_diario)

media = soma / n_dias
print(f"Média: {media}")

maior_consumo_registrado = lista[0]

for valor in lista:
    if valor > maior_consumo_registrado:
        maior_consumo_registrado = valor

dias_acima_media = []

for i in range(len(lista)):
    if lista[i] > media:
        dias_acima_media.append(i + 1)

print("Dias acima da média:", dias_acima_media)
print("Quantidade:", len(dias_acima_media))