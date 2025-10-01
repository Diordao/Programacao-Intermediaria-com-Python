#!/usr/bin/env python3
"""
main.py - interface CLI para o pacote 'personalizador'
Uso: python main.py "texto ou arquivo" -m painel -f 1 [-a]
"""

import argparse
from personalizador import painel, layout, progresso, estilo

# Mapas: id->module_name e module_name->objeto módulo
mod_id_to_name = {"1": "painel", "2": "layout", "3": "progresso", "4": "estilo"}
mod_name_to_module = {"painel": painel, "layout": layout, "progresso": progresso, "estilo": estilo}

# Funções disponíveis por módulo (id -> função) e nome -> função
func_defs = {
    "painel": {"1": painel.painel_simples, "2": painel.painel_destacado,
               "painel_simples": painel.painel_simples, "painel_destacado": painel.painel_destacado},
    "layout": {"1": layout.mostrar_layout, "2": layout.mostrar_regra,
               "mostrar_layout": layout.mostrar_layout, "mostrar_regra": layout.mostrar_regra},
    "progresso": {"1": progresso.progresso_simulado, "2": progresso.progresso_por_linhas,
                  "progresso_simulado": progresso.progresso_simulado, "progresso_por_linhas": progresso.progresso_por_linhas},
    "estilo": {"1": estilo.estilo_negrito, "2": estilo.estilo_colorido,
               "estilo_negrito": estilo.estilo_negrito, "estilo_colorido": estilo.estilo_colorido}
}

def listar_opcoes():
    """Retorna string curta mostrando módulos e funções (para uso no help)."""
    s = []
    for mid, mname in mod_id_to_name.items():
        s.append(f"{mid}:{mname}")
        fns = [k for k in func_defs[mname].keys() if not k.isalpha() or k[0].isdigit()]  # pega ids
        s.append("  funcoes: " + ", ".join(sorted(k for k in func_defs[mname].keys() if not k.isalpha())))
    return "\n".join(s)

def main():
    parser = argparse.ArgumentParser(
        description="Personalizador - formata texto com rich. Módulos/funções disponíveis:\n" + listar_opcoes(),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("texto", help="texto ou caminho de arquivo (dependendo de -a)")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indicar que 'texto' é um arquivo (leitura utf-8)")
    parser.add_argument("-m", "--modulo", required=True, help="Módulo (id ou nome). Ex.: 1 ou painel")
    parser.add_argument("-f", "--funcao", required=True, help="Função (id ou nome) do módulo. Ex.: 1 ou painel_simples")

    args = parser.parse_args()

    # descobrir nome do módulo
    mod_arg = args.modulo
    if mod_arg in mod_id_to_name:
        mod_name = mod_id_to_name[mod_arg]
    else:
        mod_name = mod_arg

    if mod_name not in mod_name_to_module:
        print("Módulo inválido. Opções:", ", ".join(mod_name_to_module.keys()))
        return

    # descobrir função
    f_map = func_defs[mod_name]
    func_key = args.funcao
    if func_key not in f_map:
        print("Função inválida para o módulo", mod_name)
        print("Opções:", ", ".join(k for k in f_map.keys() if not k.isalpha()))
        return

    func = f_map[func_key]
    # chamar
    func(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
