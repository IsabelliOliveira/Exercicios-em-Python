#Elaborar um algoritmo que leia 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada.

N1 = float(input(" Digite a primeira nota \n "))
N2 = float(input(" Digite a segunda nota \n "))
N3 = float(input(" Digite a terceira nota \n "))

#mediaFinal = (N1 + N2 + N3) / 3
#print(" Media final é %0.2f" % (mediaFinal))

mediaPonderada = (2*N1 + 3*N2 + 5*N3) / (2+3+5)

print(" Media final Ponderada é", mediaPonderada)