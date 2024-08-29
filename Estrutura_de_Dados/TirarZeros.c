/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int tirazeros (int n, int v[]){
    // esse valor vai nos mostrar o indice de um novo n( tamanho valido do vetor )
    int indiceDoEninho = 0;
    for (int j = 0; j < n ; j++){
        // quando achar um numero diferente de 0, significa que eu quero esse valor
        // assim, atualizamos o tamanho do n( tamanho valido do vetor ) --> indiceDoEninho + 1
        if (v[j] != 0){
            // primeiro atribui , depois incremente o valor no "indiceDoEninho"
            v[indiceDoEninho++] = v[j];
        }
    }
    // retorna o novo tamanho do vetor valido
    return indiceDoEninho;
}

int main()
{
    // tamanho --> n[0...11] N[17]
    int vetor[] = { 1,0,2,3,0,0,3,3,0,4,2,      9,9,9,9,9,9};
    int enao = 17;
    int eninho = 11;
    int novoEninho = tirazeros( eninho, vetor);
    printf("%d \n", novoEninho);
    
    // printa o valor do novo vetor valido
    for ( int i = 0; i < novoEninho; i++){
        printf("%d ", vetor[i]);
    }
    
    printf("\n");
    
    // printa o vetor inteiro
    for ( int j = 0; j < enao; j++){
        printf("%d ", vetor[j]);
    }
    
    return 0;
}