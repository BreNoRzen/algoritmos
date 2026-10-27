n_autorizados = int(input('digite o N de autorizados:'))

lista_autorizados = []

for i in range(n_autorizados):
    codigo = input('codigo: ')
    if codigo not in lista_autorizados:
        lista_autorizados.append(codigo)

m_tentativas = input('M tentativas:')
lista_ja_entraram = []

acesso_liberado = 0
duplicado = 0
nao_autorizado = 0

for i in range(m_tentativas):
    tentativa = input('tentativa de acesso: ')
    if tentativa not in lista_autorizados:
        print('nao autorizado')
        nao_autorizado += 1

    elif tentativa in lista_autorizados:
        print('duplicado.')
        duplicado += 1

    else:
        print('acesso liberado')
        lista_ja_entraram. append(tentativa)
        acesso_liberado += 1

cont_nao_entraram = 0
for codigo in lista_autorizados:
    if codigo not in lista_ja_entraram:
        cont_nao_entraram += 1

print("\n--- Relatório Final ---")
print(f"Participantes que conseguiram entrar: {acesso_liberado}")
print(f"Tentativas duplicadas: {duplicado}")
print(f"Tentativas com códigos não autorizados: {nao_autorizado}")
print(f"Participantes autorizados que ainda não entraram: {cont_nao_entraram}")

