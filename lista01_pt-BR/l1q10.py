# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.
Apresentar os valores trocados.
'''

A = input("A: ")
B = input("B: ")

def swap(A, B):
    aux = A
    A = B
    B = aux

    print(f"A: {A}")
    print(f"B: {B}")
    
swap(A, B)