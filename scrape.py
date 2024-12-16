import requests
from bs4 import BeautifulSoup

# URL сайта для сбора данных
BASE_URL = "http://books.toscrape.com/catalogue/"


# Функция для извлечения информации о книге
def scrape_book(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # Название книги
        title = soup.find("h1").text.strip()
        # Цена
        price = soup.find(class_="price_color").text.strip().replace('Â', '')
        # Рейтинг
        rating = soup.find(class_="star-rating")['class'][1]
        # Количество оставшихся книг
        stock = soup.find(class_="instock availability").text.strip()
        # Описание
        description = soup.select_one("#product_description ~ p")
        description = description.text.strip() if description else "No description"
        # Дополнительные характеристики
        product_info = {}
        for row in soup.select("table.table.table-striped tr"):
            key = row.find("th").text.strip()
            value = row.find("td").text.strip()
            product_info[key] = value

        return {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Stock': stock,
            'Description': description,
            **product_info
        }

    except Exception as e:
        print(f"Ошибка при обработке {book_url}: {e}")
        return None


# Функция для извлечения данных о книгах с одной страницы
def scrape_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    # Сбор ссылок на книги с текущей страницы
    book_links = [BASE_URL + link['href'] for link in soup.select("h3 > a")]
    for book_url in book_links:
        book_data = scrape_book(book_url)
        if book_data:
            books.append(book_data)

    return books


# Функция для извлечения данных со всех страниц сайта
def scrape_all_books():

    page_url = BASE_URL + "page-1.html"
    all_books = []

    while True:
        print(f"Сбор данных с {page_url}...")
        books = scrape_page(page_url)
        all_books.extend(books)

        # Переход на следующую страницу
        soup = BeautifulSoup(requests.get(page_url).text, 'html.parser')
        next_page = soup.select_one("li.next > a")
        if next_page:
            page_url = BASE_URL + next_page['href']
        else:
            break

    return all_books
