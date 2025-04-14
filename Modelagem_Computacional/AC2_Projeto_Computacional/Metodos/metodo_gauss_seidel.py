# metodo de gauss-seidel
import numpy as np

def matriz_to_ldr(matriz_a):
    A = np.array(matriz_a)
    # diagoanal
    L = np.diag(np.diag(A))
    # triangulo inferior sem a diagonal
    D = np.tril(A,k=-1)
    # triangulo superior sem a diagonal
    R = np.triu(A,k=1)
    return L,D,R

def soma_matriz(A,B):
    return A + B

def mult_matriz(A,B):
    return np.dot(A,B)

def inversa_matriz(A):
    det = np.linalg.det(A)
    if det != 0:
        return np.linalg.inv(A)
    print('matriz nao inversivel det=0')
    return None

def erro_normal_infinita(A,B):
    # ( ||A-B|| / ||A||)
    max_a = np.max(np.abs(A))
    delta = A - B
    max_delta = np.max(np.abs(delta))
    return max_delta / max_a
    

def metodo_gauss_seidel(matriz_A, matriz_x, matriz_b, erro_max=0.001, iter_max=100):
    X = np.array(matriz_x).reshape(-1,1)
    B = np.array(matriz_b).reshape(-1,1)
    L,D,R = matriz_to_ldr(matriz_A)
    
    soma = L + D
    inversa_LD = inversa_matriz(soma)
    if inversa_LD is None:
        return None

    for i in range(0, iter_max):
        temp_x = inversa_LD @ (B - R @ X)
        # verificar erro
        if erro_normal_infinita(temp_x,X) < erro_max:
            return temp_x,i
        X = temp_x 
    return X,i

