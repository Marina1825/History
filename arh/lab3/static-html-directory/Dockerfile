# Используем официальный образ nginx
FROM nginx:latest
RUN apt-get update && apt-get install -y apache2-utils
# Копируем наш конфигурационный файл в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем наш статический сайт в контейнер
COPY static-html-directory /usr/share/nginx/html

# Экспортируем порт 80
EXPOSE 80

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
