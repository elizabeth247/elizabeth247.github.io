import csv
import json
import tkFileDialog

#make list of 26 city names
citieslist = []
with open("26citiesWithLatitudeLongitude.csv") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		citieslist.append(row["\xef\xbb\xbfCity"]) #weird encoding thing added this crap to the beginning of City



#save json data as list, each item is one city entry from json file
config = json.loads(open("cityPrices.json").read())



#build dictionary of cities and prices. Keys: cities. Values: json entry for that city
prices = {}
for item in config:
	cityname = item["name"].strip().split(",")[0]
	prices[cityname] = item




#skeleton structure for getting average price of item at particular index (example uses index 1) for each of 26 cities
# for city in citieslist:
# 	pricelist = prices[city]
# 	print pricelist["prices"][1]["average_price"]


#get average grocery price for a given city
def getGroceries(city):
	pricelist = prices[city]
	groceriesIndexes = [7,8,9,10,17,45,46,47,48,50,51,52,53]
	groceriesTotal = 0
	for ind in groceriesIndexes:
		pricelist = prices[city]
		groceriesTotal += pricelist["prices"][ind]["average_price"]
	groceriesAvg = float(groceriesTotal)/len(groceriesIndexes)
	return groceriesAvg

def getRestaurant(city):
	pricelist = prices[city]
	return pricelist["prices"][1]["average_price"]

def getPublicTransport(city):
	pricelist = prices[city]
	return pricelist["prices"][16]["average_price"]

def getGasPrice(city):
	pricelist = prices[city]
	return pricelist["prices"][19]["average_price"]

def getApartmentRent(city):
	pricelist = prices[city]
	aptRentIndexes = [21,22]
	aptTotal = 0
	for ind in aptRentIndexes:
		aptTotal += pricelist["prices"][ind]["average_price"]
	aptAvg = float(aptTotal)/len(aptRentIndexes)
	return aptAvg

def getApartmentBuy(city):
	pricelist = prices[city]
	aptBuyIndexes = [37,39]
	aptTotal = 0
	for ind in aptBuyIndexes:
		aptTotal += pricelist["prices"][ind]["average_price"]
	aptAvg = float(aptTotal)/len(aptBuyIndexes)
	return aptAvg

def getEntertainment(city):
	pricelist = prices[city]
	return pricelist["prices"][30]["average_price"]

def allInfoForCity(city):
	info = []
	info.append(getGroceries(city))
	info.append(getRestaurant(city))
	info.append(getPublicTransport(city))
	info.append(getGasPrice(city))
	info.append(getApartmentRent(city))
	info.append(getApartmentBuy(city))
	info.append(getEntertainment(city))
	return info


headers = ["City","Groceries","Restaurant","PublicTransport","Gas","Rent","BuyApartment","Entertainment"]


def get_file_to_save():
    """
    prompt for new file, user enters name, return file (open for writing)
    """
    file = tkFileDialog.asksaveasfile(title="save file")
    return file

def writeToFile():
	file = get_file_to_save()
	if file == None:
		return
	#write headers as first row
	for header in headers:
		file.write(header)
		file.write(",")
	file.write("\n")
	#write rows for each city
	for city in citieslist:
		file.write(city)
		file.write(",")
		citypriceinfo = allInfoForCity(city)
		for thing in citypriceinfo:
			file.write(str(thing))
			file.write(",")
		file.write("\n")
	file.close()

writeToFile()





