import numpy as np
class HuntMatrixProcessor:
    def __init__(self):
        self.scale = 256
    def execute_filter(self, s, n):
        i_s = int(np.round(s * self.scale)) & 0xFFFF
        i_n = int(np.round(n * self.scale)) & 0xFFFF
        w_a = (~i_n + 1) & 0xFFFF
        o_f = (i_s + i_n + w_a) & 0xFFFF
        return o_f / self.scale
if __name__ == '__main__':
    print('--- INICIANDO 0003_APP.PY ---')
    p = HuntMatrixProcessor()
    print('Output Node 0:', p.execute_filter(1.25, 0.45))