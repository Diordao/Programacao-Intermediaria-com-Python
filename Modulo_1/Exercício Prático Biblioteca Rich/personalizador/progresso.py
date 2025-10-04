"""Módulo progresso: funções que demonstram barras/indicadores de progresso."""

from rich.console import Console
from rich.progress import Progress, BarColumn, TimeElapsedColumn, SpinnerColumn
import time

console = Console()

def progresso_simulado(texto, isArquivo=False):
    """Mostra uma barra de progresso simulada e, no final, imprime o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    console.print("Iniciando tarefa simulada...")
    with Progress(SpinnerColumn(), "[progress.description]{task.description}", BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("Processando...", total=100)
        for i in range(100):
            time.sleep(0.01)  # simula trabalho
            progress.update(task, advance=1)
    console.print("Concluído!")
    console.print(texto)

def progresso_por_linhas(texto, isArquivo=False):
    """Lê arquivo (ou considera texto dividido por linhas) e faz progresso por linha."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    else:
        linhas = texto.splitlines() if isinstance(texto, str) else [str(texto)]

    total = max(1, len(linhas))
    with Progress("[progress.percentage]{task.percentage:>3.0f}%", BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("Processando linhas...", total=total)
        for ln in linhas:
            time.sleep(0.02)
            progress.update(task, advance=1)
    console.print("Linhas processadas:", total)
