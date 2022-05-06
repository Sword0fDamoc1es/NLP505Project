import json
import re
import pandas as pd
import requests


def LAT2AR(word):
    path = f"https://api.yamli.com/transliterate.ashx?word={word}&tool=api&account_id=000006&prot=https:&hostname=www" \
           f".yamli.com&path=/&build=5515 "
    response = requests.get(path)
    html = response.content
    try:
        newWord = json.loads(html.decode("utf-8"))["r"].split("|")[0].rsplit('/', 1)[0]
    except:
        return word
    return word if newWord == "" else newWord


def translate(text):
    newtext = []
    text = re.sub(r"[,.;@/#?\!&$]+\ *", " ", text)
    text = text.split(' ')
    try:
        for i in range(len(text)):
            newtext.append(LAT2AR(text[i].strip()))
    except:
        newtext.append(LAT2AR(text[i].strip()))

    return ' '.join(newtext)


if __name__ == '__main__':
    df = pd.read_csv('data/Arabizi/Train.csv', delimiter=',', header=0)
    translated = []
    for line in df['text']:
        translated.append(translate(line))
    new_df = pd.DataFrame(data={'text': translated, 'label': df['label']})
    new_df.to_csv("train_arabic.csv")
