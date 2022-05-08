import matplotlib.pyplot as plt
import numpy as np
def coeficiente(amostragem,teta,jota):
    real = round(np.cos((2*np.pi*jota*teta)/amostragem),2)
    imaginario = (-1)*round(np.sin((2*np.pi*jota*teta)/amostragem),2)
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
                imaginaria = imaginaria + d[j]*retorno[1]
            d_chapeu.append([round(real,2),round(imaginaria,2)])
        magnitude = []
        fase = []
        for i in d_chapeu:
            magnitude.append(round(np.sqrt(i[0]**2 + i[1]**2),2))
        #Plotagem dos valores 
    else:
        print("As matrizes não são iguais")
x = np.arange(0,np.pi,0.3)
d = 1 + np.sin(x)

DFT(amostragem=len(x),x=x,d=d)