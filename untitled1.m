% Инициализация переменных
length = 31;
x = [1, 0, 0, 0, 0];
y = [0, 0, 0, 1, 0];
x2 = [0, 1, 0, 0, 0];
y2 = [1, 1, 0, 0, 0];
golden = zeros(1, length, 'single');
golden2 = zeros(1, length, 'single');

% Основной цикл
for i = 1:length
    % Вычисление XOR для последних битов x и y, результат сохраняется в golden
    golden(i) = xor(x(5), y(5));
    
    % Вычисление XOR для последних битов x2 и y2, результат сохраняется в golden2
    golden2(i) = xor(x2(5), y2(5));
    
    % Сохранение битов для следующей итерации
    savex = xor(x(3), x(4));
    savey = xor(y(2), y(3));
    savex2 = xor(x2(3), x2(4));
    savey2 = xor(y2(2), y2(3));
    
    % Циклический сдвиг битов вправо
    for j = 5:-1:2
        x(j) = x(j - 1);
        y(j) = y(j - 1);
        x2(j) = x2(j - 1);
        y2(j) = y2(j - 1);
    end
    
    % Присваивание новых значений для первого бита
    x(1) = savex;
    y(1) = savey;
    x2(1) = savex2;
    y2(1) = savey2;
end
[autocor, lag0] = xcorr(golden, golden);
[vzcor, lag0] = xcorr(golden, golden2);
% Вычисление автокорреляции между golden и golden
lag1 = sqrt(xcorr(golden, golden));
lag2 = sqrt(xcorr(golden2, golden2));
%flipped = flip(lag2, 2);

lag = xcorr(golden, golden2) / lag1 * lag2;

% Вывод графика автокорреляции
plot(lag);
plot(lag0);
% Вычисление автокорреляции между golden и golden2
%[vzcor, lag] = xcorr(golden, golden2);

% Вывод значения автокорреляции для лага 31
disp(vzcor(31));