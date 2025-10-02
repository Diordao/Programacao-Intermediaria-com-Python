"""
Módulo utils.py - Funções utilitárias
"""

from rich.console import Console
console = Console()

def imprime_instrucoes():
    """Lê e exibe as instruções do jogo"""
    with open("instrucoes.txt", "r") as f:
        conteudo = f.read()
    console.print(conteudo, style="bold cyan")

def exibir_menu():
    """Exibe o menu principal usando match-case"""
    console.print("[bold green]1.[/bold green] Jogar")
    console.print("[bold green]2.[/bold green] Instruções")
    console.print("[bold green]3.[/bold green] Sair")
    opcao = input("Escolha: ")
    return opcao
