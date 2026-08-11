module standing_wave_filter #(parameter DATA_WIDTH = 16)(
    input wire signed [DATA_WIDTH-1:0] i_quantum_signal,
    input wire signed [DATA_WIDTH-1:0] i_stationary_noise,
    output wire signed [DATA_WIDTH-1:0] o_filtered_signal
);
    wire signed [DATA_WIDTH-1:0] w_anti_node_vector;
    assign w_anti_node_vector = ~i_stationary_noise + 1'b1;
    assign o_filtered_signal = i_quantum_signal + i_stationary_noise + w_anti_node_vector;
endmodule