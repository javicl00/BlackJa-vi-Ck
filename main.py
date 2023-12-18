import random
import tkinter as tk
from tkinter import messagebox
from logica import *

# Funciones de Blackjack similares al código anterior...
# Función para crear una baraja

def mostrar_interfaz():
    ventana = tk.Tk()
    ventana.title("Blackjack")

    def iniciar_juego():
        baraja = crear_baraja()
        mano_jugador = [baraja.pop(), baraja.pop()]
        mano_crupier = [baraja.pop(), baraja.pop()]

        def mostrar_mano_jugador():
            nonlocal mano_jugador_frame
            mano_jugador_frame.destroy()
            mano_jugador_frame = tk.Frame(ventana)
            mano_jugador_frame.pack()
            for carta in mano_jugador:
                carta_label = tk.Label(mano_jugador_frame, text=f"{carta[0]} de {carta[1]}")
                carta_label.pack(side=tk.LEFT)

        def pedir_carta():
            mano_jugador.append(baraja.pop())
            mostrar_mano_jugador()

        def plantarse():
            while valor_mano(mano_crupier) < 17:
                mano_crupier.append(baraja.pop())

            if valor_mano(mano_jugador) > 21:
                messagebox.showinfo("Resultado", "Te pasaste de 21. ¡Perdiste!")
            else:
                resultado = determinar_ganador()
                messagebox.showinfo("Resultado", resultado)

        def determinar_ganador():
            valor_jugador = valor_mano(mano_jugador)
            valor_crupier = valor_mano(mano_crupier)

            if valor_crupier > 21 or valor_jugador > valor_crupier:
                return "¡Ganaste!"
            elif valor_crupier > valor_jugador:
                return "El crupier gana. ¡Perdiste!"
            else:
                return "Empate."

        juego_frame = tk.Frame(ventana)
        juego_frame.pack()

        mano_jugador_frame = tk.Frame(ventana)
        mano_jugador_frame.pack()

        mostrar_mano_jugador()

        crupier_frame = tk.Frame(ventana)
        crupier_frame.pack()
        carta_oculta_label = tk.Label(crupier_frame, text="<carta oculta>")
        carta_oculta_label.pack(side=tk.LEFT)
        for _ in mano_crupier[1:]:
            carta_label = tk.Label(crupier_frame, text=f"{_[0]} de {_[1]}")
            carta_label.pack(side=tk.LEFT)

        botones_frame = tk.Frame(ventana)
        botones_frame.pack()

        pedir_carta_btn = tk.Button(botones_frame, text="Pedir carta", command=pedir_carta)
        pedir_carta_btn.pack(side=tk.LEFT)

        plantarse_btn = tk.Button(botones_frame, text="Plantarse", command=plantarse)
        plantarse_btn.pack(side=tk.LEFT)

    boton_iniciar = tk.Button(ventana, text="Iniciar Juego", command=iniciar_juego)
    boton_iniciar.pack()

    ventana.mainloop()

if __name__ == "__main__":
    mostrar_interfaz()
