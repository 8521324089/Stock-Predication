import let
import requests
stock="AAPL";
url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history"

querystring = {"symbol":stock,"interval":"5m","diffandsplits":"false"}

headers = {
	"X-RapidAPI-Key": "41f8e317a3mshacdafb16b16cfa6p137a6ejsn5ce2259b80ab",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

st=(response.json()["meta"])
print(st["regularMarketPrice"])