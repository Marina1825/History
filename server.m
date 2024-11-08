server = tcpserver("0.0.0.0", 2000);
% Устанавливаем обработчик события для получения данных
server.configureCallback("byte", 1, @readData);

% Бесконечный цикл для поддержания работы сервера
disp('Сервер запущен и ожидает подключений...');
while true
    pause(1);  % Пауза для снижения нагрузки на процессор
end

% Функция обработки полученных данных
function readData(src, ~)
    % Читаем данные из буфера сервера
    data = read(src, src.BytesAvailable, "uint8");
    
    % Преобразуем данные в строку
    dataStr = char(data');
    
    % Выводим информацию о полученных данных
    disp("Получены данные:");
    disp(dataStr);
end
