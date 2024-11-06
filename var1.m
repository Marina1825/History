% Строка символов
letters = 'Buyanova Marina';

% Преобразование букв в коды ASCII
ascii_codes = double(letters);

% Вывод результата
disp(ascii_codes);
decimal = 66;
binary = '';
while decimal > 0
    binary = [num2str(mod(decimal, 2)), binary]; % Добавляем остаток от деления на 2 в начало строки
    decimal = floor(decimal / 2); % Делим нацело на 2
end
disp(binary);
% Декодирование чисел в символы ASCII
letters = char(ascii_codes);

% Вывод результата
disp(letters);