"""
Módulo labirinto
Responsável por criar e imprimir o labirinto do jogo.
"""
import random

def criar_labirinto(tamanho=5):
    lab = [['.' for _ in range(tamanho)] for _ in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            if random.random() < 0.2 and (i, j) not in [(0, 0), (tamanho-1, tamanho-1)]:
                lab[i][j] = '#'
    lab[0][0] = 'P'
    lab[tamanho-1][tamanho-1] = 'X'
    return lab

def imprimir_labirinto(lab):
    for linha in lab:
        print(" ".join(linha))
