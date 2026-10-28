lista_prog = []
lista_ia = []
lista_seg = []

qtd_alunos = int(input('digite a quantidade de alunos interessados nas oficinas: '))

for aluno in range(qtd_alunos):
    oficinas = input('qual oficina quer entrar: ')
    matricula = int(input("Digite a matrícula do aluno: "))

    if oficinas == lista_prog:
        lista_prog.append(matricula)

    elif oficinas == lista_ia:
        lista_ia.append(matricula)

    elif oficinas == lista_seg:
        lista_seg.append(matricula)

prog = set(lista_prog)
ia = set(lista_ia)
seg = set(lista_seg)

apenas_uma = (prog - ia - seg) | (ia - prog - seg) | (seg - prog - ia)
exatamente_duas = ((prog & ia) - seg) | ((prog & seg) - ia) | ((ia & seg) - prog)
tres_oficinas = prog & ia & seg
total_distintos = prog | ia | seg

print("Apenas uma:", sorted(list(apenas_uma)))
print("Exatamente duas:", sorted(list(exatamente_duas)))
print("Três oficinas:", sorted(list(tres_oficinas)))
print("Total de participantes distintos:", len(total_distintos))