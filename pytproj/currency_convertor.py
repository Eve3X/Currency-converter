import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
df = pd.read_csv("sorted_combined_data.csv")  # Replace with your actual file path

# Convert the 'Date' column to a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Standard Currency Statement
        self.standard_currency_label = ttk.Label(root, text="Our Standard Currency is USD.")
        self.standard_currency_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.W)

        # Convert USD Segment
        self.convert_usd_label = ttk.Label(root, text="Convert USD to:")
        self.convert_usd_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.convert_currency_var = tk.StringVar()
        self.convert_currency_entry = ttk.Entry(root, textvariable=self.convert_currency_var)
        self.convert_currency_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        self.convert_currency_entry.insert(0, "")  # Default selection

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_usd)
        self.convert_button.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

        # Currency Selection
        self.currency_label = ttk.Label(root, text="Select Currency:")
        self.currency_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.currency_var = tk.StringVar()
        self.currency_entry = ttk.Entry(root, textvariable=self.currency_var)
        self.currency_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.currency_entry.insert(0, "")  # Default selection

        # Duration Selection
        self.duration_label = ttk.Label(root, text="Select Duration:")
        self.duration_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.duration_var = tk.StringVar()
        self.duration_combobox = ttk.Combobox(root, textvariable=self.duration_var, values=["Weekly", "Monthly", "Quarterly", "Yearly", "Decade"])
        self.duration_combobox.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        self.duration_combobox.set("Weekly")  # Default selection

        # Graph Display
        self.plot_button = ttk.Button(root, text="Plot Graph", command=self.plot_graph)
        self.plot_button.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_usd(self):
        selected_currency = self.convert_currency_var.get()
        if selected_currency in df.columns:
            last_conversion_rate = df[selected_currency].iloc[-1]
            converted_value = 1 / last_conversion_rate
            tk.messagebox.showinfo("Conversion Result", f"1 USD = {last_conversion_rate} {selected_currency}\nConverted Value: {converted_value:.4f} USD")
        else:
            tk.messagebox.showerror("Error", "Please select a valid currency.")

    def plot_graph(self):
        currency = self.currency_var.get()
        duration = self.duration_var.get()

        if currency and duration:
            df_subset = df[[currency]]

            # Interpolate missing values using linear interpolation
            df_subset = df_subset.interpolate(method='linear')

            if duration == "Weekly":
                # Fetch data for the last 7 days
                df_subset = df_subset[df_subset.index > (df_subset.index.max() - pd.DateOffset(days=7))]
            elif duration == "Monthly":
                # Fetch data for the last 30 days
                df_subset = df_subset[df_subset.index > (df_subset.index.max() - pd.DateOffset(days=30))]
            elif duration == "Quarterly":
                # Fetch data for the last 3 months
                df_subset = df_subset[df_subset.index > (df_subset.index.max() - pd.DateOffset(months=3))]
            elif duration == "Yearly":
                # Fetch data for the last 12 months
                df_subset = df_subset[df_subset.index > (df_subset.index.max() - pd.DateOffset(months=12))]
            elif duration == "Decade":
                # Fetch data for the last 10 years
                df_subset = df_subset[df_subset.index > (df_subset.index.max() - pd.DateOffset(years=10))]

            # Plotting
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(df_subset.index, df_subset[currency], label=f'{currency} ({duration})', color='blue')

            # Annotate highest and lowest values with dates
            max_value_index = df_subset[currency].idxmax()
            min_value_index = df_subset[currency].idxmin()
            max_value = df_subset[currency].max()
            min_value = df_subset[currency].min()

            ax.annotate(f'Highest Value: {max_value:.2f}\nDate: {max_value_index}', 
                        xy=(max_value_index, max_value), 
                        xytext=(max_value_index, max_value + 5),
                        arrowprops=dict(facecolor='black', shrink=0.05),
                        )

            ax.annotate(f'Lowest Value: {min_value:.2f}\nDate: {min_value_index}', 
                        xy=(min_value_index, min_value), 
                        xytext=(min_value_index, min_value - 5),
                        arrowprops=dict(facecolor='black', shrink=0.05),
                        )

            ax.set_title(f"{currency} - {duration} Average")
            ax.set_xlabel('Date')
            ax.set_ylabel('Currency Value')
            ax.legend()
            ax.grid(True)
            
            # Show the plot
            plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
