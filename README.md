# Relatório de Resultados

## Equipe:
- **Nome da Equipe:** Ana Carolina Rocha, Gabriel Colonetti e Luiz Henrique de Oliveira.

## Descrição do Algoritmo

Este algoritmo utiliza o **Algoritmo Genético** (GA) para resolver o problema da **Mochila**. O objetivo é selecionar itens de uma lista, levando em consideração seus **pesos** e **valores**, de modo a maximizar o valor total sem ultrapassar a capacidade total da mochila.

O algoritmo segue os seguintes passos principais:

1. **Criação de Indivíduos:** A população inicial é gerada aleatoriamente, onde cada indivíduo é representado por uma lista de 0s e 1s. Cada posição indica se o item correspondente está ou não na mochila.
2. **Avaliação da Aptidão:** Para cada indivíduo, é calculado o valor total dos itens na mochila e o peso total. O valor total é considerado apenas se o peso não ultrapassar a capacidade máxima da mochila.
3. **Seleção:** Os dois melhores indivíduos (com maior valor) são selecionados para reprodução. A seleção é feita através de torneios, onde indivíduos competem entre si.
4. **Cruzamento:** A reprodução ocorre por meio de um ponto de cruzamento, gerando dois filhos.
5. **Mutação:** Cada filho pode sofrer mutação, com base em uma taxa de mutação especificada.
6. **Substituição:** A população é substituída pelos filhos gerados, e o processo se repete por várias gerações. A técnica de **elitismo** foi incorporada para preservar os melhores indivíduos de cada geração.

## Exemplos de Entrada/Saída

### Exemplo 1: Teste Pequeno

**Entradas:**
- Pesos: [2, 3, 4, 5]
- Valores: [3, 4, 5, 6]
- Capacidade da mochila: 5

**Saída:**
- Melhor valor encontrado: 9
- Peso total: 14
- Tempo de execução: 0.06 segundos

### Exemplo 2: Teste Médio

**Entradas:**
- Pesos: valores aleatórios gerados
- Valores: valores aleatórios gerados
- Capacidade da mochila: 1000

**Saída:**
- Melhor valor encontrado: 31495
- Peso total: 6005
- Tempo de execução: 15.53 segundos

### Exemplo 3: Teste Grande

**Entradas:**
- Pesos: valores aleatórios gerados
- Valores: valores aleatórios gerados
- Capacidade da mochila: 10000

**Saída:**
- Melhor valor encontrado: 264640
- Peso total: 52907
- Tempo de execução: 343.57 segundos

## Dificuldades e Aprendizados

Durante o desenvolvimento do algoritmo, algumas dificuldades foram encontradas:

- **Desempenho em Testes Grandes:** O tempo de execução aumentou consideravelmente para o teste com um número muito grande de itens. Algumas alterações foram feitas para tentar otimizar o desempenho, como ajustar a capacidade da mochila e diminuir o tamanho da população e o número de gerações.
- **Seleção e Cruzamento:** A escolha do ponto de cruzamento e a forma como a seleção é feita impactaram diretamente os resultados. A seleção baseada em fitness foi eficiente, mas poderia ser aprimorada com técnicas mais sofisticadas.
- **Mutação:** A mutação teve um papel importante em explorar diferentes combinações, mas uma taxa muito alta pode levar a uma "exploração" excessiva do espaço de soluções, prejudicando a convergência do algoritmo.

Os principais aprendizados foram sobre a importância de ajustar os parâmetros do algoritmo genético, como o tamanho da população, a taxa de mutação e o número de gerações, para otimizar tanto o desempenho quanto os resultados. Além disso, o uso de **elitismo** ajudou a melhorar a qualidade das soluções encontradas ao longo das gerações.
