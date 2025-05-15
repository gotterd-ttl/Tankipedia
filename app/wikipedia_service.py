import wikipediaapi
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Словарь соответствий русских названий танков и их точных страниц в Википедии
TANK_NAME_MAPPING = {
    "Тигр": "Тигр (танк)",
    "Т-34": "Т-34",
    "ИС-2": "ИС-2",
    "Пантера": "Пантера (танк)",
    "Маус": "Маус (танк)",  # Исправлено, чтобы показывать информацию о танке, а не о сказке
    # Добавьте другие танки по необходимости
}

def get_tank_info(tank_name):
    """
    Получить краткую информацию о танке из Wikipedia API.
    :param tank_name: Название танка (на русском).
    :return: Словарь с данными о танке или сообщением об ошибке.
    """
    # Переводим название танка на уточнённое название страницы
    localized_name = TANK_NAME_MAPPING.get(tank_name, tank_name)

    # Логируем попытку поиска
    logger.info(f"Ищем информацию о танке: {localized_name}")

    # Инициализация Wikipedia API для русского языка
    wiki_wiki = wikipediaapi.Wikipedia('ru')  # Используем русскую Wikipedia
    page = wiki_wiki.page(localized_name)

    # Проверяем, существует ли страница
    if page.exists():
        logger.info(f"Информация о танке '{localized_name}' найдена.")
        return {
            "title": page.title,
            "summary": page.summary[:500],  # Обрезаем описание до 500 символов
            "url": page.fullurl
        }
    else:
        logger.warning(f"Информация о танке '{localized_name}' не найдена.")
        return {
            "error": f"Информация о танке '{tank_name}' не найдена."
        }
