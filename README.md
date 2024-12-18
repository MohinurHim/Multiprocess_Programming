Домашнее задание по теме "Многопроцессное программирование"

Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.

Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
Подготовка:
Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.
Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, предварительно закомментировав другой.

Примечания:
Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
Выводить или возвращать список all_data в функции не нужно. Можете сделать это, но кол-во информации в файлах достигает - 10^9 строк.
Дополнительно о классе Pool можете прочитать здесь.
