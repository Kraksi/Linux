import pandas as pd

# Функция предобработки данных
def preprocess_data(data):

    # Создание дата фрейма из полученных книг
    df = pd.DataFrame(data)
    is_null(df)
    delete_duplicates(df)

    # Вывод общей статистики
    print("Общее количество книг:", len(df))
    print("Основная статистика по числовым данным:")
    print(df.describe(include='all'))

    return df


# Функция проверки на пропуски
def is_null(df):

    if df.isnull().values.any():
        df.fillna('Неизвестно', inplace=True)
        print("Заполнены пропуски значением -> 'Неизвестно'.")


# Функция удаления дубликатов
def delete_duplicates(df):

    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_count - len(df)
    print(f"Удалено дубликатов: {duplicates_removed}")