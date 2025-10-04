"""Módulo estilo: funções que exibem o texto com estilos (cores, ênfase)."""

from rich.console import Console
from rich.text import Text

console = Console()

def estilo_negrito(texto, isArquivo=False):
    """Exibe o texto em negrito e cor verde."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    t = Text(texto, style="bold green")
    console.print(t)

def estilo_colorido(texto, isArquivo=False):
    """Exibe o texto com destaque por palavra (exemplo simples)."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    # exemplo: imprime cada palavra com cor alternada
    parts = texto.split()
    styled = Text()
    colors = ["red", "yellow", "green", "cyan", "magenta"]
    for i, p in enumerate(parts):
        styled.append(p + " ", style=colors[i % len(colors)])
    console.print(styled)
