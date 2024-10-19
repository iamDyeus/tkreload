import tkinter as tk

def on_button_click():
    print("Hello World!")

# Create the main application window
app = tk.Tk()
app.title("Demo Application")

# set size to 500x500
app.geometry("500x500")



# Create a label
label = tk.Label(app, text="tkreload Demo Application, fuck around and find out", font=("Helvetica", 16))
label.pack(pady=50)

label = tk.Label(app, text="Change stuff here, and press ENTER+R to refresh", font=("Helvetica", 16))
label.pack(pady=50)

# Create a button
button = tk.Button(app, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Run the application
app.mainloop()
