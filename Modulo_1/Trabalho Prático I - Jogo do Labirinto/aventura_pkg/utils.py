"""
Módulo utils
Funções utilitárias do jogo.
"""
from rich.console import Console
import time
console = Console()

def imprime_instrucoes():
    console.print("[bold cyan]Bem-vindo ao jogo Aventura no Labirinto![/bold cyan]")
    console.print("Use as teclas W A S D para se mover.")
    console.print("Evite paredes (#), alcance o X para vencer!")
    console.print("Boa sorte!\n")

def exibir_menu():
    console.print("1. Jogar")
    console.print("2. Instruções")
    console.print("3. Sair")
    return input("Escolha: ")

def animacao_vitoria_recursiva(contador=3):
    if contador == 0:
        console.print("[bold green]🎉 Vitória![/bold green]")
        return
    console.print(f"[bold yellow]🎊 Parabéns! {contador}[/bold yellow]")
    time.sleep(1)
    animacao_vitoria_recursiva(contador-1)
