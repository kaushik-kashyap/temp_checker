import requests as rq

# enter the openweather api key here
# ##########################################################
key = "2c825c1148826e301f6a99070542a4d9"
# ##########################################################




endpoint = "https://api.openweathermap.org/data/2.5/weather"
endpoint2 = "http://api.openweathermap.org/geo/1.0/direct"



def input_data():
    k = input("enter the name of your place-->")
    return k



qep2 = {
    "q": input_data() ,
    "appid":key
} 





r2 = rq.get(endpoint2,params=qep2)

r2_lat = r2.json()[0]["lat"]
r2_lon = r2.json()[0]["lon"]




jk = {
    "lat" : r2_lat,
    "lon" : r2_lon,
    # "exclude" : ("hourly","minutely","daily","alerts"),
    "appid" : key,
    "units" : "metric"
}








r = rq.get(endpoint,params=jk)

rt = r.json()["main"]["temp"]

rd = r.json()["weather"][0]["description"]

print(f"the temperature is : {rt}(c) and the weather is : {rd}")


