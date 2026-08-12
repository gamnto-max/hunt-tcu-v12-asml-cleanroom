// src/sim/quantum_game.c
// Project: HUNT-QSoC "Continuum" v1.2 (Gaming Evolution)
// Core: Native 32-bit C-Engine for Quantum SoC & QRAM Emulation

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

#define WIDTH 60
#define HEIGHT 12

int main() {
    double qram_stability = 128.0;
    int score = 0;
    int player_x = 30;
    int enemy_x = 15;
    double enemy_y = 0.0;
    int laser_active = 0;
    int cycle = 0;

    // Bucle cuántico principal acelerado por hardware
    while (qram_stability > 0 && cycle < 100) {
        cycle++;
        
        // Limpiar la pantalla de la consola de forma nativa en Windows
        system("cls");

        // 1. ACTUALIZAR PIPELINE EN CALIENTE (Caída del Ruido de Nvidia)
        enemy_y += 0.8;
        if (enemy_y >= HEIGHT) {
            enemy_y = 0;
            enemy_x = (rand() % (WIDTH - 10)) + 5;
            qram_stability -= 15.0; // El ruido impacta si no se intercepta
        }

        // 2. SIMULACIÓN DE MANDOS SECUENCIALES (Teclas Virtuales)
        if (cycle % 3 == 0) {
            player_x += (rand() % 3) - 1; // Movimiento fluido simulado
            laser_active = 1;             // Disparar Rayo Antinodo Hunt
        } else {
            laser_active = 0;
        }

        // Delimitar fronteras físicas del chip
        if (player_x < 5) player_x = 5;
        if (player_x > WIDTH - 5) player_x = WIDTH - 5;

        // 3. DETECTOR DE INTERCEPCIÓN (Teorema de Hunt a 0.00 ns)
        if (laser_active && player_x == enemy_x && (int)enemy_y > 4) {
            qram_stability += 20.0;
            if (qram_stability > 256.0) qram_stability = 256.0;
            score += 100;
            enemy_y = 0;
            enemy_x = (rand() % (WIDTH - 10)) + 5;
            Beep(880, 50); // Sonido físico: Pitido de plasma por el altavoz de la laptop
        }

        // 4. RENDERIZADO TELEMÉTRICO CENTRADO EN LA PANTALLA
        printf("==============================================================\n");
        printf("   🔱 CONTINUUM SoC v1.2 -- MOTOR DE COMPILACIÓN NATIVO C     \n");
        printf("==============================================================\n");
        printf(" QRAM STABILITY: %.1f GB | LATENCY: 0.00 ns | MARCADOR: %d\n", qram_stability, score);
        printf("==============================================================\n\n");

        // Dibujar la matriz del túnel de Silicio-28
        for (int y = 0; y < HEIGHT; y++) {
            printf("  ");
            for (int x = 0; x < WIDTH; x++) {
                if (laser_active && x == player_x && y < HEIGHT - 2) {
                    printf("|"); // Rayo Láser de Neón continuo azul
                } else if (x == player_x && y == HEIGHT - 2) {
                    printf("O"); // Tu Caza Fotónico Cuántico Verde (🟢)
                } else if (x == enemy_x && y == (int)enemy_y) {
                    /*X*/; // Nave de Ruido clásica de Nvidia (🟥)
                    printf("X");
                } else if (y == 3 || y == 8) {
                    printf("."); // Rejillas del bus combinacional
                } else {
                    printf(" ");
                }
            }
            printf("\n");
        }
        
        Sleep(70); // Velocidad del refresco cinético
    }

    if (qram_stability <= 0) {
        printf("\n❌ DECORRECCIÓN TÉRMICA DEL CHIP - INSTABILIDAD DE BUS\n");
    } else {
        printf("\n✅ SECUENCIA DE CERTIFICACIÓN LOGRADA CON ÉXITO ANTE ASML\n");
    }
    return 0;
}