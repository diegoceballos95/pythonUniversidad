import numpy as np    

mat = np.array([[1,2],[3,4]], dtype="int")

print(mat)
print("FILA 0")
print(mat[0][:].min())  #mínimo.
print(mat[0][:].max())  #máximo
print(mat[0][:].sum())  #suma.
print(mat[0][:].prod()) #producto
print(mat[0][:].mean()) #media

print("\nFILA 1")
print(mat[1][:].min())
print(mat[1][:].max())
print(mat[1][:].sum())
print(mat[1][:].prod())
print(mat[1][:].mean()) 

print("\nCOLUMNA 0")
print(mat[:][0].min())
print(mat[:][0].max())
print(mat[:][0].sum())
print(mat[:][0].prod())
print(mat[:][0].mean()) 

print("\nCOLUMNA 1")
print(mat[:][1].min())
print(mat[:][1].max())
print(mat[:][1].sum())
print(mat[:][1].prod())
print(mat[:][1].mean())

print("Mas funciones en: https://numpy.org/doc/stable/reference/routines.math.html ")

