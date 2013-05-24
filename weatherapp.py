import Weather

def getWeather():
    request = input("What would you like to know?")
    if ("temperature" or 'weather') and "outside" in request:
	    print ("Right now it is", Weather.weatherObject.gatherCurrentTemp(),
		"degrees outside and", Weather.weatherObject.gatherCurrentCondition())
    elif "high" in request:
        print ("The high temperature for today is", Weather.weatherObject.gatherWeatherTempHigh(), "degrees")
    elif "low" in request:
        print ("The low temperature for today is", Weather.weatherObject.gatherWeatherTempLow(), "degrees")    
    elif "nothing" in request:
	    return