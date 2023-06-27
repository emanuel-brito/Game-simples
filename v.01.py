import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Meu Jogo")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Posição inicial do jogador
posicao_jogador_x = largura_tela // 2
posicao_jogador_y = altura_tela - 50

# Tamanho e velocidade do jogador
tamanho_jogador = 50
velocidade_jogador = 5

# Posição inicial do inimigo
posicao_inimigo_x = random.randint(0, largura_tela - tamanho_jogador)
posicao_inimigo_y = 0

# Tamanho e velocidade do inimigo
tamanho_inimigo = 50
velocidade_inimigo = 3

# Contador de pontos
pontos = 0

# Fonte de texto
fonte = pygame.font.SysFont(None, 36)

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and posicao_jogador_x > 0:
        posicao_jogador_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and posicao_jogador_x < largura_tela - tamanho_jogador:
        posicao_jogador_x += velocidade_jogador

    # Movimentação do inimigo
    posicao_inimigo_y += velocidade_inimigo
    if posicao_inimigo_y > altura_tela:
        posicao_inimigo_x = random.randint(0, largura_tela - tamanho_jogador)
        posicao_inimigo_y = 0
        pontos += 1

    # Colisão entre jogador e inimigo
    if posicao_jogador_x < posicao_inimigo_x + tamanho_inimigo and \
            posicao_jogador_x + tamanho_jogador > posicao_inimigo_x and \
            posicao_jogador_y < posicao_inimigo_y + tamanho_inimigo and \
            posicao_jogador_y + tamanho_jogador > posicao_inimigo_y:
        rodando = False

    # Pintando a tela
    tela.fill(BRANCO)
    pygame.draw.rect(tela, VERMELHO, (posicao_jogador_x, posicao_jogador_y, tamanho_jogador, tamanho_jogador))
    pygame.draw.rect(tela, VERMELHO, (posicao_inimigo_x, posicao_inimigo_y, tamanho_inimigo, tamanho_inimigo))

    # Exibindo a pontuação na tela
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, VERMELHO)
    tela.blit(texto_pontos, (10, 10))

    pygame.display.update()

# Tela de game over
tela.fill(BRANCO)
texto_game_over = fonte.render("Game Over", True, VERMELHO)
texto_pontuacao = fonte.render(f"Pontuação final:{pontos}", True, VERMELHO)
texto_reiniciar = fonte.render("Pressione R para jogar novamente", True, VERMELHO)
tela.blit(texto_game_over, (largura_tela // 2 - 100, altura_tela // 2 - 50))
tela.blit(texto_pontuacao, (largura_tela // 2 - 100, altura_tela // 2))
tela.blit(texto_reiniciar, (largura_tela // 2 - 150, altura_tela // 2 + 50))
pygame.display.update()

reiniciar = False
while not reiniciar:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reiniciar = True

# Encerrando o Pygame
pygame.quit()