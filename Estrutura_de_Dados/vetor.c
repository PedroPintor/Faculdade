
#include <stdio.h>
#include <stdlib.h>



typedef struct Atendimento {
    char nome;
    float horario;
}Atendimento;


typedef struct agendaDiaria {
    Atendimento dia[6];
    int N;
    int n;

}agendaDiaria;


agendaDiaria* criar_agenda(){
    agendaDiaria* novaAgenda = (agendaDiaria *)malloc(sizeof(agendaDiaria));
    novaAgenda->N = 6;
    novaAgenda->n = 0;

    return novaAgenda;
}


int ta_vazio( agendaDiaria* dia){
    if ( dia->n == 0 ){
        return 1;
    }
    return 0;
}

int ta_cheio( agendaDiaria* dia){
    if ( dia->N != dia->n){
        return 0;
    }
    return 1;
}

Atendimento novo_atendimento( char nome, float horario){
    Atendimento novo_atendimento;
    novo_atendimento.nome = nome;
    novo_atendimento.horario = horario;

    return novo_atendimento;
}

void insertionSort (agendaDiaria* agenda) {
    int i;
    int j;
    float value;

    for (i = 1; i < agenda->n; i++){
        value = agenda->dia[i].horario;

        for (j = i - 1; (j >= 0) && (value < agenda->dia[j].horario); j --)
        {
            agenda->dia[j + 1] = agenda->dia[j];           
        }
        agenda->dia[j + 1].horario = value;               
     }                          
}

agendaDiaria* marcar_horario_fim( agendaDiaria* dia, Atendimento atendimento) {
    if ( ta_cheio(dia)){
        return NULL;
    }

    dia->dia[dia->n] = atendimento;
    insertionSort( dia);
    dia->n += 1;
}

agendaDiaria* marcar_horario_meio( agendaDiaria* dia, Atendimento atendimento){

}
int index_horario( agendaDiaria* dia, int horario){
    for ( int i = 0; i < dia->n; i++){
        if ( dia->dia[i].horario == horario ){
            return i;
        }
    }
    return -1;
}

int deletar_horario( agendaDiaria* dia, float horario){
    int index = index_horario( dia, horario);

    if ( index == -1 ) return 0;
    for ( int i = index; i < dia->n; i++){
        dia->dia[i] = dia->dia[i+1];
    }
    dia->n -= 1;
    return 1;
}



int agendar_atendimento( agendaDiaria *agenda,char nome, float horario) {
    
    Atendimento novoAtendimento = novo_atendimento( nome, horario); 
    
    if ( ta_vazio( agenda)){
        marcar_horario_fim( agenda, novoAtendimento);
        return 1;
    }

    int index = index_horario( agenda, horario);
    
    if ( index == -1 ){
        marcar_horario_fim( agenda, novoAtendimento);
        return 1;
    }

}

void printar_dia( agendaDiaria* dia){
    for ( int i = 0; i<dia->n; i++){
        printf( " %f ", dia->dia[i].horario);
    }
    printf(" \n");
}



int main() {
    
    agendaDiaria *agenda = criar_agenda();

    Atendimento atendimento = novo_atendimento( 'p', 7.5);
    Atendimento atendimento2 = novo_atendimento( 'l', 1);
    Atendimento atendimento3 = novo_atendimento( 'i', 6.5);
    Atendimento atendimento4 = novo_atendimento( 'k', 10);
    marcar_horario_fim( agenda, atendimento);
    marcar_horario_fim( agenda, atendimento2);
    marcar_horario_fim( agenda, atendimento3);
    marcar_horario_fim( agenda, atendimento4);

    printar_dia( agenda);

    deletar_horario(agenda, 1);

    printar_dia( agenda);

    free(agenda);
}



