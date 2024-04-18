# Importamos la biblioteca nuimpy y le ponemos el alias 'np'

import numpy as np

# Definimos una matriz cuadrada

matriz = np.array([[3,9],[5,8]])

# Calcularemos los valores propios
# Usaremos "np.linalg.eigvals" 
# np.linalg.eigvals es un función que calcula los valores propios de un arreglo

valores_propios = np.linalg.eigvals(matriz)

print(valores_propios)


# ¿Qué son los valores y vectores propios?
# ¿Cómo se utilizan en la ICG?

# GOOGLE_DOCS:
# https://docs.google.com/document/d/1zpyv_dVKjuiILnZJ4f0CD1Wd6DwwLTke5i5iQz_UCis/edit?usp=sharing