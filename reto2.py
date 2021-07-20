P=input()
N= input()
nombres=input()


def calcular_resultado(sj1: int, sj2: int, ij1: str, ij2: str):
    letra = "I"
    if sj1 > sj2:
        letra = ij1
    elif sj2 > sj1:
        letra = ij2
    return letra

def main():
    contador = 0;
    i = 0;
    output = ""
    score_j1 = 0
    score_j2 = 0
    p_trasformed = "P"
    n_trasformed = "N"
    for i in nombres:
        if i in P :           
            score_j1 += 1
        if i in N:
           score_j2 += 1
        resultado = calcular_resultado(score_j1, score_j2,p_trasformed, n_trasformed)
        word = str(resultado)
        output += word               
    return output
print(main())


