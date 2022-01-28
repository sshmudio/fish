import requests


def send_info(bot_message):
    bot_token = '5040876149:AAHXU7Ro_6fmrpuZ-AB2lUcx_OGpQalvKBs'
    #Enter your telegram id
    bot_chatID = '0000000'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
