# Algoritmo Genético em Python

Este projeto implementa um algoritmo genético para resolver um problema de otimização. O objetivo é maximizar o valor total dos itens selecionados sem exceder o peso máximo permitido.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `random`, `numpy`

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/MarcosPauloA/oProblemaDaMochila
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd seu-repositorio
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install numpy
    ```

## Como Executar

1. Certifique-se de que você está no diretório do projeto.
2. Execute o script Python:
    ```bash
    python algoritmo_genetico.py
    ```

## Descrição do Código

### Funções Principais

- **fitness(cromossomo, pesos_e_valores, peso_maximo)**: Calcula o valor total e o peso total de um cromossomo. Retorna 0 se o peso total exceder o peso máximo.
- **criar_cromossomo(tamanho)**: Cria um cromossomo aleatório.
- **crossover(cromossomo1, cromossomo2)**: Realiza o crossover entre dois cromossomos.
- **mutacao(cromossomo, taxa_de_mutacao)**: Realiza a mutação em um cromossomo.
- **algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes, taxa_de_mutacao)**: Função principal que executa o algoritmo genético.

### Parâmetros de Entrada

- `pesos_e_valores`: Lista de listas onde cada sublista contém o peso e o valor de um item.
- `peso_maximo`: Peso máximo permitido para a seleção de itens.
- `numero_de_cromossomos`: Número de cromossomos na população.
- `geracoes`: Número de gerações para a execução do algoritmo.
- `taxa_de_mutacao`: Taxa de mutação aplicada aos cromossomos (padrão é 0.01).

### Exemplo de Execução

```python
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

resultado = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

for fitness, cromossomo in resultado:
    print(f"fitness: {fitness}, cromossomo: {cromossomo}")
