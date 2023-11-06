from functions import sentence_and_time_result

"""
Це основний файл, який потрібно запускати, 
functions.py -- функції, які використовуються в функції convert_to_webvtt
"""

# Дістаємо текст, який потрібно редагувати
with open('DATA_BEFORE_transcript.txt', 'r') as file:
    content = file.read()[33:]


def convert_to_webvtt(sentence_and_time):
    """
    Ф-ція, яка збирає дані з sentence_and_time_result, та створює файл WebVTT
    :param sentence_and_time:
    :return: Створює файл
    """

    data = sentence_and_time_result(file_content=sentence_and_time)
    webvtt = "WEBVTT\n\n"

    final = []
    for v in data:
        final.append({
            'start_time': '00:00:00',
            'end_time': v.get('time'),
            'text': v.get('sentence'),
        })

    for i, subtitle in enumerate(final, start=1):
        webvtt += f"{i}\n"
        start_time = subtitle["start_time"]
        end_time = subtitle["end_time"]
        webvtt += f"{start_time} --> {end_time}\n"
        webvtt += subtitle["text"] + "\n\n"

    with open("output.vtt", "w", encoding="utf-8") as vtt_file:
        vtt_file.write(webvtt)


convert_to_webvtt(content)
