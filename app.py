from tkinter import *


def main():

    app = Tk()
    app.title("Coronavirus statistics")

    COUNTRIES = ["Poland", "USA", "France"]
    currentCountry = StringVar(app)
    currentCountry.set("Poland")

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
