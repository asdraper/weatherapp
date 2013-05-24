import WeatherSystem

# Where On Earth ID (Default is Joliet, IL)
woeid = '2429708'

#Create WeatherSystem object and pass woeid
weatherObject = WeatherSystem.WeatherSystem(woeid)

# Load and then display weather data
weatherObject.loadWeather()


