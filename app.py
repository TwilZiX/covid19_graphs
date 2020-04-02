import urllib.request, json
import pandas as pd
from tkinter import *


def main():

    app = Tk()
    app.title("Coronavirus statistics")

    # Getting JSON data
    url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    response = urllib.request.urlopen(url)
    jsonData = json.loads(response.read())

    # Labels for pandas DataFrame
    labels = ["Date", "Cases", "Deaths", "Country"]
    data = []
    # Countries without duplicates
    COUNTRIES = []

    # Adding records to data / COUNTRIES
    for row in jsonData["records"]:
        data.append([row["dateRep"], row["cases"], row["deaths"], row["countriesAndTerritories"]])
        if row["countriesAndTerritories"] not in COUNTRIES:
            COUNTRIES.append(row["countriesAndTerritories"])

    # Creating DataFrame based on data from JSON
    df = pd.DataFrame(data, columns=labels)

    # Setting default value for country
    currentCountry = StringVar(app)
    currentCountry.set("Poland")

    # Setting default value for type of data
    TYPEOFDATA = ["Cases", "Deaths"]
    currentTypeOfData = StringVar(app)
    currentTypeOfData.set("Cases")

    # Displaying OptionMenu for country
    countryLabel = Label(app, text="Choose a country").grid(row=0, column=0)
    countryMenu = OptionMenu(app, currentCountry, *COUNTRIES).grid(row=0, column=1)

    # Displaying OptionMenu for type of data
    typeOfDataLabel = Label(app, text="Choose type of data").grid(row=0, column=2)
    typeOfDataMenu = OptionMenu(app, currentTypeOfData, *TYPEOFDATA).grid(row=0, column=3)

    # Getting values based on user options
    result = df[["Date", currentTypeOfData.get()]].loc[df["Country"] == currentCountry.get()]
    print(result.to_string(index=False))

    app.mainloop()


if __name__ == "__main__":
    main()
