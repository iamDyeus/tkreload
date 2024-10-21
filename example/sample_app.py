import tkinter as tk

def on_button_click():
    print("Hello World!")

# Create the main application window
app = tk.Tk()
app.title("Demo Application")

# set size to 500x500
app.geometry("500x500")



# Create a label
label = tk.Label(app, text="Hello from iamDyeus 👋", font=("Helvetica", 16))
label.pack(pady=50)

label = tk.Label(app, text="use `tkreload` to open this app, and play around!", font=("Helvetica", 12))
label.pack(pady=30)

label = tk.Label(app, text="in your terminal: `tkreload sample_app.py`", font=("Helvetica", 12))
label.pack(pady=5)

label = tk.Label(app, text="When the reloader is running, press 'H' to see list of commands", font=("Helvetica", 10))
label.pack(pady=10)

# Create a button
button = tk.Button(app, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Run the application
app.mainloop()
