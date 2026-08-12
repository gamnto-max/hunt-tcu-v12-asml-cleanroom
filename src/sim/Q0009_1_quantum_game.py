# src/sim/Q0009_1_quantum_game.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite Completed)
# Interface: Native 32-bit Window Engine (Tkinter Framework - Full Clean Rebuild)

import tkinter as tk
import random

class QuantumTkinterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔱 HUNT-QSoC Continuum v1.2 - Quantum Interface")
        self.root.geometry("820x620")
        self.root.configure(bg="#020305")
        self.root.resizable(False, False)

        # Variables unificadas rígidas del SoC Cuántico y la QRAM
        self.qram_score = 128.0
        self.score = 0
        self.player_x = 400
        self.enemy_x = random.randint(80, 720)
        self.enemy_y = 40
        self.laser_active = False

        self._build_centered_interface()
        self._start_quantum_loop()

    def _build_centered_interface(self):
        # 1. CUADRO DE CONSOLA INDUSTRIAL SUPERIOR (Centrado Simétrico)
        console_frame = tk.Frame(self.root, bg="#090d16", bd=1, relief="solid")
        console_frame.pack(pady=10, fill="x", padx=20)
        
        tk.Label(console_frame, text=">>> INTERFAZ DE NAVEGACIÓN NATAL (32-BIT TKINTER PIPELINE)", font=("Courier New", 11, "bold"), fg="#00ffaa", bg="#090d16").pack(anchor="w", padx=5)
        
        self.telemetry_lbl = tk.Label(console_frame, text="", font=("Courier New", 10), fg="#ffffff", bg="#090d16")
        self.telemetry_lbl.pack(anchor="w", padx=5, py=2)

        # 2. EL LIENZO GRÁFICO DEL VIDEOJUEGO (Canvas de neón en fondo negro)
        self.canvas = tk.Canvas(self.root, width=760, height=400, bg="#010205", highlightbackground="#1f3a60", highlightthickness=2)
        self.canvas.pack(pady=5)

        # 3. PANEL DE MANDOS INFERIOR (Optimizado para Touchpad de la Laptop)
        control_frame = tk.Frame(self.root, bg="#020305")
        control_frame.pack(pady=10)

        # Mando deslizante integrado para mover tu nave verde
        self.slider = tk.Scale(control_frame, from_=50, to=710, orientation="horizontal", label="Alinear Caza Cuántico (Eje X)", font=("Courier New", 9), fg="#ffffff", bg="#090d16", troughcolor="#1f3a60", activebackground="#00ffaa", length=350, command=self._move_player)
        self.slider.set(400)
        self.slider.grid(row=0, column=0, padx=20)

        # Botón físico neón de disparo instantáneo
        fire_btn = tk.Button(control_frame, text="💥 DISPARAR RAYO ANTINODO", font=("Courier New", 12, "bold"), fg="#00ffaa", bg="#1f3a60", activebackground="#00ffaa", bd=2, relief="raised", command=self._fire_laser, width=25, height=2)
        fire_btn.grid(row=0, column=1, padx=20)

    def _move_player(self, val):
        self.player_x = int(val)

    def _fire_laser(self):
        self.laser_active = True
        self.root.bell() # Activación del zumbido acústico por hardware de la laptop
        
        # Teorema de Hunt: Verificación combinacional de la colisión en el bus de 64 bits
        if abs(self.player_x - self.enemy_x) <= 45:
            self.qram_score += 15.0
            if self.qram_score > 256: self.qram_score = 256.0
            self.score += 100
            # Desintegración de la nave de ruido de Nvidia y regeneración arriba
            self.enemy_y = 40
            self.enemy_x = random.randint(80, 720)
        else:
            self.qram_score -= 10.0

    def _start_quantum_loop(self):
        # Desplazamiento continuo del ruido de transistores descendiendo por la oblea
        self.enemy_y += 12
        if self.enemy_y >= 380:
            self.enemy_y = 40
            self.enemy_x = random.randint(80, 720)
            self.qram_score -= 15.0  # El ruido clásico golpea la RAM

        if self.qram_score < 0: self.qram_score = 0.0

        # LIMPIAR EL PIPELINE ANTERIOR
        self.canvas.delete("all")

        # Dibujar rejilla molecular del Silicio-28
        for i in range(0, 760, 40):
            self.canvas.create_line(i, 0, i, 400, fill="#07111b")
            self.canvas.create_line(0, i, 760, i, fill="#07111b")

        # Dibujar Caza de Ruido de Nvidia (Enemigo - Nave Triangular Roja)
        ex, ey = self.enemy_x, self.enemy_y
        self.canvas.create_polygon(ex, ey, ex - 18, ey - 22, ex + 18, ey - 22, fill="#ff4b4b", outline="#ffffff")

        # Dibujar tu Caza Fotónico Cuántico (Jugador - Nave Triangular Verde Neón)
        px, py = self.player_x, 375
        self.canvas.create_polygon(px, py - 22, px - 20, py, px + 20, py, fill="#00ffaa", outline="#ffffff")

        # Dibujar el Rayo Láser de Cancelación Azul Neón (Si está activo a 0.00 ns)
        if self.laser_active:
            self.canvas.create_line(px, py - 22, px, 0, fill="#00ffff", width=5)
            self.laser_active = False 

        # Formateo de texto de telemetría seguro libre de desbordes
        metric_text = "QRAM COHERENTE: " + str(round(self.qram_score, 1)) + " GB | LATENCIA: 0.00 ns | MARCADOR: " + str(self.score)
        self.telemetry_lbl.config(text=metric_text)

        if self.qram_score > 0:
            # Lazo de refresco continuo coordinado (60 FPS equivalentes)
            self.root.after(40, self._start_quantum_loop)
        else:
            self.canvas.create_text(380, 200, text="DECORRECCIÓN TÉRMICA DEL CHIP\nGAME OVER", font=("Courier New", 24, "bold"), fill="#ff4b4b", justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumTkinterGame(root)
    root.mainloop()
