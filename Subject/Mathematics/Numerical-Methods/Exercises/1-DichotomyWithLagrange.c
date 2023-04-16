#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// Controle de alocação e memória
void aloca(double **p, int tam);

// Dicotomia
void dichotomy(double *valoresDaEquacao, int maiorGrau);
void calculateDichotomy(double *valoresDaEquacao, int maiorGrau);
double f(double X, double *valoresDaEquacao, int tam);

// Forma de Lagrange
void lagrange(double *xis, double *fxis, double *L, int qXis);
void showTable(double *xis, double *fxis, int qXis);
void interoplation(double *xis, double *fxis, double *L, int qXis);

int main() {
    // Dicotomia
    double *valoresDaEquacao = NULL;
    // Lagrange
    double *xis = NULL;
    double *fxis = NULL;
    double *L = NULL;
    
    int maiorGrau=0; int qXis=0;
    
    int opt=0;
    
    do {
        printf("\n===================================================");
        printf("\n\nVoce deseja executar qual metodo de calculo numerico?\n[1] FORMA DE LAGRANGE\n[2] METODO DICOTOMIA\n[0] SAIR\n");
        printf("\nDigite numero da opção:\n");
        scanf("%d", &opt);
        
        switch (opt) {
            case 1:
                printf("Quantos valores de X/f(X) existem?\n");
                scanf("%d", &qXis);
                aloca(&xis, qXis);
                aloca(&fxis, qXis);
                aloca(&L, qXis);
                lagrange(xis, fxis, L, qXis);
            break;
            case 2:
                printf("Qual o maior grau da equação?\n");
                scanf("%d", &maiorGrau);
                aloca(&valoresDaEquacao, maiorGrau);
                dichotomy(valoresDaEquacao, maiorGrau);
            break;
            default:
                if (opt != 0)
                    printf("\nA opção %d não existe\n\n", opt);
        }
        
    } while (opt != 0);

    

    return 0;
}


/*
==================================
Funções para execução da DICOTOMIA
==================================
*/

void dichotomy(double *valoresDaEquacao, int maiorGrau) {
    for (int i=0; i<=maiorGrau; i++) {
        printf("Digite valor de X^%d:\n", i);
        scanf("%lf", (valoresDaEquacao+i));
    }
    
    int opt;
    do {
        calculateDichotomy(valoresDaEquacao, maiorGrau);
        printf("\n\nVoce deseja calcular para outro intervalo e/ou erro? \n[1] Sim \n[0] Nao\n");
        scanf("%d", &opt);
    } while (opt != 0);

}

void calculateDichotomy(double *valoresDaEquacao, int maiorGrau) {
    double precisao, A, B;
    
    printf("Qual o valor de A do intervalo?\n");
    scanf("%lf", &A);

    printf("Qual o valor de B do intervalo?\n");
    scanf("%lf", &B);

    if (A > B) {
        double aux = A;
        A = B;
        B = aux;
        printf("O valor de A não pode ser maior que B, portanto o software inverteu eles automaticamente, agora A = %.3lf e B = %.3f\n",A,B);
    }

    printf("Qual a precisão?\n");
    scanf("%lf", &precisao);

    bool temRaiz = f(A, valoresDaEquacao, maiorGrau) * f(B, valoresDaEquacao, maiorGrau) < 0;

    if (!temRaiz) {
        printf("Não tem raiz.\n");
    }

    double k = (log(abs(B-A))-log(precisao))/log(2);
    
    double M = 0;
    int iteration = 0;
    
    printf("\nI\tA\tM\tB\tf(A)\tf(M)\tf(B)\n");
    do {
        M = (A+B)/2;
        printf("%d\t%.3lf\t%.3lf\t%.3lf\t%.3lf\t%.3lf\t%.3lf\n",iteration,A,M,B,f(A, valoresDaEquacao, maiorGrau),f(M, valoresDaEquacao, maiorGrau),f(B, valoresDaEquacao, maiorGrau));
        
        if (f(A, valoresDaEquacao, maiorGrau) * f(M, valoresDaEquacao, maiorGrau) < 0)
            B = M;
        else
            A = M;
        
        iteration++;
    } while (fabs(f(M, valoresDaEquacao, maiorGrau)) >= precisao);

    printf("\nA raiz e %.3lf com erro de +/- %.3lf", M, fabs(f(M, valoresDaEquacao, maiorGrau)));
    printf("\nA quantidade de iteracoes e aproximadamente %.0lf (k=%.3lf)", ceil(k), k);
}

// Função para executar o calculo da função (f) 
double f(double X, double *valoresDaEquacao, int tam) {
    double resultadoDaFuncao = 0.0;
    for (int i=0; i<=tam; i++) {
        if (*(valoresDaEquacao+i) != 0) {
            resultadoDaFuncao += *(valoresDaEquacao+i) * pow(X, i);
        }
    }
    return resultadoDaFuncao;
}

/*
==================================
Funções para execução de LAGRANGE
==================================
*/

void lagrange(double *xis, double *fxis, double *L, int qXis) {
    for (int i=0; i<qXis; i++) {
        printf("Qual o valor de X%d?\n", i);
        scanf("%lf", (xis+i));
        printf("Qual o valor de f(X%d)?\n", i);
        scanf("%lf", (fxis+i));
    }

    // Show table
    showTable(xis, fxis, qXis);
    
    int opt;
    do {
        interoplation(xis, fxis, L, qXis);
        printf("\n\nVoce deseja interpolar outro ponto? \n[1] Sim \n[0] Nao\n");
        scanf("%d", &opt);
    } while (opt != 0);
}

void showTable(double *xis, double *fxis, int qXis) {
    printf("\n\n===== Your table ======\n\n");

    printf("X\t");
    for (int i=0; i<qXis; i++) {
        printf("%.3lf\t",*(xis+i));
    }
    printf("\n");
    printf("f(X)\t");
    for (int i=0; i<qXis; i++) {
        printf("%.3lf\t",*(fxis+i));
    }
    printf("\n");
}

void interoplation(double *xis, double *fxis, double *L, int qXis) {
    double x;
    printf("\nDigite o ponto a ser interpolado\n");
    scanf("%lf", &x);
    
    double resX;
    
    // Calculate L
    int needToAttribuiteValue;
    
    for (int i=0; i<qXis; i++) {
        needToAttribuiteValue = 1;
        
        for (int j=0; j<qXis; j++) {
            if (i!=j) {
                if (needToAttribuiteValue==1) {
                    *(L+i) = (x-(*(xis+j)))/(*(xis+i)-(*(xis+j)));
                    needToAttribuiteValue=0;
                }else{
                    *(L+i) *= (x-(*(xis+j)))/(*(xis+i)-(*(xis+j)));   
                }
            }
        }
        
        printf("\nL[%d]=%.3lf",i,*(L+i));
    }
    
    // Calculate p(X)
    for (int i=0; i<qXis; i++) {

        resX += (*(fxis+i)) * (*(L+i));
    }
        
    printf("\n\nO ponto %.3lf em f(x) e: %.3lf\n", x, resX);
}

// =====
// ALOCA
// =====
void aloca(double **p, int tam) {
    if (( *p=(double*)realloc(*p,tam*sizeof(double)) ) == NULL)
    {
        printf("Nao foi possivel alocar dados");
	    printf("\n--------\n");
        exit(1);
    }
}