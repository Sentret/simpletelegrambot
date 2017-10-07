import json
import requests
TELEGRAM_API_TOKEN = '477664984:AAE3DMVARlsk-L5loYPNG4J6Jcm8D2EYsvI'

req = json.loads( b'{"update_id":820635093,\n"message":{"message_id":13,"from":{"id":341288157,"is_bot":false,"first_name":"Eugene","last_name":"Andrianov","language_code":"ru"},"chat":{"id":341288157,"first_name":"Eugene","last_name":"Andrianov","type":"private"},"date":1507398412,"text":"hi"}}'.decode("utf-8"))
print(req['message']['text'])
print(req['message']['chat']['id'])


answer_args = {
  'chat_id':req['message']['chat']['id'],
  'text':'hi'
}
requests.get('https://api.telegram.org/bot%s/sendMessage'%TELEGRAM_API_TOKEN,answer_args)
detection = json.loads(detect_response.text)


print(detection)