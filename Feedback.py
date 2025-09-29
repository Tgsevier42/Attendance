from tkinter import *
from tkinter import ttk

class FeedbackApp:
    def __init__(self, master):
        # Set the main window title
        master.title("Customer Feedback")

        # --- 1. Setup Input Variables ---
        self.name_var = StringVar()
        self.email_var = StringVar()
        # Note: Text widget content is managed directly, not with a StringVar

        # --- 2. Create and Place Widgets using Grid ---

        # Row 0: Title Label
        title_label = ttk.Label(master, text="Please provide feedback on your experience", font=('Arial', 12, 'bold'))
        # Spans two columns for better centering
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Row 1: Name Entry
        ttk.Label(master, text="Name:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.name_entry = ttk.Entry(master, textvariable=self.name_var, width=40)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        # Row 2: Email Entry
        ttk.Label(master, text="Email:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.email_entry = ttk.Entry(master, textvariable=self.email_var, width=40)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        # Row 3: Feedback Label
        ttk.Label(master, text="Feedback:").grid(row=3, column=0, sticky='nw', padx=5, pady=5)

        # Row 3 (Cont): Multiline Text Widget for Feedback
        # Text widget is used for multi-line input (as shown in the slide's image)
        self.feedback_text = Text(master, height=5, width=30)
        self.feedback_text.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
        
        # Row 4: Submit Button
        self.submit_btn = ttk.Button(master, text="Submit", command=self.submit_feedback)
        # Place the button in the right column, spanning 1 column
        self.submit_btn.grid(row=4, column=1, padx=5, pady=10, sticky='e') 

        # Configure column weights to allow the right column (col 1) to expand
        master.grid_columnconfigure(1, weight=1)

    # --- Button Command Method ---

    def submit_feedback(self):
        # 1. Have the text they have entered print to the console
        
        # Get data from entry fields using the StringVars
        name = self.name_var.get()
        email = self.email_var.get()
        
        # Get data from the Text widget (from index 1.0 to end, minus the trailing newline)
        feedback = self.feedback_text.get("1.0", END).strip()
        
        print("-" * 30)
        print("FEEDBACK SUBMITTED:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Feedback: {feedback}")
        print("-" * 30)
        
        # 2. Clear the text
        
        # Clear Entry fields by setting the StringVars to an empty string
        self.name_var.set("")
        self.email_var.set("")
        
        # Clear Text widget content (from index 1.0 to END)
        self.feedback_text.delete("1.0", END)


# Create the main window (root) and run the application
if __name__ == "__main__":
    root = Tk()
    app = FeedbackApp(root)
    root.mainloop()