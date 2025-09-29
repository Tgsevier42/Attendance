from tkinter import *
from tkinter import ttk

class GreetingApp:
    def __init__(self, master):
        # 1. Create the buttons and arrange them vertically
        
        # Spanish Button (Row 1, Column 0)
        self.btn_es = ttk.Button(master, text="Español", command=self.set_spanish)
        self.btn_es.grid(row=1, column=0, padx=5, pady=5)
        
        # French Button (Row 2, Column 0)
        self.btn_fr = ttk.Button(master, text="Français", command=self.set_french)
        self.btn_fr.grid(row=2, column=0, padx=5, pady=5)

        # German Button (Row 3, Column 0)
        self.btn_de = ttk.Button(master, text="Deutsch", command=self.set_german)
        self.btn_de.grid(row=3, column=0, padx=5, pady=5)
        
        # English Button (Row 4, Column 0)
        self.btn_en = ttk.Button(master, text="English", command=self.set_english)
        self.btn_en.grid(row=4, column=0, padx=5, pady=5)
        
        # 2. Initialize and configure the main label
        # Place the label in the first row (row=0) as the initial instruction
        self.label1 = ttk.Label(master, text="Welcome. Select any language to see the greeting.")
        self.label1.grid(row=0, column=0, pady=10) # Positioned above the buttons
        
        # 3. Create the greeting label underneath the buttons
        # Note: I am assuming the request for the "translation under the buttons"
        # means placing the *greeting* below the buttons, while the *instruction* # label (which is more of a title/prompt) stays above. 
        # I'll use a second label for the actual greeting. 
        # I'll initialize it to an empty string.
        self.greeting_label = ttk.Label(master, text="")
        self.greeting_label.grid(row=5, column=0, pady=10)

    # --- Button Command Methods ---

    def set_english(self):
        # Update the greeting label text
        self.greeting_label.config(text="Hello")

    def set_spanish(self):
        self.greeting_label.config(text="¡Hola") # "Hola" matches the slide example
        
    def set_french(self):
        self.greeting_label.config(text="Bonjour")

    def set_german(self):
        self.greeting_label.config(text="Hallo")

# Create the main window (root) and run the application
if __name__ == "__main__":
    root = Tk()
    root.title("The 'Hello' Translator")
    app = GreetingApp(root)
    root.mainloop()