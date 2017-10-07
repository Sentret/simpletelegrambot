# import json
# import requests
# TELEGRAM_API_TOKEN = '477664984:AAE3DMVARlsk-L5loYPNG4J6Jcm8D2EYsvI'
# YANDEX_TRANSLATE_API_TOKEN ='trnsl.1.1.20171007T151418Z.c518155b55576f48.b05b24f6c5542b4f63acc2857d3f3bf44202cd62'


# def detect_language(word):

#     params = {
#     'key':YANDEX_TRANSLATE_API_TOKEN ,
#     'text':word

#     }

#     response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/detect',params)
#     detection = json.loads(response.text)
#     return detection['lang']


# def translate(word):
#     lang = detect_language(word)

#     params = {
#         'key':YANDEX_TRANSLATE_API_TOKEN,
#         'text':word,
#         'lang':lang+'-ru',
#      }

#     response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',params)
#     detection = response.json()
#     return detection['text']


# def send_answer(chatid, message):
#     answer_args = {
#   'chat_id':chatid,
#   'text':translate(message)
# }

#     print((chatid,message))
#     requests.get('https://api.telegram.org/bot%s/sendMessage'%TELEGRAM_API_TOKEN, answer_args)


# send_answer(341288157, 'hi')