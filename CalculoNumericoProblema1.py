print ("Relatorio de Calculo Numerico - Problema 1 - Calculo das Voltagens dos nos da Rede Eletrica - Turma EE1")
print ("Alunas: \n Barbara Maria Oliveira Santos - DRE: 112046089 \n Isis Zaidan da Silva - DRE: 112017307 \n Monique Calmon de Carvalho Ferreira - DRE: 112036741  \n \n")
print ("Valores para teste do problema proposto:  R1=3[ohm], R2=15[ohm], R3=1[ohm], R4=3[ohm], R5=10[ohm], R6=2[ohm], R7=4[ohm], R8=3[ohm], R9=3[ohm], DDP=100V \n \n")


r1=input("Entre com a primeira resistencia (R1) [ohm]: ")
r2=input("Entre com a segunda resistencia (R2)[ohm]: ")
r3=input("Entre com a terceira resistencia (R3) [ohm]: ")
r4=input("Entre com a quarta resistencia (R4) [ohm]: ")
r5=input("Entre com a quinta resistencia (R5) [ohm]: ")
r6=input("Entre com a sexta resistencia (R6) [ohm]: ")
r7=input("Entre com a setima resistencia (R7) [ohm]: ")
r8=input("Entre com a oitava resistencia (R8) [ohm]: ")
r9=input("Entre com a nona resistencia (R9) [ohm]: ")

ddp=input("Entre com a DDP total do circuito[V]: ")

chute = input("De um chute inicial para os valores (entre como lista do tipo [xo,x1,x2]): ")
tolerancia = input("Qual e a tolerancia desejada?: ")
iteracoes = input("De o numero maximo de iteracoes desejado: ")


def entraMatriz():

    matriz=[[],[],[]]

    matriz[0].append(-1*(r1+r3+r2))
    matriz[0].append(r2)
    matriz[0].append(0)
    matriz[1].append(r2)
    matriz[1].append(-1*(r2+r4+r5+r6))
    matriz[1].append(r5)
    matriz[2].append(0)
    matriz[2].append(r5)
    matriz[2].append(-1*(r7+r8+r9+r5))

    return matriz

def vetorindep():

    vetorindep = []
    vetorindep.append(-1*ddp)
    vetorindep.append(0)
    vetorindep.append(0)
    
    return vetorindep

def ResolveGaussSeidel(matriz, vetorindep, chute, tolerancia, iteracoes):
    x=[]
    xanterior = []
    c = len(chute)
    iteracao = 0
    convergiu = False

    for i in range(0,c):
        x.append(chute[i])

    while convergiu == False:

        for i in range(0,c):
            xanterior.append(x[i])
        

        for i in range(0,c):
            soma = 0
            for j in range(0,c):
                if i != j:
                    soma = soma + matriz[i][j]*x[j]
            x[i] = (vetorindep[i] - soma)/float(matriz[i][i])
        iteracao = iteracao + 1
        
        for i in range(0,c):
            E = abs(x[i]-xanterior[i])
            if iteracao >= iteracoes or E <= tolerancia:
                convergiu = True
        
    return x


def calculaddps():

    matriz= entraMatriz()
    vetorind= vetorindep()
    correntes = ResolveGaussSeidel(matriz,vetorind,chute,tolerancia,iteracoes)
    v1=ddp-r1*correntes[0]
    v2=v1-r2*(correntes[0]-correntes[1])
    v3=v1-r4*correntes[1]
    v4=v3-r5*(correntes[1]-correntes[2])
    v5=v3-r7*correntes[2]
    v6=v5-r8*correntes[2]

    print 'Resposta: V1= ', v1,'V', '; V2= ', v3,'V', '; V3= ', v5,'V', '; V4= ',v6,'V', '; V5= ', v4,'V', '; V6= ', v2 ,'V'


while True:
    print calculaddps()
    fim=input("Digite 1 para sair do programa. ") 
    if fim==1:
        break
