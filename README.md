# Yandex Школа информационной безопасности
## Задача 5
Напишите программу, обрабатывающую приложенный журнал и выполняющую следующие функции (можно реализовать не полный набор функций. оценка за задание будет равна сумме баллов корректно работающих функций):

1. Поиск 5ти пользователей, сгенерировавших наибольшее количество запросов (1 балл)
2.	Поиск 5ти пользователей, отправивших наибольшее количество данных (2 балла)
3.	Поиск регулярных запросов (запросов выполняющихся периодически) по полю src_user (3 балла)
4.	Поиск регулярных запросов (запросов выполняющихся периодически) по полю src_ip (4 балла)
5.	Рассматривая события сетевого трафика как символы неизвестного языка, найти 5 наиболее устойчивых [N-грамм](https://ru.wikipedia.org/wiki/N-грамм) журнала событий (текста на неизвестном языке), где N=3-5. Тип символа задается квартетом user+src_port+dest_ip+dest_port (5 баллов)

## Запуск программы
```
task_5.py shkib.csv
```