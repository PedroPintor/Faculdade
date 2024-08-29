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

int printarVetor(int vetor[], int enao, int novoEninho){
    // printa o valor do novo vetor valido
    for ( int i = 0; i < novoEninho; i++){
        printf("%d ", vetor[i]);
    }
    
    printf("\n");
    
    // printa o vetor inteiro
    for ( int j = 0; j < enao; j++){
        printf("%d ", vetor[j]);
    }
}


int main()
{
    // tamanho --> n[0...11] N[17]
    int enao = 17;
    int eninho = 11;
    
    int vetor[] = { 1,0,2,3,0,0,3,3,0,4,2,      9,9,9,9,9,9};
    
    // com vetor vazio da overflow
    int vetorVazio[] = {};
    // vom o vetor cheio de zeros , vai me retornar um novo n( vetor valido ) de tamanho 0
    // esse é melhor cenario --> O(n): 3n + 2
    int vetorZeros[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    // vetor sem zeros, vai retornar n = N ( vetor valido = vetor )
    // esse é o pior cenario --> O(n): 4n + 2
    int vetorSemZero[] = {5,1,6,2,7,3,76,90,34,43,12,        48,23,28,16,91,61};
    
    // essa parte do codigo é so para a variavel "vetor"
    int novoEninho = tirazeros( eninho, vetor);
    printf("%d \n", novoEninho);
    printarVetor(vetor,enao,novoEninho);
    
    
    
    // essa parte do codigo é para printar os outros vetores
    int teste = tirazeros(eninho, vetorSemZero);
    printf("%d \n", teste);
    for ( int bbb = 0; bbb < eninho; bbb++){
        printf("%d ", vetorSemZero[bbb]);
    }
    
    return 0;
}