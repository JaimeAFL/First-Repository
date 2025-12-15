import numpy as np

matriz = np.arange(2*3*4*5).reshape(2, 3, 4, 5)

if matriz.ndim == 4:
    print("La matriz tiene 4 dimensiones" )
else:
    print("La matriz no tiene 4 dimensiones")

print("ndim:", matriz.ndim)        
print("shape:", matriz.shape)        
print("contenido:\n", matriz)

S = matriz.sum(axis=(-2, -1))
print("shape S:", S.shape)
print("S:\n", S)
