🧭 Aventura no Labirinto



Jogo simples via terminal onde o jogador deve se mover dentro de um labirinto até alcançar a saída (representada por \*\*X\*\*), somando pontos a cada movimento.





🎯 Objetivo

Mover o personagem \*\*P\*\* até o \*\*X\*\*, evitando caminhos bloqueados, utilizando as teclas:

\- `w` → cima  

\- `a` → esquerda  

\- `s` → baixo  

\- `d` → direita  





⚙️ Como Executar no Ubuntu



1\. Criar e acessar a pasta:



mkdir aventura\_no\_labirinto

cd aventura\_no\_labirinto



2\. Criar e ativar ambiente virtual:



python3 -m venv venv

source venv/bin/activate



3\. Instalar dependências:



pip install rich pynput

pip freeze > requirements.txt



4\. Executar o jogo:



python3 main.py --name "SeuNome" --dificuldade 5





🧭 Menu Principal



1 → Jogar



2 → Instruções



3 → Sair





🏁 Vitória



O jogo termina automaticamente ao alcançar o X, exibindo uma animação de vitória.

Para sair a qualquer momento, use Ctrl + C.

