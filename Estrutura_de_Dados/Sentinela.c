#include <stdio.h>
#include <stdlib.h>
#include<time.h>

void gerarListaAleatoria(int tamanho, int* lista){
    // printf("intervalo da rand: [0,%d]\n", RAND_MAX);
    
    srand((unsigned int)time(NULL));
    for (int i = 0; i < tamanho; i++){
        lista[i] = rand() % 10;
    }
    
    for (int j = 0; j < tamanho; j++){
        printf("%d \n", lista[j]);
    }

}

int buscarNaLista(int lista[], int numero,int tamanho){
    // sentinela
    lista[tamanho] = numero;
    int indice = 0;
    while( lista[indice] != numero ){
        indice++;
    }
    
    if ( indice < tamanho) return indice;
    return -1;
}


int main()
{
    int numero, tamanho=12;
    printf("digite o numero para procurar na lista: \n");
    scanf("%d", &numero);
    // printf("digite o tamanho da lista: \n");
    // scanf("%d", &tamanho);
    // int lista[tamanho];
    // gerarListaAleatoria(tamanho, lista);
    
    // tamanho --> n = 12
    int lista[] = {12,3,5,11,7,4,6,15,13,2,1,999};
    
    
    int posicaoDoNumeroNaLista = buscarNaLista( lista, numero , tamanho);
    
    if ( posicaoDoNumeroNaLista < 0){
        printf("nao tem o numero digitado :(");
    }
    else{
        printf(" o numero foi encontrado \n ele esta na posiçao: %d da lista \n", posicaoDoNumeroNaLista);
    }
    return 0;
    
    
    