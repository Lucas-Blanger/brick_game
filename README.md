# Jogo Brick Breaker em Python com Pygame

# Descrição

Este projeto é uma implementação do clássico jogo Brick Breaker desenvolvida em Python utilizando a biblioteca Pygame. O objetivo do jogo é quebrar todos os blocos na tela usando uma bola, controlada por uma plataforma que o jogador pode mover horizontalmente. O jogador perde uma vida se a bola cair abaixo da plataforma e ganha ao destruir todos os blocos.
Funcionalidades

  Movimentação da Plataforma: O jogador controla uma plataforma horizontalmente para rebater a bola.
  Bola com Física de Colisão: A bola se move constantemente e rebate nas bordas da tela, nos blocos e na plataforma.
  Blocos Destrutíveis: Cada bloco é destruído ao ser atingido pela bola.
  Sistema de Pontuação: A pontuação aumenta à medida que os blocos são destruídos.
  Múltiplas Vidas: O jogador começa com um número de vidas e perde uma vida cada vez que a bola cai abaixo da plataforma.

# Requisitos

  Python 3.x
  Biblioteca Pygame: Pode ser instalada com o seguinte comando:

    bash

    pip install pygame

# Como Executar o Jogo

  Certifique-se de ter o Python e o Pygame instalados.
  Clone o repositório ou baixe os arquivos do projeto.
  Abra o terminal na pasta do projeto e execute o seguinte comando:

    bash

    python brick_game.py

   O jogo abrirá em uma janela Pygame, onde você poderá controlar a plataforma com as teclas de seta ou as teclas A e D.

# Controles

  Seta Esquerda / A: Move a plataforma para a esquerda.
  Seta Direita / D: Move a plataforma para a direita.
  Tecla Esc: Pausa o jogo ou fecha a janela.

# Estrutura do Projeto

  brick_game.py: Arquivo principal contendo a lógica do jogo.
  README.md: Documento com as instruções sobre o projeto.

# Regras do Jogo

  Controle a plataforma para impedir que a bola caia.
  Rebata a bola para quebrar os blocos na parte superior da tela.
  O jogo termina quando todas as vidas se esgotam ou quando todos os blocos são destruídos.

# Autores

    Nome do(a) desenvolvedor(a): Lucas Blanger

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
