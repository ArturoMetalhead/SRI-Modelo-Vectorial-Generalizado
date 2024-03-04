from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Definir los contenidos de los documentos
documentos = [
    "Este es el contenido del Documento1",
    "Aquí está el contenido del Documento2",
    "El contenido del Documento3 es diferente",
    "Este es el contenido del Documento4"
]

# Definir la matriz de preferencias de usuarios y documentos
usuarios = ['Usuario1', 'Usuario2', 'Usuario3', 'Usuario4']

matriz_preferencias = [
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4]
]

# Crear una matriz TF-IDF para los documentos
vectorizer = TfidfVectorizer()
matriz_tfidf = vectorizer.fit_transform(documentos)

# Función para calcular la similitud de contenido entre documentos
def calcular_similitud_contenido(documento1, documento2):
    documento1_tfidf = matriz_tfidf[documento1]
    documento2_tfidf = matriz_tfidf[documento2]
    similitud = cosine_similarity(documento1_tfidf, documento2_tfidf).flatten()[0]
    return similitud

# Función para calcular la similitud entre usuarios (distancia del coseno)
def calcular_similitud_usuario(usuario1, usuario2):
    preferencias_usuario1 = matriz_preferencias[usuario1]
    preferencias_usuario2 = matriz_preferencias[usuario2]
    similitud = cosine_similarity([preferencias_usuario1], [preferencias_usuario2]).flatten()[0]
    return similitud

# Función para obtener las recomendaciones para un usuario dado
def obtener_recomendaciones(usuario):
    similitudes_contenido = []
    similitudes_usuario = []
    for i in range(len(documentos)):
        if i != usuario:
            similitud_contenido = calcular_similitud_contenido(usuario, i)
            similitud_usuario = calcular_similitud_usuario(usuario, i)
            similitudes_contenido.append((i, similitud_contenido))
            similitudes_usuario.append((i, similitud_usuario))

    similitudes_contenido.sort(key=lambda x: x[1], reverse=True)
    similitudes_usuario.sort(key=lambda x: x[1], reverse=True)

    recomendaciones = []
    for i in range(len(documentos)):
        if i != usuario:
            puntaje = similitudes_contenido[i][1] + similitudes_usuario[i][1]
            recomendaciones.append((documentos[i], puntaje))

    recomendaciones.sort(key=lambda x: x[1], reverse=True)
    return recomendaciones

# Ejemplo de uso
usuario_ejemplo = 0
recomendaciones_usuario_ejemplo = obtener_recomendaciones(usuario_ejemplo)

print(f'Recomendaciones para {usuarios[usuario_ejemplo]}:')
for recomendacion in recomendaciones_usuario_ejemplo:
    print(f'{recomendacion[0]} - Puntaje: {recomendacion[1]}')