# src/sim/Q0009_1_quantum_game.py
# Project: HUNT-QSoC "Continuum" v1.2 (Gaming Evolution)
# Interface: Native 32-bit Window Engine (Tkinter Framework)

import tkinter as tk
import random
import math

class QuantumTkinterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔱 HUNT-QSoC Continuum v1.2 - Quantum Interface")
        self.root.geometry("820x620")
        self.root.configure(bg="#020305")
        self.root.resizable(False, False)

        # Variables lógicas del Superchip y la QRAM
        self.qram_stability = 128.0
        self.score = 0
        self.player_x = 400
        self.enemy_x = random.randint(80, 720)
        self.enemy_y = 40
        self.laser_active = False

        self._build_centered_interface()
        self._start_quantum_loop()

    def _build_centered_interface(self):
        # 1. CUADRO DE CONSOLA INDUSTRIAL SUPERIOR
        console_frame = tk.Frame(self.root, bg="#090d16", bd=1, relief="solid", highlightbackground="#1f3a60", highlightthickness=1)
        console_frame.pack(pady=10, fill="x", px=20)
        
        tk.Label(console_frame, text=">>> INTERFAZ DE NAVEGACIÓN NATAL (32-BIT TKINTER PIPELINE)", font=("Courier New", 11, "bold"), fg="#00ffaa", bg="#090d16").pack(anchor="w", px=5)
        
        self.telemetry_lbl = tk.Label(console_frame, text=f"QRAM COHERENTE: {self.qram_stability} GB | LATENCIA: 0.00 ns | PUNTAJE: {self.score}", font=("Courier New", 10), fg="#ffffff", bg="#090d16")
        self.telemetry_lbl.pack(anchor="w", px=5, py=2)

        # 2. EL LIENZO GRÁFICO DEL VIDEOJUEGO (Canvas de neón en fondo negro)
        self.canvas = tk.Canvas(self.root, width=760, height=400, bg="#010205", highlightbackground="#1f3a60", highlightthickness=2)
        self.canvas.pack(pady=5)

        # 3. PANEL DE MANDOS INFERIOR (Ideal para Touchpad sin ratón)
        control_frame = tk.Frame(self.root, bg="#020305")
        control_frame.pack(pady=10)

        # Mando deslizante integrado en la ventana para mover la nave verde
        self.slider = tk.Scale(control_frame, from_=50, to=710, orientation="horizontal", label="Alinear Caza Cuántico (Eje X)", font=("Courier New", 9), fg="#ffffff", bg="#090d16", troughcolor="#1f3a60", activebackground="#00ffaa", length=350, command=self._move_player)
        self.slider.set(400)
        self.slider.grid(row=0, column=0, px=20)

        # Botón físico neón de disparo de alta precisión
        fire_btn = tk.Button(control_frame, text="💥 DISPARAR RAYO ANTINODO", font=("Courier New", 12, "bold"), fg="#00ffaa", bg="#1f3a60", activebackground="#00ffaa", activeforeground="#020305", bd=2, relief="raised", command=self._fire_laser, width=25, height=2)
        fire_btn.grid(row=0, column=1, px=20)

    def _move_player(self, val):
        self.player_x = int(val)

    def _fire_laser(self):
        self.laser_active = True
        # Pitido acústico nativo por hardware del portátil (bip limpio al disparar)
        self.root.bell()
        
        # Verificar interceptación geométrica del Teorema de Hunt en el eje X
        if abs(self.player_x - self.enemy_x) <= 35:
            self.qram_stability += 15.0
            if self.qram_stability > 256: self.qram_stability = 256.0
            self.score += 100
            # Desintegrar la nave de ruido roja y regenerarla arriba
            self.enemy_y = 40
            self.enemy_x = random.randint(80, 720)
        else:
            self.qram_stability -= 10.0

    def _start_quantum_loop(self):
        # Desplazamiento continuo de la nave enemiga Nvidia por el pipeline
        self.enemy_y += 12
        
        if self.enemy_y >= 380:
            self.enemy_y = 40
            self.enemy_x = random.randint(80, 720)
            self.qram_stability -= 15.0 # Penalización si el ruido impacta la base

        if self.qram_stability < 0: self.qram_stability = 0.0

        # LIMPIAR Y REDIBUJAR EL HARDWARE EN EL CANVAS
        self.canvas.delete("all")

        # Dibujar líneas de bus estáticas de fondo
        for i in range(0, 760, 40):
            self.canvas.create_line(i, 0, i, 400, fill="#07111b")
            self.canvas.create_line(0, i, 760, i, fill="#07111b")

        # Dibujar Caza de Ruido de Nvidia (Enemigo - Nave Triangular Roja)
        ex, ey = self.enemy_x, self.enemy_y
        self.canvas.create_polygon(ex, ey, ex - 18, ey - 22, ex + 18, ey - 22, fill="#ff4b4b", outline="#ffffff")

        # Dibujar tu Caza Fotónico Cuántico (Jugador - Nave Triangular Verde Neón)
        px, py = self.player_x, 375
        self.canvas.create_polygon(px, py - 22, px - 20, py, px + 20, py, fill="#00ffaa", outline="#ffffff")

        # Dibujar el Rayo Láser de Cancelación Azul Neón (Si está activo)
        if self.laser_active:
            self.canvas.create_line(px, py - 22, px, 0, fill="#00ffff", width=5)
            self.laser_active = False # El rayo combinacional se propaga instantáneo

        # Actualizar textos de telemetría de la consola central
        self.telemetry_lbl.config(text=f"QRAM COHERENTE: {self.qram_stability:.1f} GB  |  LATENCIA INTERNAL: 0.00 ns  |  MARCADOR: {self.score}")

        if self.qram_stability > 0:
            # Lazo de refresco automatizado continuo (Sincronizado para laptops)
            self.root.after(45, self._start_quantum_loop)
        else:
            self.canvas.create_text(380, 200, text="DECORRECCIÓN TÉRMICA DEL CHIP\nGAME OVER", font=("Courier New", 24, "bold"), fill="#ff4b4b", justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumTkinterGame(root)
    root.mainloop()