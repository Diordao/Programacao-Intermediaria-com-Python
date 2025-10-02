"""
Módulo labirinto.py - Responsável por criar e exibir o labirinto
"""

def criar_labirinto(tamanho=5):
    """Cria um labirinto simples representado por uma matriz 2D"""
    lab = [["." for _ in range(tamanho)] for _ in range(tamanho)]
    lab[0][0] = "P"  # Posição inicial
    lab[-1][-1] = "X"  # Saída
    return lab

def imprimir_labirinto(labirinto):
    """Imprime o labirinto no terminal"""
    for linha in labirinto:
        print(" ".join(linha))
