"""
Arquivo principal main.py - Controla a execução do jogo
"""

import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar, animar_vitoria
from aventura_pkg.utils import imprime_instrucoes, exibir_menu

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--dificuldade", type=int, default=5, help="Tamanho do labirinto")
    args = parser.parse_args()

    nome = args.name
    tamanho = args.dificuldade

    print(f"Bem-vindo(a), {nome}!")
    lab = criar_labirinto(tamanho)
    jogador = iniciar_jogador()

    while True:
        opcao = exibir_menu()
        match opcao:
            case "1":
                imprimir_labirinto(lab)
                direcao = input("Digite w/a/s/d para mover: ")
                mover(jogador, direcao, tamanho)
                pontuar(jogador)
                print(f"Posição: {jogador['pos']} | Pontos: {jogador['pontos']}")
            case "2":
                imprime_instrucoes()
            case "3":
                animar_vitoria(3)
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
