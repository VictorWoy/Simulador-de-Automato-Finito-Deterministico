class AFD:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes
    
    def verificar_palavra(self, palavra):
        estado_atual = self.estado_inicial
        for simbolo in palavra:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                return False
        return estado_atual in self.estados_finais


# Função para obter as informações do AFD a partir da entrada do usuário
def obter_informacoes_afd():
    estados = input("Informe os estados do AFD (separados por vírgula): ").split(',')
    estado_inicial = input("Informe o estado inicial do AFD: ")
    estados_finais = input("Informe os estados finais do AFD (separados por vírgula): ").split(',')
    
    transicoes = {}
    print("Informe as transições de estados (digite 'sair' para encerrar):")
    while True:
        transicao = input("Transição (estado_atual, símbolo, estado_destino): ")
        if transicao == 'sair':
            break
        estado_atual, simbolo, estado_destino = transicao.split(',')
        transicoes[(estado_atual.strip(), simbolo.strip())] = estado_destino.strip()
    
    return estados, estado_inicial, estados_finais, transicoes


# Exemplo de utilização
print("Bem-vindo ao simulador de Autômatos AFD e AFND!")
estados, estado_inicial, estados_finais, transicoes = obter_informacoes_afd()

afd = AFD(estados, estado_inicial, estados_finais, transicoes)

while True:
    palavra = input("Informe uma palavra (ou 'sair' para encerrar): ")
    if palavra == 'sair':
        break
    if afd.verificar_palavra(palavra):
        print("A palavra foi aceita pelo AFD.")
    else:
        print("A palavra foi rejeitada pelo AFD.")
