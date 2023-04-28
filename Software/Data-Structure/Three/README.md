# Arvores

- Tem uma raiz (A)
- Cada nó pode ter filhos (N filhos)
- (G) e (H) irmão ->
- (D) descende de C e C é ancestral de D;
- G e I descende do mesmo ancestral;
- Árovres são mais restringidas em relação aos grafos;

? Tem como implementar xadrez (matriz) em uma árvore onde cada jogada é um nó;

- Nós folhas não possuem filhos;
- Cada nó só possue um pai;
- (F) tem dois filhos então é grau 2;
- grau só conta os filhos;
- nós grau zzero -> nó folha
- de um nó ao outro só existe um unico caminho;
- profunidade de I (raiz até ele) 3;
- arvore de 1 nó -> profundidade 0;
- _se existe um caminho...._

## arvore binaria

- cada no pode ter no max. 2 filhos
- facilita a busca binaria
  - _arvore binaria de busca_
    - os filhos tem que ter uma ordem logica de inserção

? para balancear uma arvore requer um custo maior computacional para achar um elemento diferente para raiz.

- arvore nao balanceada tende a ter complexidade O(n)

* log2(7)=>2.807=>3 (passos para adicionar um elemento)
  ? o que acontece se tiver 8 elementros

* pre ordem utiliza menos memória que o uso de diversos nós com ponteiros

Exercicio

em ordem [2, 4, 6, 8, 12, 16]

pre ordem [12, 4, 2, 8, 6, 16]

pos ordem [2, 8, 4, 6, 16, 12] (Errei)

Exercicito 2

7 3 1 2 5 4

```
                    7
        3
1               5
    2       4
```
