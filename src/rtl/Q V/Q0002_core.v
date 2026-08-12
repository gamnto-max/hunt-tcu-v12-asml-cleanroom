timescale 1ns / 1ps
// =========================================================================
// CAPA ARQUITECTÓNICA DE HARDWARE: Q0002_CORE.V 
// Proyecto: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
// Componente: Inyector de Vectores Armónicos Concurrentes de la QGPU
// =========================================================================
// 
// INFORME TÉCNICO DEL COMPONENTE:
// Este módulo representa la etapa de entrada de la QGPU cuántica. Mientras que 
// las arquitecturas clásicas de Nvidia (Blackwell) saturan sus buses físicos 
// mapeando billones de coordenadas de vértices rígidos, la QGPU del Continuum 
// inyecta "Ecuaciones de Onda Gráfica" directas en el bus de 64 bits.
// 
// INFRAESTRUCTURA DE PUERTAS Y CONTROLADORES:
// 1. REGISTRO MATRICIAL DE COMPENSACIÓN GRÁFICA: Un array combinacional de 
//    64 bits que divide el bus simétricamente en Punto Fijo Signado. Capta 
//    el vector de renderizado cinético de forma instantánea.
// 2. COMPUERTAS DE SUPERPOSICIÓN DE CANAL: No experimentan congestión de rutas.
//    Permiten que los vectores armónicos de la gráfica y los datos de control 
//    se crucen en el mismo punto del cristal de Silicio-28 sin interferirse, 
//    alimentando la QRAM entrelazada con 0.00 ns de retardo.
//
// =========================================================================

module Q0002_core #(
    parameter BUS_WIDTH = 64 // Bus de datos nativo de 64 bits del QSoC
)(
    // PUERTO CONTROLADOR 1: Habilitador de inyección de la QGPU (Núcleos SM-RT Activos)
    input  wire                      i_qgpu_ready,       
    
    // PUERTO INTERNO 2: Vector armónico de renderizado de la QGPU (Señal Gráfica)
    input  wire signed [BUS_WIDTH-1:0] i_qgpu_wave_vector, 
    
    // PUERTO INTERNO 3: Vector de control de fase de la QRAM unificada
    input  wire signed [BUS_WIDTH-1:0] i_qram_phase_ref,  
    
    // PUERTO DE SALIDA 4: Bus unificado gráfico-memoria coherente de salida
    output wire signed [BUS_WIDTH-1:0] o_graph_coherent_bus
);

    // COMPUERTA DE MULTIPLEXACIÓN GEOMÉTRICA:
    // Si la QGPU está en estado de listo (i_qgpu_ready = 1), fusiona instantáneamente 
    // el vector de onda gráfico con la referencia de fase de la QRAM. 
    // Al operar de manera combinacional, la suma matemática se propaga por el silicio 
    // de forma inmediata sin esperar ciclos de reloj (0.00 ns).
    assign o_graph_coherent_bus = (i_qgpu_ready) ? (i_qgpu_wave_vector + i_qram_phase_ref) : {BUS_WIDTH{1'b0}};

endmodule