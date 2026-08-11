`timescale 1ns / 1ps

module standing_wave_filter #(
    parameter DATA_WIDTH = 16
)(
    input  wire signed [DATA_WIDTH-1:0] i_quantum_signal,
    input  wire signed [DATA_WIDTH-1:0] i_stationary_noise,
    output wire signed [DATA_WIDTH-1:0] o_filtered_signal
);
    wire signed [DATA_WIDTH-1:0] w_anti_node_vector;
    assign w_anti_node_vector = ~i_stationary_noise + 1'b1;
    assign o_filtered_signal = i_quantum_signal + i_stationary_noise + w_anti_node_vector;
endmodule

module standing_wave_filter_tb;
    reg signed [15:0] s; reg signed [15:0] n; wire signed [15:0] o;
    standing_wave_filter uut (.i_quantum_signal(s), .i_stationary_noise(n), .o_filtered_signal(o));
    initial begin
        s = 16'h0140; n = 16'h0073; #1;
        $display(" ");
        $display("=== COMIENZA SIMULACION DE HARDWARE (HUNT-TCU v1.2) ===");
        $display("Resultado en Bus de Salida : %f", o / 256.0);
        $display("=======================================================");
        $finish;
    end
endmodule
