"""Módulo layout: funções que organizam o texto usando rich.Layout e rule."""

from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.rule import Rule

console = Console()

def mostrar_layout(texto, isArquivo=False):
    """Cria um layout simples com header e body e coloca o texto no body."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body")
    )
    layout["header"].update(Text("CABEÇALHO", style="bold white on blue"))
    layout["body"].update(Text(texto))
    console.print(layout)

def mostrar_regra(texto, isArquivo=False):
    """Exibe uma 'rule' (linha separadora) antes do texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Rule(title="SEÇÃO"))
    console.print(texto)
    console.print(Rule())
