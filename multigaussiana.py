import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math

mu1=2
sigma1=3
mu2=5
sigma2=3.5
k=2
puntos=15
rango=2*puntos
nums=np.array([])
numsy=np.array([])
lambdac1=random.random()
muc1=random.randint(0,10)
sigmac1=random.random()
lambdac2=1-lambdac1
muc2=random.randint(0,10)
sigmac2=random.random()
gmuc1=np.array([muc1])
gmuc2=np.array([muc2])
glambdac1=np.array([lambdac1])
glambdac2=np.array([lambdac2])
gsigmac1=np.array([sigmac1])
gsigmac2=np.array([sigmac2])
xiteracion=np.array([0])

#FUNCION PARA CALCULO DE LA NORMAL
def normal (x,mu,sigma):
    return np.exp(-1*((x-mu)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)

#CREACION DE PUNTOS ALEATORIOS BASADO EN DATOS DE GAUSSIANA
for i in range(puntos):
    x=random.gauss(mu1, sigma1)
    nums=np.append(nums,x)
    numsy=np.append(numsy,0)
    x=random.gauss(mu2, sigma2)
    nums=np.append(nums,x)
    numsy=np.append(numsy,0)
    
#CREACION DE FIGURAS CON MU Y SIGMA DADOS
plt.subplot(2,2,1)
plt.title("Gaussianas de valores dados")
x1=np.linspace(mu1-6*sigma1,mu1+6*sigma1,100)    
y1=normal(x1,mu1,sigma1)
x2=np.linspace(mu2-6*sigma2,mu2+6*sigma2,100)    
y2=normal(x2,mu2,sigma2)
plt.plot(x1,y1,'b')
plt.plot(x2,y2,'g')
plt.scatter(nums,numsy,color='k')
plt.xlim(-5,12)
plt.ylim(0,0.5)

#CREACION DE FIGURA CON MU Y SIGMA ALEATORIOS
plt.subplot(2,2,2)
plt.title("Gaussianas de valores aleatorios")
x1=np.linspace(muc1-6*sigmac1,muc1+6*sigmac1,100)    
y1=normal(x1,muc1,sigmac1)
x2=np.linspace(muc2-6*sigmac2,muc2+6*sigmac2,100)    
y2=normal(x2,muc2,sigmac2)
plt.plot(x1,y1,'b')
plt.plot(x2,y2,'g')
plt.scatter(nums,numsy,color='k')
plt.xlim(-5,12)
plt.ylim(0,0.5)

#INICIO DE ITERACIONES
for j in range(1,5):

    vrik1=np.zeros((rango))
    vrik2=np.zeros((rango))
    sumrik1=0
    sumrik2=0
    sumriks=0
    sumrik1x=0
    sumrik2x=0
    #CALCULO DE rik DE CADA PUNTO EN CADA K
    for i in range(rango):
        n1=lambdac1*normal(nums[i],muc1,sigmac1)
        n2=lambdac2*normal(nums[i],muc2,sigmac2)
        rik1=n1/(n1+n2)
        rik2=n2/(n1+n2)
        vrik1[i]=rik1
        vrik2[i]=rik2
        sumrik1=sumrik1+rik1
        sumrik2=sumrik2+rik2
        sumriks=sumriks+rik1+rik2
        sumrik1x=sumrik1x+(rik1*nums[i])
        sumrik2x=sumrik2x+(rik2*nums[i])

    #CALCULO DE NUEVOS LAMBDAS
    lambdac1old=lambdac1
    lambdac2old=lambdac2
    lambdac1=sumrik1/sumriks
    lambdac2=sumrik2/sumriks

    #CALCULO DE NUEVAS MUS
    muc1old=muc1
    muc2old=muc2
    muc1=sumrik1x/sumrik1
    muc2=sumrik2x/sumrik2


    sumrik1xmu=0
    sumrik2xmu=0
    #CALCULO DE NUEVAS SIGMAS
    for i in range(rango):
        sumrik1xmu=vrik1[i]*((nums[i]-muc1)**2)+sumrik1xmu
        sumrik2xmu=vrik2[i]*((nums[i]-muc2)**2)+sumrik2xmu

    sigmac1old=sigmac1
    sigmac2old=sigmac2
    sigmac1=sumrik1xmu/sumrik1
    sigmac2=sumrik2xmu/sumrik2

    gmuc1=np.append(gmuc1,muc1)
    gmuc2=np.append(gmuc2,muc2)
    glambdac1=np.append(glambdac1,lambdac1)
    glambdac2=np.append(glambdac2,lambdac2)
    gsigmac1=np.append(gsigmac1,sigmac1)
    gsigmac2=np.append(gsigmac2,sigmac2)
    xiteracion=np.append(xiteracion,j)

print(gmuc1)
print(xiteracion)

#CREACION DE FIGURA CON MU Y SIGMA ENTRENADOS
plt.subplot(2,2,3)
plt.title("Gaussianas de valores entrenados")
x1=np.linspace(muc1-6*sigmac1,muc1+6*sigmac1,100)    
y1=normal(x1,muc1,sigmac1)
x2=np.linspace(muc2-6*sigmac2,muc2+6*sigmac2,100)    
y2=normal(x2,muc2,sigmac2)
plt.plot(x1,y1,'b')
plt.plot(x2,y2,'g')
plt.scatter(nums,numsy,color='k')
plt.xlim(-5,12)
plt.ylim(0,0.5)

plt.subplot(2,2,4)
plt.title("Modificación de valores")

plt.plot(xiteracion,gmuc1,'b')

plt.plot(xiteracion,gmuc2,'g')
plt.legend("muk2")
plt.plot(xiteracion,glambdac1,'r')
plt.legend("lambdak1")
plt.plot(xiteracion,glambdac2,'c')
plt.plot(xiteracion,gsigmac1,'m')
plt.plot(xiteracion,gsigmac2,'y')
plt.legend('muk1','muk2')

plt.show()