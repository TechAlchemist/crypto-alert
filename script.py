import requests
import pyttsx3
import datetime
import vars

engine = pyttsx3.init()
engine.setProperty('rate', 125)

currentDate = datetime.datetime.now()
currentDate = currentDate.strftime('%Y-%m-%d')

cryptoSymbol = 'DOGE'
querystring = {'market': 'USD', 'symbol': cryptoSymbol, 'function': 'DIGITAL_CURRENCY_DAILY'}
headers = {
	'x-rapidapi-key': vars.API_KEY,
	'x-rapidapi-host': vars.API_HOST
}

response = requests.request('GET', vars.API_URL, headers=headers, params = querystring)

queryResponse = response.json()
queryResponseData = queryResponse['Time Series (Digital Currency Daily)'][currentDate]

engine.say('Hello, here is your cryptocurrency update. ')
engine.say(queryResponseData)
engine.runAndWait()
engine.stop()
