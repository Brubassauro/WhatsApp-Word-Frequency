import matplotlib.pyplot as plt
import numpy as np

def Data(Str, Bin):

    try: A = int(Str[:2])
    except: return 'fewqdef'

    if Bin == 'm': return Str[len(Str)-4:] + Str[2:][:3]

    if A <= 15: return Str[len(Str)-4:] + Str[2:][:3] + '/1º'
    else: return Str[len(Str)-4:] + Str[2:][:3] + '/2º'

def Find(Palavra, Conv, Bin = 'm', Print = 'n'):

    arq = open('Conversas/' + Conv, 'r', encoding="utf8")

    X = [0]
    Y = [0]

    cDia = 0

    for line in arq:

        if X[cDia] != Data(line[:10], Bin):
            if '/2020' in line[:10] or '/2021' in line[:10]:
                X += [Data(line[:10], Bin)]
                Y += [0]
                cDia += 1

        for j in range(len(Palavra)):
            if Palavra[j].lower() in line.lower():
                Y[cDia] += 1
                if Print == 's': print(line)

    X.pop(0)
    Y.pop(0)

    plt.bar(X,Y,zorder=2)
    plt.xticks(rotation=45)
    Name = Palavra[0].replace(' ','').replace('-','').replace(':','')
    plt.title('Palavra "%s" no Grupo "%s". Total: %s' %(Name,Conv[:len(Conv)-4],sum(Y)))
    plt.xlabel('Mês')
    plt.ylabel('Nº de falas')
    plt.grid(zorder=1)
    plt.savefig('Histogramas/' + Conv[:len(Conv) - 4] + '_' + Name[:4] + '_Data.png', dpi = 300)
    plt.show()

    arq.close()

def Hora(Palavra, Conv, Print = 'n'):
    arq = open('Conversas/' + Conv,'r',encoding="utf8")

    X = [int(i) for i in range(24)]
    Y = [0 for i in range(24)]

    for line in arq:
        for j in range(len(Palavra)):
            if Palavra[j].lower() in line.lower():
                try: Y[int(line[11:][:2])] += 1
                except: continue
                if Print == 's': print(line)

    plt.bar(X,Y,zorder=2)
    Name = Palavra[0].replace(' ','').replace('-','').replace(':','')
    plt.title('Palavra "%s" no Grupo "%s". Total: %s' %(Name,Conv[:len(Conv)-4],sum(Y)))
    plt.xticks(np.arange(min(X), max(X), 2))
    plt.xlabel('Hora')
    plt.ylabel('Nº de falas')
    plt.grid(zorder=1)
    Name = Palavra[0].replace(' ','').replace('-','')
    plt.savefig('Histogramas/' + Conv[:len(Conv) - 4] + '_' + Name[:4] + '_Hora.png', dpi = 300)
    plt.show()

    arq.close()

Hora(['Vasco','vascão','vascao','vaxco'],'CDB.txt')

Find(['Vasco','vascão','vascao','vaxco'],'CDB.txt')