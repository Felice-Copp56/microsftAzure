import datetime
import logging
import requests
from bs4 import BeautifulSoup
import telegram
from telegram.error import TelegramError
import logging
import datetime
import azure.functions as func


BOT_TOKEN = '6569717002:AAFuVM404UTWXFNroEbDHEE1shPm15Jyqoc'
CHANNEL_ID= '@paddockpassionef1'
ARCHIVE_FILE = 'archivio_notizie.txt'  # Nome del file di archiviazione



def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    logging.info('Dio merda sono partito')
    sendNews()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


def sendNews():
    logging.info('chiamata')
    bot = telegram.Bot(token=BOT_TOKEN)
    

    # Carica l'archivio delle notizie già pubblicate
    try:
        with open(ARCHIVE_FILE, 'r') as file:
            news_archive = set(line.strip() for line in file)
    except FileNotFoundError:
        news_archive = set()
    api_url = "https://it.motorsport.com/f1/news/"
    response = requests.get(api_url)
    soup=BeautifulSoup(response.content,"html.parser")
    for data in soup.find_all('div', class_='ms-grid ms-grid-hor-d ms-grid-hor-t ms-grid-hor-m'):
        for a in data.find_all('a'):
            datetime_element = a.find('time', class_='ms-item__date')
            if datetime_element:
                datetime_value = datetime_element['datetime']
                print(f'Datetime: {datetime_value}')
                link = a.get('href')
            
                # Create the message text
                message_text = f"https://it.motorsport.com/{link}"

            if message_text in news_archive:
                print(f'Notizia già pubblicata: {message_text}')
                continue

            # Send the message to the Telegram channel
            try:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message_text}&parse_mode=HTML&link_preview=True"
                print(requests.get(url).json()) # this sends the message
                print("Message sent successfully!")
                news_archive.add(message_text)
                with open(ARCHIVE_FILE, 'a') as file:
                    file.write(message_text + '\n')
            except TelegramError as e:
                print(f"Error sending message: {e}")