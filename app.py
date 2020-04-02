import urllib.request, json
import pandas as pd
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def main():
    
    app = Tk()
    app.title("Coronavirus statistics")
    app.geometry("1000x500")
    frame= Frame(app)
    frame.grid()
    grid = Frame(frame)
    grid.grid(sticky=N+S+E+W)

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

        # Converting to rrrrmmdd so it can be changed to pandas date
        date = str(row["dateRep"][6:] + row["dateRep"][3:5] + row["dateRep"][:2])

        data.append([date, row["cases"], row["deaths"],  row["countriesAndTerritories"]])
        if row["countriesAndTerritories"] not in COUNTRIES:
            COUNTRIES.append(row["countriesAndTerritories"])

    # Creating DataFrame based on data from JSON
    df = pd.DataFrame(data, columns=labels)

    # Converting Cases and Deaths to integer numbers
    df[["Cases", "Deaths"]] = df[["Cases", "Deaths"]].astype(int)

    # Converting Date to datetime
    df["Date"] = pd.to_datetime(df["Date"])

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

    # Function for displaying plot with current user choices
    def showPlot():
        # Limiting DataFrame based on user choice
        result = df[["Date", currentTypeOfData.get()]].loc[df["Country"] == currentCountry.get()]

        # Creating plot
        fig = Figure(figsize=(10,5), dpi=100)
        fig.add_subplot(111).plot(result["Date"], result[currentTypeOfData.get()])
        fig.autofmt_xdate()
        fig.suptitle(currentCountry.get() + " - " + currentTypeOfData.get())

        # Putting plot to TkInter
        canvas = FigureCanvasTkAgg(fig, master=app)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=5)

    # Displaying plot even before pushing button
    showPlot()

    #Generate button
    generateButton = Button(text="Generate", command=showPlot).grid(row=0, column=4)

    app.mainloop()


if __name__ == "__main__":
    main()
