from flask import Flask, request
import urllib.request
from bs4 import BeautifulSoup
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    message = response.message()
    responded = False

    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Ik kan geen quotes vinden op dit moment'
        message.body(quote)
        responded = True

    if 'kat' in incoming_msg and not responded:
        # return a cat pic
        message.media('https://cataas.com/cat')

        responded = True

    if 'wiki' in incoming_msg and not responded:
        # return a corresponding wiki page
        r = requests.get('https://nl.wikipedia.org/wiki/' + incoming_msg[5:])

        if r.status_code == 200:
            text = str(r.url)
        else:
            text = 'Ik kan geen fatsoenlijke wiki vinden op dit moment, alleen een foutmelding'
            message.media('https://http.cat/' + str(r.status_code))
        message.body(text)

        responded = True

    if 'vacatures' in incoming_msg and not responded:
        # search for jobs
        url = 'https://conspect.nl/vacatures'
        req = urllib.request.Request(url)
        text = urllib.request.urlopen(req).read()

        soup = BeautifulSoup(str(text), 'html.parser')
        functies = soup.findAll('div', {'class':'elementor-button-wrapper'})

        message.body('Alle huidige vacatures bij Conspect')
        for item in functies[3:-3]:
            response.message(url + str(item.find('a')['href']))

        responded = True

    if not responded:
        message.body('Er gaat iets niet helemaal lekker')

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
