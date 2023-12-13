import json
import time
import urllib.request

API='JoZpeCmsptmiRaBXJv59aVz1BVxApjLX'

def getLocation(city):
    search_address="http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+API+"&q="+city+"&details=true"
    with urllib.request.urlopen(search_address) as search_address:
        data=json.loads(search_address.read().decode())
        loaction_key=data[0]['Key']
        return(loaction_key)

#city='mumbai'
#locationkey=getLocation(city)

def getforecast(locationkey):
    daily_forecastURL="http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+locationkey+"?apikey="+API+""
    #print(daily_forecastURL)
    with urllib.request.urlopen(daily_forecastURL) as daily_forecastURL:
        data=json.loads(daily_forecastURL.read().decode())
        #print(data["DailyForecasts"])
        return(data["DailyForecasts"])
    #print(data)

