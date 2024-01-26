Instituto de Investigaciones en Inteligencia Artificial - Universidad Veracruzana

**Probabilidad**

**Tarea 8**

**Ajuste de Modelo GMM Gaussian Mixture Model**

Dado un conjunto de I=30 puntos generados muestreando aleatoriamente 2 gaussianas unidimensionales μ1=4 σ1=3, μ2=12 σ2=3.5. Muestrear 15 de la Gaussiana 1 y 15 puntos de la Gaussiana 2. Iterar el algoritmo para encontrar los parámetros óptimos para el conjunto de entrenamiento. Se proporciona k=2.

Para realizar este trabajo, se hace uso de las siguientes formulas:

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.001.png)

Calculo de la probabilidad para la multigaussiana

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.002.png)

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.003.png)

Calculo de parámetros para la siguiente iteración

En la primera iteración los valores de μ, σ y λ para las dos k empiezan de manera aleatoria y con cada iteración se van entrenando de acuerdo a los 30 puntos que se generaron de las dos gaussianas dadas.



**Resultados:**

Al correr el código, debido a que los valores de las μ y σ son aleatorios, cuando las sigmas son grandes y sus valores de mu son muy cercanos es posible que ambos μ y σ terminen teniendo valores similares, y en ver de verse como dos gaussianas unidas termina pareciendo una sola:

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.004.png)

Otro caso es donde los valores si tienen cierta separación y se aprecia de mejor manera como las gaussianas se dividen y como la multigaussiana toma forma similar a las dos gaussianas juntas:

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.005.png)

El siguiente caso se puede ver como a pesar de que μ2 empieza siendo mas chico que μ1, uno pensaria que la guassiana 1, de color azul, seria la que se moveria al lado derecho para aprender los valores de ese lado, sin embargo aquí es donde juega un factor importante los σ, ya que σ1=2 y σ2=11, por lo que al ser  σ2 el valor mas grande es el que termina haciendo que la gaussiana verde se mueva a la derecha y sea la que mas probabilidad tenga para esos datos.

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.006.png)

El siguiente caso es donde las μ empiezan separadas y tienen σ con valores menores a 5, lo cual hace que el entrenamiento, tome la forma ideal, donde es fácilmente distinguible cada gaussiana y se puede apreciar como la multigaussiana toma forma similar a las dos gaussianas.

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.007.png)

Finalmente el ultimo caso es cuando aumentamos el numero de puntos aleatorios generados al inicio de 15 por gaussiana a 30 para cada una, dando 60 puntos en total, para obtener las siguientes graficas:

![](Aspose.Words.9fa96c72-9a7e-47d3-aa19-91d17120e70a.008.png)

**Conclusión:**

En conclusión se puede ver que el modelo si es capaz de aprender de manera adecuada los puntos generados y obtener una multigaussiana para estos datos, sin embargo al ser aleatorios los μ, σ y λ es posible que aprendan de diferente manera en cada corrida, lo cual se puede mejorar limitando la aleatorización de estos valores de acuerdo al tipo de problema que se quiere resolver.
Métodos probabilísticos para la Inteligencia Artificial
