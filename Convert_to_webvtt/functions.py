import re


def iteration(text_to_iterate):
    """
    Функція, яка перебирає речення. Використовується, щоб порахувати к-сть слів у тексті.
    :param text_to_iterate: Текст, який хочемо перебрати
    :return:
    """
    list_word = []
    list_sentence = []
    for i in text_to_iterate:
        list_sentence.append(i)
        for m in i.split():
            list_word.append(m)

    return list_word


def calculate_speech_time(text):
    """
    Функція, перебирає текст, який ми передали і вираховує час вимови
    :param text:
    :return: Повертає словник з часом
    """

    # Середня швидкість вимови (слова на секунду)
    speech_speed = 2.5

    # Розрахунок часу вимови (у секундах)
    speech_time_seconds = len(iteration(text)) / speech_speed
    # Перетворення часу в хвилини та секунди
    minutes = int(speech_time_seconds // 60)
    seconds = int(speech_time_seconds % 60)

    # return f"Час вимови: {minutes} хвилин {seconds} секунд", minutes, seconds
    return {'minutes': minutes, 'seconds': seconds}


def convert_to_replica(text):
    """
    Конвертує 'сирий' текст на репліки
    :param text:
    :return: Повертається список, з готовими репліками
    """
    replica = re.split(r'[\n]', text)

    # Створити список для зберігання реплік та тексту
    replica_data = []

    # Ітерувати через репліки і додавати їх у список
    for r in replica:
        replica_data.append(r)

    person_data = []
    # Вивести список із репліками та текстом
    for data in replica_data:
        person_data.append(data)

    return person_data


def sentence_and_time_result(file_content):
    """
    Створює фінальний результат з реченням та часом
    :param file_content:
    :return: Повертається словник, в якому є речення та час вимови
    """
    data = convert_to_replica(file_content)

    final_subtitle = []
    for sentence in data:
        pronunciation_time = calculate_speech_time(sentence)

        final_subtitle.append({
            'sentence': sentence,
            'time': f"{pronunciation_time.get('minutes')}хв:{pronunciation_time.get('seconds')}с",
        })

    return final_subtitle
