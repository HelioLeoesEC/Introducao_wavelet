import matplotlib.pyplot as plt
import numpy as np
def coeficiente(amostragem,teta,jota):
    real = round(np.cos((2*np.pi*jota*teta)/amostragem),2)
    imaginario = round(np.sin((2*np.pi*jota*teta)/amostragem),2)
    return [real, imaginario]
def DFT(amostragem,x,d):
    if len(x) == len(d):
        d_chapeu = []
        for teta in range(len(x)):
            real = 0
            imaginaria = 0
            for j in range(len(x)):
                retorno = coeficiente(amostragem=amostragem,teta=teta,jota=j)
                real = real + d[j]* retorno[0]
                imaginaria = real + d[j]*retorno[1]
            d_chapeu.append([real,imaginaria])
    else:
        print("As matrizes não são iguais")
