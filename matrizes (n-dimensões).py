import numpy as np                             #----------------->  impotando a biblioteca do numpy

A = np.random.standard_normal(size=(800,800))  #----------------->  gerando uma matriz A de  800x800 (randômica)
B = A.astype(np.float32)                       #----------------->  tornando a matriz A em B para ficar no type = float32

print("\n")

print("-"*(70))                                #----------------->  'enfeite' para que apareça 70x o carácter '-'

print("MATRIZ 800x800".center(70))             #----------------->  printando o nome matriz e centralizando

print("-"*(70))

print(B)                                       #----------------->  printando a matriz B (convertida em float32)

print("-"*(70))

print ('\033[1m')                              #----------------->  'enfeite' para que as linhas fiquem coloridas

                    #   VERIFICAÇÃO DOS DADOS DA MATRIZ 800X800 - TYPE FLOAT32    #

print("TIPO DE DADOS:",B.dtype)                #----------------->  printando o tipo de dado da matriz gerada e convertida

print("VALOR MÁXIMO:",np.max(A))               #----------------->  printando o seu valor máximo

print("VALOR MÍNIMO:",np.min(A))               #----------------->  printando o seu valor mínimo

print("MÉDIA:",np.mean(A))                     #----------------->  printando a sua média

print("VARIÂNCIA:",np.var(A,ddof=1))           #----------------->  printando a sua variância




