#include <gtk/gtk.h>

// Функция, которая вызывается при нажатии на кнопку
void on_button_clicked(GtkWidget *widget, gpointer data) {
    gtk_widget_destroy(GTK_WIDGET(data)); // Закрываем окно
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *button;

    gtk_init(&argc, &argv); // Инициализируем GTK+

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL); // Создаем новое окно верхнего уровня
    gtk_window_set_title(GTK_WINDOW(window), "Hello World"); // Устанавливаем заголовок окна
    gtk_window_set_default_size(GTK_WINDOW(window), 200, 200); // Устанавливаем размер окна

    button = gtk_button_new_with_label("Hello World"); // Создаем кнопку с надписью "Hello World"
    g_signal_connect(button, "clicked", G_CALLBACK(on_button_clicked), window); // Подключаем сигнал к кнопке

    gtk_container_add(GTK_CONTAINER(window), button); // Добавляем кнопку в окно

    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL); // Подключаем сигнал к окну, чтобы завершить GTK+ при закрытии окна

    gtk_widget_show_all(window); // Отображаем все элементы окна

    gtk_main(); // Запускаем главный цикл GTK+

    return 0;
}