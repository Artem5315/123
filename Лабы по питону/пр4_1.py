import re

# открываем файл с исходной речью для чтения
with open("speech.txt", "r") as f:
    speech = f.read()

# удаляем все вхождения слова "короче" независимо от регистра и формы
clean_speech = re.sub(r'\bкороч[е|к|а|у]?\b', '', speech, flags=re.IGNORECASE)

# открываем файл для записи очищенной речи
with open("clean_speech.txt", "w") as f:
    f.write(clean_speech)
