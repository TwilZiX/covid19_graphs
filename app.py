import urllib.request, json
from tkinter import *


def main():

    # Getting JSON data
    url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    response = urllib.request.urlopen(url)
    jsonData = json.loads(response.read())

    data = []
    # Countries without duplicates
    COUNTRIES = []

    # Adding records to data / COUNTRIES
    for row in jsonData["records"]:
        data.append([row["dateRep"], row["cases"], row["deaths"], row["countriesAndTerritories"]])
        if row["countriesAndTerritories"] not in COUNTRIES:
            COUNTRIES.append(row["countriesAndTerritories"])


    app = Tk()
    app.title("Coronavirus statistics")

    # Setting default value for country
    currentCountry = StringVar(app)
    currentCountry.set("Poland")

    # Setting default value for type of data
    TYPEOFDATA = ["Cases", "Deaths"]
    currentTypeOfData = StringVar(app)
    currentTypeOfData.set("Cases")

    countryLabel = Label(app, text="Choose a country").grid(row=0, column=0)
    countryMenu = OptionMenu(app, currentCountry, *COUNTRIES).grid(row=0, column=1)

    typeOfDataLabel = Label(app, text="Choose type of data").grid(row=0, column=2)
    typeOfDataMenu = OptionMenu(app, currentTypeOfData, *TYPEOFDATA).grid(row=0, column=3)

    app.mainloop()


if __name__ == "__main__":
    main()
