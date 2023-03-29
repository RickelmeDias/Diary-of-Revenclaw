#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

void aloca(double **p, int tam);
double f(double X, double *valoresDaEquacao, int tam);

int main() {

    int maiorGrau;

    double *valoresDaEquacao = NULL;
    double precisao, A, B;

    printf("Qual o maior grau da equação?\n");
    scanf("%d", &maiorGrau);

    aloca(&valoresDaEquacao, maiorGrau);

    for (int i=0; i<=maiorGrau+1; i++) {
        if (i==maiorGrau+1) {
            printf("Digite o valor do ultimo termo: \n");
            scanf("%lf", (valoresDaEquacao+i));
        } else {
            printf("Digite valor de X^%d: \n", i);
            scanf("%lf", (valoresDaEquacao+i));
        }
    }

    // Maior valor deve ser sempre o A, validar a ordem dos intervalors (valido: [1,2], não valido: [2,1])
    printf("Qual o valor de A do intervalo?\n");
    scanf("%lf", &A);

    printf("Qual o valor de B do intervalo?\n");
    scanf("%lf", &B);

    if (A > B) {
        printf("O valor de A não pode ser maior que B\n");
	printf("\n--------\n");
        exit(1);
    }

    printf("Qual a precisão?\n");
    scanf("%lf", &precisao);

    // double funcaoResultado = f(A, valoresDaEquacao, maiorGrau);

    bool temRaiz = f(A, valoresDaEquacao, maiorGrau) * f(B, valoresDaEquacao, maiorGrau) < 0;

    if (!temRaiz) {
        printf("Não tem raiz. Programa finalizado!");
        printf("\n--------\n");
        exit(1);
    }

    double M = 0;

    do {
        M = (A+B)/2;

        if (f(A, valoresDaEquacao, maiorGrau) * f(M, valoresDaEquacao, maiorGrau) < 0)
            B = M;
        else
            A = M;
    } while (fabs(f(M, valoresDaEquacao, maiorGrau)) >= precisao);

    printf("A raiz e %lf com erro de +/- %lf", M, fabs(f(M, valoresDaEquacao, maiorGrau)));

    printf("\n--------\n");

    return 0;
}

void aloca(double **p, int tam) {
    if (( *p=(double *)realloc(*p,tam*sizeof(double)) ) == NULL)
    {
        printf("Nao foi possivel alocar dados");
	printf("\n--------\n");

        exit(1);
    }
}

double f(double X, double *valoresDaEquacao, int tam) {
    double resultadoDaFuncao = 0.0;
    for (int i=0; i<=tam+1; i++) {
        if (*(valoresDaEquacao+i) != 0) {
            if (i==tam+1) {
                resultadoDaFuncao += *(valoresDaEquacao+i);
                // printf("%lf", *(valoresDaEquacao+i));
            } else {
                resultadoDaFuncao += *(valoresDaEquacao+i) * pow(X, i);
                // printf("X^%d * %lf\n", i, *(valoresDaEquacao+i));
            }
        }
    }
    return resultadoDaFuncao;
}
