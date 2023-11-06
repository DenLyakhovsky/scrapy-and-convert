import re

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def iteration(data, word):
    """
    Функція перебирає HTML клас data-productinfo та знаходить значення по ключу
    :param data: Масив даних, які потрібно перебрати
    :param word: Слово, яке потрібно знайти
    :return: Значення
    """
    for item in data.split():
        if word in item:
            pattern = rf'"{word}":"([^"]+)"'

            matches = re.search(pattern, item)

            if matches:
                at_value = matches.group(1)
                return at_value
            else:
                print(f"'{word}' не знайдено в рядку.")


def remove_symbols(word):
    """
    Функція видаляє зайві символи
    :param word: Передаємо слово або список, яке має зайві символи
    :return:
    """
    clean_list = []
    for i in word:
        clean_list.append({
            'options': i.strip('"')
        })

    return [i.get('options').strip('"') for i in clean_list]
