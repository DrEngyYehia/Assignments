import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

# Function to calculate monthly payment
def calculate_payment():
    try:
        # Get user input
        loan_amount = float(loan_amount_entry.get())
        years = int(years_entry.get())
        job = job_var.get()

        # Fixed interest rates based on loan years
        interest_rates = {1: 13.76, 3: 14.06, 5: 14.87, 7: 15.71}
        interest_rate = interest_rates.get(years)

        # Calculate total interests
        total_interests = loan_amount * (interest_rate / 100) * years

        # Calculate total loan and monthly payment
        total_loan = loan_amount + total_interests
        monthly_payment = total_loan / (years * 12)

        # Display result
        result_label.config(text="Monthly Payment: $%.2f" % monthly_payment)
        total_label.config(text="Total loan: $%.2f" % total_loan)
        interest_label.config(text="interest rate: $%.2f" % interest_rate)


    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")


# Create GUI window
window = tk.Tk()
window.title("QNB – Loan Application")
window.geometry("500x300+100+100")
window.configure(bg='pink')
def resize_image(image_path, width, height):
    # Open the image file
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo
image_path = "C:/Users/mohse/Downloads/Qatar_National_Bank_Logo.svg.png"
resized_photo = resize_image(image_path, 100, 40)  # Change dimensions as needed
label = tk.Label(window, image=resized_photo)
label.pack(anchor="nw", padx=10, pady=10)

# Add logo
# logo_image = tk.PhotoImage(file="img_1.png")
# logo_label = tk.Label(window, image=logo_image)
# logo_label.place(relx=0.05, rely=0.05, anchor="center")

# Add title label
title_label = tk.Label(window, text="Saving Account", font=("Helvetica", 15))
title_label.place(relx=0.5, rely=0.2, anchor="center")

# Create widgets
job_var = tk.StringVar(window)
job_var.set("Select Job")
job_options = ["Doctor", "Engineer", "Teacher", "Other"]
job_menu = tk.OptionMenu(window, job_var, *job_options)
job_menu.place(relx=0.5, rely=0.35, anchor="center")

loan_amount_label = tk.Label(window, text="Enter Loan:")
loan_amount_label.place(relx=0.25, rely=0.45, anchor="center")
loan_amount_entry = tk.Entry(window)
loan_amount_entry.place(relx=0.5, rely=0.45, anchor="center")

years_label = tk.Label(window, text="Years:")
years_label.place(relx=0.25, rely=0.55, anchor="center")
years_entry = tk.Entry(window)
years_entry.place(relx=0.5, rely=0.55, anchor="center")


calculate_button = tk.Button(window, text="Calculate", command=calculate_payment)
calculate_button.place(relx=0.5, rely=0.65, anchor="center")

result_label = tk.Label(window, text="")
result_label.pack(side="bottom")
total_label = tk.Label(window, text="")
total_label.pack(side="bottom")
interest_label = tk.Label(window,text="")
interest_label.pack(side="bottom")

# Run the GUI
window.mainloop()