## Fila (queue)



- Estrutura linear de dados que cresce somando elementos ao final ou diminuindo em sua frente.
  - Só pode tirar o primeiro elemento;
- Modelar situações onde é necessario que o primeiro elemento que entre seja o primeiro que saia
- FIFO (First In, First Out)



#### Casos

- Impressora: Lista de documentos para serem impressos em ordem de fila;
- Troca de mensagens entre computadores em uma rede;
- Gerenciamento de E/S em um disco;
  - Escalonamento de acessos



#### Metodos (operações)

- enqueue(x): insere elemento no final da fila;
- dequeue: remove o primeiro elemento da fila;
- isEmpty: retorna se a fila está vazia;
- isFull: retorna se a fila está cheia;
- front(): retorna o primeiro elemento da fila sem remover;
- size(): retorna o número de elementos;
- clear(): remove os elementos da fila.



#### Alocação estatica

- Pode-se usar array, ou uma lista de tamanho fixo;
- Adicionar (enqueue): incrementa o __rear__
- Remover (dequeue): decrementa o __front__



##### Complexidade das operações



A fila estatica tem o problema de que ao mudar o indice do __front__ , os valores anteriores que estão liberados na fila, ficam como valores que ainda nao foram removidos, ou seja, mover o indice front apenas não basta.



1. Uma das soluções utiliza e adiciona a complexidade O(n), que é puxar todos os valores para trás (movimentar todos para esquerda para que o primeiro elemento esteja sempre no indice zero).
2. Podemos usar a Alocação Estatica Circular, fazendo com que o rear aponte para a posição zero, pois ele sabe que está livre, já que o front não esta no indice zero mais.



#### Alocação dinâmica

- Normalmente usa-se __lista encadeada__;
- O tamanho não é fixo;
- Cada elemento (nó ou node) da fila deve contar um valor e referência para o próximo elemento.



##### Complexidade das operações



## Fila dupla (deque)

- Em alguns casos faz sentido remover elementos do começo e do fim da fila;
- Exemplo de implementação (fila de um restaurante):
  - A primeira pessoa da fila pode ser retirada da fila, mas quando for chamada não ter mesa disponivel, nesse caso a primeira pessoa da fila deve voltar para seu lugar (1);
  - A ultima pessoa pode ficar impaciente e sair da fila.
- Pode ser implementada estaticamente ou dinamicamente.



#### Metodos (operações)

- enqueueFront(x): insere elemento no final da fila;
- dequeueFront(): remove o primeiro elemento da fila;
- enqueueRear(x): insere elemento no final da fila;
- dequeueRear(): remove o primeiro elemento da fila;
- isEmpty(): retorna se a fila está vazia;
- isFull(): retorna se a fila está cheia;
- front(): retorna o primeiro elemento da fila sem remover;
- size(): retorna o número de elementos;
- clear(): remove os elementos da fila.

