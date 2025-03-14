import tkinter as tk
from tkinter import messagebox, PhotoImage
import requests

# API Configuration
API_URL = "http://127.0.0.1:8000/weather/"  # Your FastAPI backend URL

# Function to Fetch Weather Data
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    try:
        response = requests.get(f"{API_URL}{city}")
        if response.status_code == 200:
            data = response.json()
            city_name = data.get("city", "Unknown")
            weather = data.get("weather", "Unknown")

            # Update Weather Output
            result_label.config(text=f"🌍 {city_name}\n☁ {weather}", fg="white")

        else:
            messagebox.showerror("Error", "Could not fetch weather data!")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Hover Effects for Button
def on_enter(e):
    search_button.config(bg="#f75990", fg="white")

def on_leave(e):
    search_button.config(bg="#ff6b6b", fg="black")

# Create Tkinter Window
root = tk.Tk()
root.title("Weather Assistant")
root.geometry("500x500")
root.configure(bg="#2C3E50")

# Load Background Image
bg_image = PhotoImage(file="frontend/bg.png")  # Ensure this image exists in 'frontend' folder
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Title Label
title_label = tk.Label(root, text="🌤 Weather Assistant", font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
title_label.pack(pady=20)

# Input Box
city_entry = tk.Entry(root, font=("Arial", 16), width=20, bg="#FFD700", fg="black", bd=2, relief="flat")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city...")

# Search Button with Effects
search_button = tk.Button(
    root, text="Get Weather", font=("Arial", 14, "bold"), 
    bg="#ff6b6b", fg="black", relief="flat", padx=10, pady=5, 
    activebackground="#f75990", activeforeground="white",
    command=get_weather
)
search_button.pack(pady=15)
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

# Weather Result Display Box
result_frame = tk.Frame(root, bg="#34495E", bd=5)
result_frame.pack(pady=15)
result_label = tk.Label(result_frame, text="", font=("Arial", 18, "bold"), fg="white", bg="#34495E", padx=20, pady=10)
result_label.pack()

# Run the Tkinter Loop
root.mainloop()





