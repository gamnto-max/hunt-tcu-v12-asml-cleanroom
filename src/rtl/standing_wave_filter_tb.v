timescale 1ns / 1ps
module standing_wave_filter_tb;
    reg signed [15:0] s; reg signed [15:0] n; wire signed [15:0] o;
    standing_wave_filter uut (.i_quantum_signal(s), .i_stationary_noise(n), .o_filtered_signal(o));
    initial begin
        s = 16'h0140; n = 16'h0073; #1;
        $display('=== SIMULACION COMPILADA (HUNT-TCU v1.2) ===');
        $display('Output Vector: %f', o/256.0);
        $finish;
    end
endmodule