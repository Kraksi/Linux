import schedule
import time
from scrape import scrape_all_books
from preprocess import preprocess_data

# Предобработка данных


# Основная функция сбора и обработки данных
def collect_and_save_data():

    #Cбор всех книг со всех страниц сайта
    print("Начало сбора данных...")
    books = scrape_all_books()
    print("Сбор данных завершён.")

    # Предобработка данных для загрузки в books_data.csv
    print("Начало предобработки данных...")
    data = preprocess_data(books)

    # Сохранение предобработанных данных в books_data.csv
    data.to_csv('books_data.csv', index=False)
    print("Данные сохранены в 'books_data.csv'.")


# Планирование задачи
schedule.every().day.at("19:00").do(collect_and_save_data)

# Зацикливание для работы планиролвщика задач
print("Программа запущена. Ожидание времени запуска (Каждый день в 19:00) ...")
while True:
    schedule.run_pending()
    time.sleep(1)
