import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "N3YJLMCF2GHTG5JN"
NEWS_API_KEY = "8a59798365ad4658ace3441076a6dc22"

api_key = "3035bef9a3d4e38327b77c211092e0d9"
TWILIO_SID = "ACbdb95813d830297045c867a7f4c820ec"
TWILIO_AUTH_TOKEN = "693b5e4bd2906c1f2e32bc4b35055c47"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [(data[key]["4. close"]) for (key, value) in data.items()]

today = float(data_list[0])
yesterday = float(data_list[1])

difference = (today - yesterday)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage = round((difference / yesterday) * 100)


if abs(percentage) >= 1:
    parameters_news = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][0:3]
    formatted_articles = [f'{STOCK_NAME}: {up_down}{percentage}%\n Headline: {(article["title"])}. \nBrief: {(article["description"])}' for article in articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+19123781162',
            to="+543493495168"
        )


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

