import time
import schedule
import requests
import random
url = "https://api.telegram.org/bot1158981508:AAHC4QQr3MybLrSrmJRG1NwsDBLrIKZb70Q/"
bot_token = '1158981508:AAHC4QQr3MybLrSrmJRG1NwsDBLrIKZb70Q'
bot_chatIDs = [
    ('1214863553'),
    ('-492168190'),
    ('-470665183'),
    ('861886075'),
    ('712481525'),
    ('771649055')
]
def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()
def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id
def telegram_bot_sendtext(bot_message, bot_chatID):
    global bot_token
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
def report():
    global bot_token
    global bot_chatIDs
    my_message1 = [
        ("Good morning!1!1!1!1! An awesome day awaits you!"),
        ("RISE AND SHINE!1!1!1!1! (Please don't; it's midnight!) But I meant good morning!1!1!1!1!"),
        ("Good morning!1!1!1!1! You're no doubt going to have a great day today!"),
        ("Good morning!1!1!1!1! Wishing you a day of joy and happiness! Well I mean you are going to get such a day anyway:)"),
        ("A very warm good morning!1!1!1!1! Have a beautiful and blissful day!"),
        ("Sending positive good morning vibes! Have a GREAT GREAT MORNING!1!1!1!1!"),
    ]
    my_message2 = [
        ("RISE AND SHINE!1!1!1!1! Or if you are already awake, good morning everyone!1!1!1!1!"),
        ("Good morning!1!1!1!1! Y'all are no doubt going to have a great day today, maybe even the best day ever!"),
        ("Good morning!1!1!1!1! Wishing everyone a day of joy and happiness! Well I mean y'all are going to get such a day anyway:)"),
        ("A very warm good morning everyone!1!1!1!1! Have a beautiful and blissful day!"),
        ("Sending positive good morning vibes! Have a GREAT GREAT MORNING ev'ryone!1!1!1!1! And thanks for being great friends!"),
    ]
    for x in bot_chatIDs:
        if x[0]=='-':
            telegram_bot_sendtext(random.choice(my_message2),x)
        else:
            telegram_bot_sendtext(random.choice(my_message1),x)
        lucky=random.randint(0, 4)
        if lucky==0:
            telegram_bot_sendtext("And to wish you unlimited luck today, here's a good morning gif!", x)
        elif lucky==1:
            telegram_bot_sendtext("And today, you're going to be very happy as a good morning image is here waiting for you!", x)
schedule.every().day.at("09:00").do(report)
def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           telegram_bot_sendtext("Greetings! I'm Mornin' From Callie, a bot which wishes you good morning at 6.30 am, and hopefully wakes you up! Well, it's a good habit to rise and shine early anyway.", get_chat_id(last_update(get_updates_json(url))))
           update_id += 1
    schedule.run_pending()
    time.sleep(1)     
if __name__ == '__main__':
    main()
