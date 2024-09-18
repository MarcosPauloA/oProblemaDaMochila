import random
import numpy as np

# Função para calcular o valor total e o peso total de um cromossomo
def fitness(cromossomo, pesos_e_valores, peso_maximo):
    valor_total = 0
    peso_total = 0
    for i in range(len(cromossomo)):
        if cromossomo[i] == 1:
            peso_total += pesos_e_valores[i][0]
            valor_total += pesos_e_valores[i][1]
    if peso_total > peso_maximo:
        return 0  # Penalidade por ultrapassar o peso máximo
    return valor_total

# Função para criar um cromossomo aleatório
def criar_cromossomo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

# Função para realizar o crossover entre dois cromossomos
def crossover(cromossomo1, cromossomo2):
    ponto_de_corte = random.randint(1, len(cromossomo1) - 1)
    filho1 = cromossomo1[:ponto_de_corte] + cromossomo2[ponto_de_corte:]
    filho2 = cromossomo2[:ponto_de_corte] + cromossomo1[ponto_de_corte:]
    return filho1, filho2

# Função para realizar a mutação em um cromossomo
def mutacao(cromossomo, taxa_de_mutacao):
    for i in range(len(cromossomo)):
        if random.random() < taxa_de_mutacao:
            cromossomo[i] = 1 - cromossomo[i]

# Função principal do algoritmo genético
def algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes, taxa_de_mutacao=0.01):
    tamanho_cromossomo = len(pesos_e_valores)
    populacao = [criar_cromossomo(tamanho_cromossomo) for _ in range(numero_de_cromossomos)]
    melhor_individuo_por_geracao = []

    for geracao in range(geracoes):
        populacao = sorted(populacao, key=lambda c: fitness(c, pesos_e_valores, peso_maximo), reverse=True)
        melhor_individuo = populacao[0]
        melhor_individuo_por_geracao.append((fitness(melhor_individuo, pesos_e_valores, peso_maximo), melhor_individuo))

        nova_populacao = populacao[:2]  # Elitismo: mantém os dois melhores indivíduos
        while len(nova_populacao) < numero_de_cromossomos:
            pai1, pai2 = random.choices(populacao[:50], k=2)  # Seleção por torneio
            filho1, filho2 = crossover(pai1, pai2)
            mutacao(filho1, taxa_de_mutacao)
            mutacao(filho2, taxa_de_mutacao)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao

    return melhor_individuo_por_geracao

# Parâmetros de entrada
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

# Executa o algoritmo genético
resultado = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

# Exibe o resultado
for fitness, cromossomo in resultado:
    print(f"Fitness: {fitness}, Cromossomo: {cromossomo}")
