t = (0:100-1)/100;
pi = 3.14;

s1 = cos(2 * pi * t * 15);
s2 = cos(2 * pi * t * 19);
s3 = cos(2 * pi * t * 31);
a = 3 * s1 + 4 * s2 + s3;
b = s1 + 0.25 * s2;

corsa = sum(s1.*a);
corsb = sum(s1.*b);
disp("Корреляция a s1")
disp(corsa);
disp("Корреляция b s1")
disp(corsb);

multa = 0;
multb = 0;
mults = 0;
for n = 1:100
    mults = s1(n) * s1(n) + mults;
    multa = a(n) * a(n) + multa;
    multb = b(n) * b(n) + multb;
end
cornormsa = corsa / sqrt(mults * multa);
cornormsb = corsb / sqrt(mults * multb);
disp("Нормализованая корреляция a s1")
disp(cornormsa);
disp("Нормализованая корреляция b s1")
disp(cornormsb);

a = [0.3 0.2 -0.1 4.2 -2 1.5 0];
b = [0.3 4 -2.2 1.6 0.1 0.1 0.2];
corab = sum(a.*b);
disp("Корреляция a b")
disp(corab);
figure;
subplot(5, 1, 1);
plot(a);
title("a = [0.3 0.2 -0.1 4.2 -2 1.5 0]")
subplot(5, 1, 2);
plot(b);
title("b = [0.3 4 -2.2 1.6 0.1 0.1 0.2]")
maxsdvig = 0;
maxznach = corab;
cormas = zeros(1, length(a));
cormas(1) = corab;
for shift = 2:(length(cormas))
    save1 = b(1);
    b(1) = b(length(b));
    for dvij = 2:length(b)
        save2 = b(dvij);
        b(dvij) = save1;
        save1 = save2;
    end
    corab = sum(a.*b);
    if corab > maxznach
        maxznach = corab;
        maxsdvig = shift - 1;
    end
    cormas(shift) = corab;
end
for i = 0:maxsdvig
    save1 = b(1);
    b(1) = b(length(b));
    for dvij = 2:length(b)
        save2 = b(dvij);
        b(dvij) = save1;
        save1 = save2;
    end
end
disp("Максимальная корреляция");
disp(maxznach);
disp("При сдвиге");
disp(maxsdvig);
subplot(4, 1, 3);
plot(b);
title("b со сдвигом")
subplot(4, 1, 4);
plot(cormas);
title("Корреляция со сдвигом b")