# SRI-Modelo-Vectorial-Generalizado

## Integrantes

- Carlos Arturo Pérez Cabrera
- Diana Laura Pérez Tujillo

## Definición del modelo de SRI implementado

Para el desarrollo del proyecto se ha implementado el Modelo Vectorial Generalizado (GVM).
El Modelo Vectorial Generalizado (GVM) es una extensión del Modelo Vectorial clásico utilizado en recuperación de información. Este modelo busca representar documentos y consultas en un espacio vectorial, donde cada término o concepto se asocia con un vector. A diferencia del Modelo Vectorial clásico, el Modelo Vectorial Generalizado permite la representación de relaciones más complejas entre los términos y los documentos.Además de considerar la frecuencia de los términos en los documentos, se pueden incluir otros factores como la importancia de los términos en el contexto del documento, la relevancia de los términos en relación con la consulta y la correlación entre los términos.

## Consideraciones tomadas a la hora de desarrollar la solución

La solución ha sido implementada pensando en un corpus en el idioma inglés, asumiendo también que la consulta ingresada por el usuario se encontrará en ese idioma. El procesamiento del corpus es muy costoso temporalmente, por lo que se realiza un preprocesamiento previo del mismo, facilitando así el trabajo a la hora de procesar las consultas del usuario, dicho corpus así como otros datos de interés del algoritmo se guardan en un fichero .json.

## Explicación de como ejecutar el proyecto.Definición de la consulta

## Explicación de la solución desarrollada

La solución desarrollada resulta la implementación del Modelo Vectorial Generalizado (MVG), que define una función de similitud entre un documento y una consulta dados. Esta similitud se basa en la Similitud del Coseno, utilizada en el Modelo Vectorial estándar, sin embargo entra en en la fórmula un nuevo factor, el factor de correlación entre dos términos i,j. A continuación se definen estos conceptos, así como su significancia en la solución propuesta. 

### Similitud del coseno

La similitud del coseno es una medida utilizada para calcular cuánto se parecen dos vectores de características. Se basa en el ángulo entre los vectores en un espacio n-dimensional. Cuanto más cerca estén los vectores, mayor será su similitud del coseno.

### Factor de Correlación

Un factor de correlación entre dos términos i y j es una medida que indica la relación o asociación entre ellos en un conjunto de documentos. Puede ser calculado utilizando diversas técnicas estadísticas, específicamente en la solución propuesta se ha utilizado el coeficiente de correlación de Phi, debido a que los vectores representativos de los términos i,j son vectores discretos binarios. Este coeficiente mide la relación lineal entre los valores de dos variables y varía entre -1 y 1.  

### Modelo Vectorial Generalizado

Como se ha mencionado, el Modelo Vectorial Generalizado (MVG) se basa en el cálculo de la similitud del coseno, tomando en cuenta el factor de correlación entre un par de términos. La fórmula en la que se ha basado la implementación de la solución es la siguiente:

$sim(d_{k}, q) = \frac{\sum_{j=1}^{n}\sum_{i=1}^{n}w_{i,k} \cdot w_{j,q} \cdot t_{i} \cdot t_{j}}{\sqrt{\sum_{i=1}^{n}w_{i,k}^{2}} \cdot \sqrt{\sum_{i=1}^{n}w_{i,q}^{2}}}$

Donde:

- $w_{i,k}$ representa el peso del término i en el documento k.
- $w_{j,q}$ representa el peso del término j en la consulta q.
- $t_{i} \cdot t_{j}$ representa el factor de correlación entre el término i y el término j.

## Insuficiencias de la solución  y mejoras propuestas

- En la implemenatación del Método Booleano, se presentan dificultades ante consultas que se traduzcan de la forma 'A & B' a la Forma Normal Disyuntiva. Esto se debe a que la función implementada en Python que convierte una expresión lógica a Forma Normal Disyuntiva, no tiene en cuenta la posibilidad de aparición de este tipo de consultas. Como mejora se propone la implementación manual de una función que transforme correctamente todo tipo de expresiones lógicas a Forma Normal Disyuntiva.
- En el trabajo con la biblioteca 'spacy' a veces se encuentran dificultades en el etiquetado de palabras y en el proceso de Reducción Morfológica.  
- En general, la implementación del Modelo Vectorial Generalizado resulta costosa computacionalmente. Se logró refactorizar el código de determinadas funciones, pero se recomienda realizar un análisis en otras funciones matemáticas que pudieran aligerar el costo temporal del algoritmo.
  