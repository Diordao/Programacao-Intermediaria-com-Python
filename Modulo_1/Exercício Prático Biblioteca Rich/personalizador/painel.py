"""Módulo painel: funções que exibem texto usando rich.Panel."""

from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto, isArquivo=False):
    """Exibe o texto em um painel simples.
    texto: string ou caminho de arquivo se isArquivo True.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto, title="Painel Simples"))

def painel_destacado(texto, isArquivo=False):
    """Exibe o texto em painel com estilo/red border."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto, title="Painel Destacado", border_style="magenta", subtitle="personalizador"))
