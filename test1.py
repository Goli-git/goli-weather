import pyowm
owm = pyowm.OWM('4f64718d2995e796e4c94d7081529cee')
observation = owm.weather_at_place(input('enter city : '))
weather = observation.get_weather()
temp = weather.get_temperature('celsius')['temp']
print(temp)

