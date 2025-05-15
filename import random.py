import random

# Representação do ambiente
# W = Parede, . = Comida, G = Fantasma, P = Pacman, ' ' = espaço vazio
grade = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', '.', ' ', 'G', 'W'],
    ['W', '.', 'P', '.', 'W'],
    ['W', '.', '.', '.', 'W'],
    ['W', 'W', 'W', 'W', 'W']
]

# Direções possíveis
direcoes = {
    'CIMA': (-1, 0),
    'BAIXO': (1, 0),
    'ESQUERDA': (0, -1),
    'DIREITA': (0, 1)
}

# Encontrar a posição atual do Pacman
def encontrar_pacman(grade):
    for i, linha in enumerate(grade):
        for j, celula in enumerate(linha):
            if celula == 'P':
                return i, j
    return None

# Verificar se a posição é válida e não tem parede
def e_valida(pos):
    i, j = pos
    return grade[i][j] != 'W'

# Verifica se há um fantasma ao redor
def ha_fantasma_proximo(pos):
    i, j = pos
    for di, dj in direcoes.values():
        ni, nj = i + di, j + dj
        if grade[ni][nj] == 'G':
            return True
    return False

# Regras do Agente Lógico
def decidir_movimento(pos):
    i, j = pos

    # Regra 1: Evitar fantasma
    for nome_direcao, (di, dj) in direcoes.items():
        ni, nj = i + di, j + dj
        if grade[ni][nj] != 'W' and grade[ni][nj] != 'G':
            if not ha_fantasma_proximo((ni, nj)):
                return nome_direcao  # Movimento seguro

    # Regra 2: Ir em direção à comida
    for nome_direcao, (di, dj) in direcoes.items():
        ni, nj = i + di, j + dj
        if grade[ni][nj] == '.':
            return nome_direcao

    # Regra 3: Movimento aleatório se não houver ameaça ou comida próxima
    movimentos_validos = []
    for nome_direcao, (di, dj) in direcoes.items():
        ni, nj = i + di, j + dj
        if e_valida((ni, nj)):
            movimentos_validos.append(nome_direcao)
    
    if movimentos_validos:
        return random.choice(movimentos_validos)
    
    return 'FICAR'

# Execução
pos_pacman = encontrar_pacman(grade)
proximo_movimento = decidir_movimento(pos_pacman)
print("Pac-Man deve se mover para:", proximo_movimento)
