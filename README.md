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

## Insuficiencias de la solución  y mejoras propuestas

- En la implemenatación del Método Booleano, se presentan dificultades ante consultas que se traduzcan de la forma 'A & B' a la Forma Normal Disyuntiva. Esto se debe a que la función implementada en Python que convierte una expresión lógica a Forma Normal Disyuntiva, no tiene en cuenta la posibilidad de aparición de este tipo de consultas. Como mejora se propone la implementación manual de una función que transforme correctamente todo tipo de expresiones lógicas a Forma Normal Disyuntiva.
- En el trabajo con la biblioteca 'spacy' a veces se encuentran dificultades en el etiquetado de palabras y en el proceso de Reducción Morfológica. 
- En general, la implementación del Modelo Vectorial Generalizado resulta costosa computacionalmente. Se logró refactorizar el código de determinadas funciones, pero se recomienda realizar un análisis en otras funciones matemáticas que pudieran aligerar el costo temporal del algoritmo.