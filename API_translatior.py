import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}'.format(to_lang)
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    translation = ''.join(json_['text'])

    return response, translation

if __name__ == '__main__':
    print(translate_it('sea', 'en'))
