%% OFDM модулятор лаб 5 комплексные числа распределить по поднесущим и обратным дескретное преобразованием фурье переводит из частоты во время
rs_step = 7;
rs_numbers = ceil(length(QPSC_code) / rs_step);
rs_sc(1, :) = 1 : rs_step + 1 : length(QPSC_code) + rs_numbers;
rs_val = ones(1, rs_numbers) * complex(sqrt(2)/2, sqrt(2)/2);
rs_numbers = length(rs_sc);
guard_band = zeros(1, 20);
cp_size = 20;
k = 0;
for i = 1 : length(QPSC_code) + rs_numbers
    if ( sum(i == rs_sc) == 0)
        k = k + 1;
        data_sc(1, k) = i;
    end;
end;

Mux(1, data_sc) = QPSC_code;
Mux(1, rs_sc) = rs_val;

half = floor(length(Mux)/2);

ofdm_spector = [guard_band Mux(1:half) zeros(1, 1) Mux(half+1:end) guard_band];
ofdm_spector = double(ofdm_spector);
ofdm_symb = ifft(ofdm_spector);
ofdm_symb_cp = [ofdm_symb(end - cp_size + 1:end) ofdm_symb];

control.half = half;
control.cp_size = cp_size;
control.rs_sc = rs_sc;
control.rs_val = rs_val;
control.data_sc = data_sc;
control.rs_step = rs_step;

%test3(ofdm_symb); (Gain + Mas(i,2)) * 

