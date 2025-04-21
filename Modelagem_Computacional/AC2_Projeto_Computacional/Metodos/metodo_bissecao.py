# Metodos/

# método da bisseção
def metodo_bissecao(funcao,inicio_intervalo, fim_intervalo, erro=0.001, max_iter=200):
    
    inicio = funcao(inicio_intervalo)
    fim = funcao(fim_intervalo)

    if inicio * fim > 0:
        print(f"Intervalo inválido: {inicio} e {fim} têm o mesmo sinal.")
        return None
    
    else:
        iterador = 0
        meio_intervalo = (inicio_intervalo + fim_intervalo) / 2
        # abs(): absolute value
        while abs(funcao(meio_intervalo)) > erro and iterador < max_iter:
            if funcao(inicio_intervalo) * funcao(meio_intervalo) < 0:
                fim_intervalo = meio_intervalo
            else:
                inicio_intervalo = meio_intervalo

            meio_intervalo = (inicio_intervalo + fim_intervalo) / 2
            iterador += 1
        
        if iterador >= max_iter:
            print("Número máximo de iterações alcançado.")
        
        return meio_intervalo , iterador

def encontrar_intervalo(funcao):
    intervalo = False
    print(' Escolha um Numero \n ')
    while not intervalo :
        inicio = pegar_numero('inicio do intervalo: ')
        final = pegar_numero(' final do intervalo: ')
        i = funcao(inicio)
        f = funcao(final)
        
        if i * f < 0:
            intervalo = True
            print(f' intervalo valido {i} {f}')
        else:
            print(' intervalo invalido, tente outros valores ')
            print(f"Intervalo inválido: {i} e {f} têm o mesmo sinal.")
    return inicio,final

def pegar_numero(mensagem = 'digite um numero: '):
    while True:
        try:
            numero = float(input(mensagem))
            break
        except ValueError as e:
            print(' numero invalido ')
            print(f'erro: {e}')
    return numero