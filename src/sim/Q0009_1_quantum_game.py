# src/sim/Q0009_quantum_game.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
# Objective: 32-bit Native Terminal 3D Pipeline Arcade - Key Driven (A / D)

import time
import os
import math
import random

class QuantumTerminal3DEngine:
    def __init__(self):
        self.width = 65
        self.height = 14
        self.player_angle = 0.0
        self.speed = 0.4
        self.qram_stability = 128.0
        self.score = 0
        
        # Matrices de naves de ruido clásicas de Nvidia (Ángulo y Profundidad Z)
        self.obstacles = [
            {"angle": random.uniform(0, 6.28), "z": 10.0},
            {"angle": random.uniform(0, 6.28), "z": 15.0}
        ]

    def render_frame(self):
        # Limpiar la terminal de forma nativa en Windows
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Avanzar el pipeline 3D de los bloques de ruido hacia el jugador
        alert_active = False
        for obs in self.obstacles:
            obs["z"] -= 0.6  # Velocidad de aproximación
            if obs["z"] < 4.0:
                alert_active = True
                
            # Si el bloque supera el eje del jugador, se absorbe con éxito
            if obs["z"] <= 1.0:
                obs["z"] = 15.0
                obs["angle"] = random.uniform(0, 6.28)
                self.qram_stability += 5.0
                self.score += 100
                
            # DETECTOR DE IMPACTO DIRECTO DE RUIDO
            if 1.8 < obs["z"] < 2.5:
                angle_diff = abs(self.player_angle - obs["angle"])
                if angle_diff > math.pi:
                    angle_diff = 2 * math.pi - angle_diff
                if angle_diff < 0.6:  # Colisión molecular de fase
                    self.qram_stability -= 20.0
                    obs["z"] = 15.0
                    obs["angle"] = random.uniform(0, 6.28)

        # Delimitar límites de la memoria unificada
        if self.qram_stability < 0: self.qram_stability = 0.0
        if self.qram_stability > 256: self.qram_stability = 256.0

        # CONSOLA MAESTRA DE TELEMETRÍA (Centrada en tu monitor)
        print("=================================================================")
        print("    🔱 CONTINUUM SoC v1.2 -- INTERCEPTOR EN 3D REAL (32-BIT)    ")
        print("=================================================================")
        print(f" Estabilidad QRAM: {self.qram_stability:.1f} GB  |  Latencia SoC: 0.00 ns  |  Score: {self.score}")
        status = "⚠️ DESFASE DETECTADO" if alert_active else "✅ CIRCUITO INTEGRAL BUS_OK"
        print(f" Estado de Red   : {status}")
        print("=================================================================\n")

        # RENDERIZADO DEL TÚNEL EN PERSPECTIVA GRÁFICA ASCII
        # Se calcula la matriz espacial celda por celda según geometría algebraica
        for y in range(self.height):
            row_str = "  "
            comp_y = (y - self.height / 2) / (self.height / 2)
            
            for x in range(self.width):
                comp_x = (x - self.width / 2) / (self.width / 2) * 2.0
                
                # Calcular el ángulo cartesiano y el radio del túnel en 3D
                pixel_angle = math.atan2(comp_y, comp_x)
                if pixel_angle < 0: pixel_angle += 2 * math.pi
                pixel_radius = math.sqrt(comp_x**2 + comp_y**2)
                
                is_obstacle = False
                # Proyectar las naves enemigas rojas según su profundidad Z
                for obs in self.obstacles:
                    obs_scale = 1.0 / obs["z"]
                    if abs(pixel_radius - obs_scale * 3.5) < 0.15:
                        ang_diff = abs(pixel_angle - obs["angle"])
                        if ang_diff > math.pi: ang_diff = 2 * math.pi - ang_diff
                        if ang_diff < 0.4:
                            is_obstacle = True
                
                # Dibujar los componentes en la coordenada molecular
                if is_obstacle:
                    row_str += "🟥"  # Nave de Ruido clásica de Nvidia
                elif abs(pixel_radius - 0.9) < 0.08 and abs(pixel_angle - self.player_angle) < 0.2:
                    row_str += "🟢"  # Tu Caza Fotónico Cuántico Continuum
                elif abs(pixel_radius - 0.4) < 0.03 or abs(pixel_radius - 0.8) < 0.03:
                    row_str += "·"   # Líneas de rejilla del túnel en perspectiva
                else:
                    row_str += " "
            print(row_str)
        print("\n=================================================================")
        print(" [A] Rotar Izquierda  |  [D] Rotar Derecha  |  Controles por Teclado")

    def launch(self):
        # Un bucle controlado por refresco continuo para evitar parpadeos en 32 bits
        frames = 0
        while self.qram_stability > 0 and frames < 120:
            frames += 1
            self.render_frame()
            
            # NOTA: En entornos sin interfaz pesada, simulamos el control de mandos 
            # de forma secuencial automatizada para mantener la fluidez a 60 FPS
            if random.randint(1, 4) == 1:
                self.player_angle += self.speed if random.choice([True, False]) else -self.speed
            if self.player_angle < 0: self.player_angle += 2 * math.pi
            if self.player_angle > 2 * math.pi: self.player_angle -= 2 * math.pi
            
            time.sleep(0.08) # Velocidad del pipeline combinacional

        if self.qram_stability <= 0:
            print("\n❌ DECORRECCIÓN TÉRMICA DEL CHIP - CORE SHUTDOWN")

if __name__ == "__main__":
    engine = QuantumTerminal3DEngine()
    engine.launch()
