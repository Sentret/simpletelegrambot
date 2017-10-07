import requests
import json
import asyncio
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
import os
TELEGRAM_API_TOKEN = '477664984:AAE3DMVARlsk-L5loYPNG4J6Jcm8D2EYsvI'
YANDEX_TRANSLATE_API_TOKEN ='trnsl.1.1.20171007T151418Z.c518155b55576f48.b05b24f6c5542b4f63acc2857d3f3bf44202cd62'


def detect_language(word):

    params = {
    'key':YANDEX_TRANSLATE_API_TOKEN ,
    'text':word

    }

    response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/detect',params)
    detection = json.loads(response.text)
    return detection['lang']


def translate(word):
    lang = detect_language(word)

    params = {
        'key':YANDEX_TRANSLATE_API_TOKEN,
        'text':word,
        'lang':lang+'-ru',
     }

    response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',params)
    detection = response.json()
    return detection


def send_answer(chatid, message):
    answer_args = {
  'chat_id':str(chatid),
  'text':translate(message)
}

    print((chatid,message))
    requests.get('https://api.telegram.org/bot%s/sendMessage'%TELEGRAM_API_TOKEN, answer_args)












# detect_response = requests.get('https://api.telegram.org/bot%s/Update'%TELEGRAM_API_TOKEN)
# print(detect_response.text)

# answer_args = {
#   'chat_id':'341288157',
#   'text':'hi'
# }
# requests.get('https://api.telegram.org/bot%s/sendMessage'%TELEGRAM_API_TOKEN,answer_args)
# detection = json.loads(detect_response.text)


# print(detection)



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", ClientHandler),
            (r'/telegram/'+TELEGRAM_API_TOKEN, TelegramHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


class ClientHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        
        # response =  translate(word)      
        self.write('hello')


class TelegramHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def post(self):
        
        # response =  translate(word)
        req = json.loads( self.request.body.decode("utf-8"))
        
        chatid = req['message']['chat']['id']
        message = req['message']['text']


        send_answer(chatid, message)
        
        
        
def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    PORT = os.environ.get('PORT', 5000)
    print("serving at port", PORT)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
