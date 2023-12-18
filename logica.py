import random

# Función para crear una baraja
def crear_baraja():
    baraja = []
    for palo in ['Corazones', 'Diamantes', 'Treboles', 'Picas']:
        for valor in range(2, 11):
            baraja.append((str(valor), palo))
        for figura in ['J', 'Q', 'K', 'A']:
            baraja.append((figura, palo))
    random.shuffle(baraja)
    return baraja
# Función para calcular el valor de la mano
def valor_mano(mano):
    valor = 0
    ases = 0
    for carta in mano:
        if carta[0] in ['J', 'Q', 'K']:
            valor += 10
        elif carta[0] == 'A':
            ases += 1
        else:
            valor += int(carta[0])
    valor += ases * 11
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor