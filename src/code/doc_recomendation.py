import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Recomendación usando filtrado colaborativo basado en usuarios #

# Datos de evaluaciones de usuarios
evaluations = np.array([
    [5, 4, 0, 0, 1],
    [1, 0, 5, 2, 0],
    [0, 0, 4, 0, 4],
    [0, 0, 2, 0, 0],
    [0, 3, 0, 4, 0],
    [1, 0, 0, 5, 0],
])

# Usuario al que se le quiere hacer recomendaciones
user = np.array([0, 0, 5, 0, 0])

# Cálculo de la similitud coseno entre el usuario actual y todos los usuarios
sim = cosine_similarity([user], evaluations)[0]

# Obtener los índices de los N usuarios más similares al usuario actual
N = 3
sim_user_index = np.argsort(sim)[-N:][::-1]

# Calcular el factor de normalización k
k = 1 / np.sum(np.abs(sim[sim_user_index])) if np.sum(np.abs(sim[sim_user_index])) != 0 else 0

# Calcular la predicción para el usuario actual usando la fórmula de agregación

sum_sim=[]
for i in range(len(evaluations[1])):
    sum=0
    for j in range(len(evaluations[0])):
        eval=evaluations[j][i]
        simi=sim[j]
        sum=sum+eval*simi
    sum_sim.append(sum)

for i in range(len(evaluations[0])):
    sum_sim[i]=sum_sim[i]*k

# Eliminar las entidades que el usuario ya ha evaluado
for i in range(len(user)):
    if user[i]!=0:
        sum_sim[i]=0

print("Predicción de evaluaciones para el usuario actual:", sum_sim)