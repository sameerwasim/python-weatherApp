import tkinter as tk
from tkinter import messagebox
import datetime
import requests

# onClick for Entry Box
def onClick(event):
    if entryBox.get() == 'Enter Location':
        entryBox.delete(0, "end")
        entryBox.insert(0, '')

# Search
def search(event=None):
    try:
        # API key
        apiKey = "apiKey" #Put your api key here from open weather
        # Url
        url = "http://api.openweathermap.org/data/2.5/weather?"
        # Full Url
        Url = url + "appid=" + apiKey + "&q=" + str(entryBox.get())
        # response
        response = requests.get(Url)
        weather = response.json()
        # Global declaration
        global location
        global temperature
        # Value Passing
        location.set(weather['name'])
        temperature.set(str(round(float(weather['main']['temp']) - 273.15)) + "°C")
        weatherDesc.set("Its " + weather['weather'][0]['main'] + " outside with temperature " + str(
            round(float(weather['main']['temp']) - 273.15)) + "°C\nwhere it feel likes " + str(
            round(float(weather['main']['feels_like']) - 273.15)) + "°C with an atmospheric\n pressure of " + str(
            weather['main'][
                'pressure']) + " Hg and humidity at " + str(weather['main'][
                                                                'humidity']) + "%, the\nwind is travelling at the speed of " + str(
            weather['wind'][
                'speed']) + " km/h at a\nangle of " + str(weather['wind']['deg']) + "°.")
        mmTemperature.set("Max: " + str(round(float(weather['main']['temp_max']) - 273.15)) +
                          "°C  Min: " + str(round(float(weather['main']['temp_min']) - 273.15)) + "°C")
    except:
        messagebox.showerror("Error", "Invalid Location Name.")

# root
root = tk.Tk()
root.title("isItCold?")
root.geometry("374x666")
root.resizable(False, False)
root.bind('<Return>', search)

# Canvas
mainCanvas = tk.Canvas(root)
mainCanvas.place(relwidth=1, relheight=1)

# Frame
topFrame = tk.Frame(mainCanvas)
topFrame.configure(bg="#0A3883")
topFrame.place(relx=0.0055, relwidth=0.990, relheight=0.1)

# Body Frame
bodyFrame = tk.Frame(mainCanvas)
bodyFrame.configure(bg="#3D7AD7", borderwidth="1", highlightthickness="1")
bodyFrame.place(relx=0.06, rely=0.15, relwidth=0.5, relheight=0.25)

# Bottom Frame

bottomFrame = tk.Frame(mainCanvas)
bottomFrame.configure(bg="#282F4C")
bottomFrame.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.35)


# Entry Box
entryBox = tk.Entry(topFrame)
font = ("Bahnschrift Light", 11)
entryBox.configure(font=font, relief="flat", bg="#0A3883", fg="#ffffff")
entryBox.insert(0, 'Enter Location')
entryBox.bind('<FocusIn>', onClick)
entryBox.place(relx=0.1, rely=0.28, relheight=0.5, relwidth=0.8)

# Button
searchButton = tk.Button(topFrame, command=search)
searchButton.configure(text="Search", font=("Bahnschrift Light", 8), bg="#0A3883", relief="flat", fg="#ffffff", activeforeground="#ffffff", activebackground="#0A3883")
searchButton.place(relx=0.8, rely=0.36)

# Background
backgroundImage = tk.PhotoImage(file="night.png")
mainCanvas.create_image(0,0, image=backgroundImage, anchor="nw")

# Location
location = tk.StringVar()
location.set("Location")
labelLocation = tk.Label(bodyFrame)
labelLocation.configure(textvariable=location, font=("Bahnschrift SemiBold Condensed", 30), bg="#3D7AD7", fg="#ffffff")
labelLocation.place(relx=0.5, rely=0.18, anchor="center")

# TimeStamp
dateTime = tk.StringVar()
timeStamp = datetime.datetime.now()
format_date = f"{timeStamp:%a, %B %d, %Y}"
dateTime.set(format_date)
labelTimeStamp = tk.Label(bodyFrame)
labelTimeStamp.configure(textvariable=dateTime, font=("Bahnschrift SemiLight", 10), bg="#3D7AD7", fg="#ffffff")
labelTimeStamp.place(relx=0.5, rely=0.37, anchor="center")

# Temperature
temperature = tk.StringVar()
temperature.set("00" + "°C")
labelTemperature = tk.Label(bodyFrame)
labelTemperature.configure(textvariable=temperature, font=("Bahnschrift SemiBold Condensed", 40), bg="#3D7AD7", fg="#ffffff")
labelTemperature.place(relx=0.5, rely=0.64, anchor="center")

# Max-Min Temperature
mmTemperature = tk.StringVar()
mmTemperature.set("Max: 0°C Min: 0°C")
labelMM_Temperature = tk.Label(bodyFrame)
labelMM_Temperature.configure(textvariable=mmTemperature, font=("Bahnschrift Light", 12), bg="#3D7AD7", fg="#ffffff")
labelMM_Temperature.place(relx=0.5, rely=0.88, anchor="center")


# Time Image
timeImage = tk.PhotoImage(file="moon.png")
mainCanvas.create_image(300,180, image=timeImage)

# Weather Description
weatherDesc = tk.StringVar()
weatherDesc.set(" ")
labelWeatherDesc = tk.Label(bottomFrame)
labelWeatherDesc.configure(textvariable=weatherDesc, font=("Bahnschrift Light", 12), bg="#282F4C", fg="#ffffff")
labelWeatherDesc.place(rely=0.3, relx=0.01)

# Footer
txtFooter = "Developed by Sameer"
mainCanvas.create_text(315, 652, text=txtFooter, font="Ariel 8", fill="#ffffff")

# root loop
root.mainloop()