% Синхронизация с сигналом и отброс лишних нулей в массиве
signal = signal_with_noise;
golden_sequence = repmat(golden_sequence, 1, length(signal)/length(golden_sequence));
[~, pos] = max(conv(golden_sequence, signal));
synchronized_signal = signal(pos:pos+length_signal-1);

% Преобразование временных отсчетов в информацию и избавление от шума
cipher = synchronized_signal(1:N:end) > 0.5;

% Удаление последовательности Голда
cipher_without_gold = cipher(G+1:end)';

% Проверка CRC
crc_check = calculate_crc(cipher_without_gold');
disp(['CRC:', num2str(crc_check)]);
if any(crc_check)
    disp('Ошибка CRC');
else
    % Удаление CRC и декодирование битов информации в буквы
    word = cipher_without_gold(1:end-7);
    decoded_message = decode_binary_to_letters(word);
    decoded_text = '';
    for i = 1:length(decoded_message)
        if double(decoded_message(i)) > 65 && double(decoded_message(i)) < 90
            decoded_text = [decoded_text, ' '];
        end
        decoded_text = [decoded_text, decoded_message(i)];
    end
    disp(decoded_text(2:end));
end

function [result, G] = generate_gold_sequence()
    x = [1, 1, 1, 1, 0];
    y = [0, 1, 1, 0, 1];
    G = 31;
    result = zeros(1, G);
    for i = 1:G
        summator_x = xor(x(3), x(4));
        summator_y = xor(y(3), y(2));
        result(i) = xor(x(5), y(5));
        x = shift_right(x);
        y = shift_right(y);
        x(1) = summator_x;
        y(1) = summator_y;
    end
end

function decoded = decode_binary_to_letters(code)
    sim = '';
    decoded = [];
    j = 0;
    for i = code
        if j == 7
            decoded = [decoded, char(bin2dec(sim))];
            j = 0;
            sim = '';
        end
        sim = [sim, num2str(i)];
        j = j + 1;
    end
    decoded = [decoded, char(bin2dec(sim))];
end

function code = encode_text_to_binary(text)
    mas = [];
    for i = text
        if i ~= ' '
            mas = [mas, double(i)];
        end
    end

    code = [];
    for j = mas
        binary_representation = dec2bin(j);
        code = [code, str2num(binary_representation(3:end))];
    end
end

function plot_graph(data, title)
    bukashka = data;
    figure;
    plot(bukashka);
    title(title);
end

function result = calculate_crc(packet)
    divisor = [1, 0, 1, 0, 0, 1, 1, 1];
    remainder = 1:length(divisor);
    for i = 1:length(divisor) - 1
        remainder(i) = xor(packet(i + 1), divisor(i + 1));
    end
    remainder(end) = packet(end);

    for i = length(divisor) + 1:length(packet)
        if remainder(1) ~= 0
            for j = 1:length(divisor) - 1
                remainder(j) = xor(remainder(j + 1), divisor(j + 1));
            end
        else
            for j = 1:length(divisor) - 1
                remainder(j) = remainder(j + 1);
            end
        end
        remainder(end) = packet(i);
    end

    if remainder(1) ~= 0
        for j = 1:length(divisor)
            remainder(j) = xor(remainder(j), divisor(j));
        end
    end

    result = remainder(2:end);
end

function shifted_data = shift_right(data)
    temp = d
