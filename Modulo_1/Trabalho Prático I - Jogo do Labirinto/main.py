"""
Main do jogo Aventura no Labirinto.
Contém CLI e controle do fluxo principal.
"""
import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar
from aventura_pkg.utils import imprime_instrucoes, exibir_menu, animacao_vitoria_recursiva


def jogar(tamanho):
    # Cria o labirinto com base no tamanho informado (nível de dificuldade)
    lab = criar_labirinto(tamanho)

    # Inicializa posição e pontuação do jogador
    posicao, pontos = iniciar_jogador()

    # Loop principal do jogo
    while True:
        imprimir_labirinto(lab)  # Mostra o labirinto na tela

        # Recebe o movimento do jogador
        direcao = input("Digite w/a/s/d para mover: ")

        # Calcula nova posição de acordo com a direção
        nova_pos = mover(lab, posicao, direcao)

        # Verifica se o destino é a saída (X)
        if lab[nova_pos[0]][nova_pos[1]] == 'X':
            posicao = nova_pos
            pontos = pontuar(pontos)
            imprimir_labirinto(lab)
            animacao_vitoria_recursiva()
            break  # Sai do laço do jogo (vitória!)

        # Se o jogador realmente se moveu, atualiza posição e pontuação
        if nova_pos != posicao:
            lab[posicao[0]][posicao[1]] = '.'  # Marca posição antiga como caminho livre
            posicao = nova_pos  # Atualiza a posição
            lab[posicao[0]][posicao[1]] = 'P'  # Coloca o jogador na nova posição
            pontos = pontuar(pontos)  # Atualiza pontuação

        print(f"Posição: {posicao} | Pontos: {pontos}")  # Mostra status atual


def main():
    # Cria o parser da linha de comando (CLI)
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")

    # Argumentos da CLI
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--dificuldade", type=int, default=5, help="Tamanho do labirinto")
    args = parser.parse_args()

    # Saudação inicial
    print(f"Bem-vindo(a), {args.name}!")

    # Menu principal
    while True:
        opcao = exibir_menu()
        match opcao:
            case '1': 
                jogar(args.dificuldade)  # Inicia o jogo
            case '2': 
                imprime_instrucoes()  # Exibe as instruções
            case '3': 
                animacao_vitoria_recursiva()  # Mensagem final (sair)
                break
            case _: 
                print("Opção inválida!")


# Executa o main apenas se este arquivo for o principal
if __name__ == "__main__":
    main()