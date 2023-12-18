import numpy as np
import tensorflow as tf
from logica import *
from tkinter import messagebox
import tkinter as tk


# Función para codificar las cartas
def codificar_carta(carta):
    codificacion = np.zeros(52)
    valor, palo = carta
    valores_cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos_cartas = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    codificacion[valores_cartas.index(valor) + palos_cartas.index(palo) * 13] = 1 
    return codificacion

# Función para crear datos de entrenamiento. 
def generar_datos_entrenamiento():
    datos_entrenamiento = []
    for i in range(2, 11): 
        for palo in ['Hearts', 'Diamonds', 'Clubs', 'Spades']: 
            datos_entrenamiento.append(codificar_carta((str(i), palo)))
        for figura in ['J', 'Q', 'K', 'A']:
            datos_entrenamiento.append(codificar_carta((figura, palo)))
    return np.array(datos_entrenamiento)

# Función para crear etiquetas (decisiones)
def generar_etiquetas():
    decisiones = [0] * 17 + [1] * 4  # 0 para plantarse, 1 para pedir carta
    return tf.keras.utils.to_categorical(decisiones, num_classes=2)

# Crear el modelo de red neuronal
modelo = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, input_shape=(52,), activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Generar datos de entrenamiento y etiquetas
datos_entrenamiento = generar_datos_entrenamiento()
etiquetas = generar_etiquetas()

# Entrenar el modelo
modelo.fit(datos_entrenamiento, etiquetas, epochs=10, batch_size=32)

# Guardar el modelo
modelo.save('modelo.h5')

# Cargar el modelo
modelo = tf.keras.models.load_model('modelo.h5')

# Función para determinar la decisión
def determinar_decision(mano_jugador, mano_crupier):
    decision = modelo.predict(np.array([codificar_carta(carta) for carta in mano_jugador + [mano_crupier[0]]]))
    return np.argmax(decision)

# Función para determinar el ganador
def determinar_ganador(mano_jugador, mano_crupier):
    valor_jugador = valor_mano(mano_jugador)
    valor_crupier = valor_mano(mano_crupier)

    if valor_crupier > 21 or valor_jugador > valor_crupier:
        return "¡Ganaste!"
    elif valor_crupier > valor_jugador:
        return "El crupier gana. ¡Perdiste!"
    else:
        return "Empate."
    
# Función para jugar
def jugar():
    baraja = crear_baraja()
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_crupier = [baraja.pop(), baraja.pop()]

    while determinar_decision(mano_jugador, mano_crupier) == 1:
        mano_jugador.append(baraja.pop())

    while valor_mano(mano_crupier) < 17:
        mano_crupier.append(baraja.pop())

    print(f"Mano del jugador: {mano_jugador}")
    print(f"Mano del crupier: {mano_crupier}")
    print(determinar_ganador(mano_jugador, mano_crupier))

# Jugar
jugar()

# Función para jugar n veces
def jugar_n_veces(n):
    for _ in range(n):
        jugar()

# Jugar 100 veces
jugar_n_veces(100)

# Función para jugar n veces y guardar los resultados
def jugar_n_veces(n):
    resultados = []
    for _ in range(n):
        baraja = crear_baraja()
        mano_jugador = [baraja.pop(), baraja.pop()]
        mano_crupier = [baraja.pop(), baraja.pop()]

        while determinar_decision(mano_jugador, mano_crupier) == 1:
            mano_jugador.append(baraja.pop())

        while valor_mano(mano_crupier) < 17:
            mano_crupier.append(baraja.pop())

        resultados.append(determinar_ganador(mano_jugador, mano_crupier))
    return resultados

# Jugar 100 veces y guardar los resultados
resultados = jugar_n_veces(100)

# Función para determinar la probabilidad de ganar
def probabilidad_ganar(resultados):
    return resultados.count("¡Ganaste!") / len(resultados)

# Determinar la probabilidad de ganar
probabilidad_ganar(resultados)

# Función para automatizar el proceso
def jugar_n_veces(n):
    resultados = []
    for _ in range(n):
        baraja = crear_baraja()
        mano_jugador = [baraja.pop(), baraja.pop()]
        mano_crupier = [baraja.pop(), baraja.pop()]

        while determinar_decision(mano_jugador, mano_crupier) == 1:
            mano_jugador.append(baraja.pop())

        while valor_mano(mano_crupier) < 17:
            mano_crupier.append(baraja.pop())

        resultados.append(determinar_ganador(mano_jugador, mano_crupier))
    return resultados


