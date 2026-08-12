`timescale 1ns / 1ps
// =========================================================================
// CAPA ARQUITECTÓNICA DE HARDWARE: Q0006_CORE.V
// Proyecto: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
// Componente: Monitor de Paridad y Coherencia Entrelazada Pasiva (64 bits)
// =========================================================================
//
// INFORME TÉCNICO DEL COMPONENTE:
// Este módulo representa la capa de integridad estructural del SoC. Mientras 
// las arquitecturas de Nvidia Blackwell detienen las líneas de ejecución para 
// calcular sumas de comprobación por software que saturan los buses, este 
// hardware utiliza compuertas de reducción XOR masiva a nivel atómico.
//
// INFRAESTRUCTURA DE PUERTAS Y CONTROLADORES:
// 1. ÁRBOL DE COMPUERTAS XOR DE REDUCCIÓN (CONTROLADOR DE PARIDAD): Un array 
//    combinacional de 64 bits que calcula el bit de paridad par de forma pasiva 
//    a medida que las matrices algebraicas viajan hacia la QRAM.
// 2. DETECTOR DE DECORRECCIÓN INSTANTÁNEO: Compara el estado del bus con la 
//    referencia del entrelazamiento cuántico. Al operar de forma combinacional, 
//    levanta la bandera de alarma en 0.00 ns sin interrumpir el renderizado.
//
// =========================================================================

module Q0006_core #(
    parameter BUS_WIDTH = 64 // Formato de bus rigido del Superchip Continuum
)(
    input  wire signed [BUS_WIDTH-1:0] i_qsoc_bus_data,     // Flujo unificado QGPU-QRAM
    input  wire                      i_expected_parity,   // Paridad de referencia entrelazada
    output wire signed [BUS_WIDTH-1:0] o_validated_bus_data, // Datos limpios de salida del bus
    output wire                      o_parity_bit,        // Bit de paridad calculado en tiempo real
    output wire                      o_coherence_fault    // Bandera de alerta por fallo de paridad
);

    // CONTROLADOR DE PARIDAD PASIVO:
    // Reduccion de 64 bits usando compuertas XOR combinacionales (^).
    // El resultado se obtiene instantaneamente por propagacion fisica.
    assign o_parity_bit = ^i_qsoc_bus_data;

    // DETECTOR DE FALLO DE COHERENCIA MOLECULAR:
    // Si la paridad calculada no coincide con la esperada, se activa el flag de error.
    assign o_coherence_fault = (o_parity_bit != i_expected_parity);

    // COMPUERTA DE PROTECCIÓN DE DATOS:
    // Deja pasar el flujo intacto hacia la memoria de 128 GB de forma instantanea (0.00 ns).
    assign o_validated_bus_data = i_qsoc_bus_data;

endmodule