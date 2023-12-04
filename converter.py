import pandas as pd
from icu import Transliterator
import tkinter as tk
from tkinter import filedialog

# Create a Zawgyi to Unicode converter
converter = Transliterator.createInstance("Zawgyi-my")

# Function to perform Zawgyi to Unicode conversion on the entire DataFrame
def convert_and_save(input_path, output_path):
    # Read the DataFrame from various Excel formats
    try:
        df = pd.read_excel(input_path)
    except:
        # If unable to read as Excel, try reading as CSV
        df = pd.read_csv(input_path)

    # Apply the Zawgyi to Unicode conversion to all columns
    df = df.applymap(lambda x: converter.transliterate(str(x)))

    # Save the DataFrame to a new Excel file
    df.to_excel(output_path, index=False)

# Function to handle the "Convert" button click
def convert_button_click():
    # Ask for input file path
    input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Excel files", "*.xlsx;*.xls;*.csv")])

    # Ask for output file path
    output_file_path = filedialog.asksaveasfilename(title="Select Output Excel File", defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    # Perform conversion and save to the specified file
    convert_and_save(input_file_path, output_file_path)
    label_status.config(text="Conversion complete!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Zawgyi to Unicode Converter")

# Create and place GUI components
button_convert = tk.Button(root, text="Convert", command=convert_button_click)
button_convert.pack()

label_status = tk.Label(root, text="")
label_status.pack()

# Start the Tkinter event loop
root.mainloop()
