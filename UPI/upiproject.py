import pandas as pd
import os

folder_path = r'C:\Users\prajw\Desktop\upi projects' 
all_months_data = []

# Loop through every Excel file
for file in os.listdir(folder_path):
    if file.lower().endswith('.xlsx') or file.lower().endswith('.xls'):
        file_path = os.path.join(folder_path, file)
        
        # skiprows=4 skips all the messy titles and starts exactly at the data
        df = pd.read_excel(file_path, skiprows=4)
        
        # Manually assign clean names to the 7 columns the RBI provides
        df.columns = [
            'Blank_Margin', 'Sr_No', 'Bank_Name', 
            'Remitter_Vol_Lakh', 'Remitter_Val_Cr', 
            'Beneficiary_Vol_Lakh', 'Beneficiary_Val_Cr'
        ]
        
        # Add the month name
        df['Month'] = file.split('.')[0].title()
        
        # Convert Lakhs to Millions (Divide by 10)
        df['Remitter_Vol_Mn'] = df['Remitter_Vol_Lakh'] / 10
        df['Beneficiary_Vol_Mn'] = df['Beneficiary_Vol_Lakh'] / 10
        
        # Drop the junk columns and keep only what we need for the dashboard
        clean_df = df[['Month', 'Bank_Name', 'Remitter_Vol_Mn', 'Remitter_Val_Cr', 'Beneficiary_Vol_Mn', 'Beneficiary_Val_Cr']]
        
        all_months_data.append(clean_df)

# Merge everything into one master table
master_df = pd.concat(all_months_data, ignore_index=True)

# Drop any completely empty rows that might have snuck in at the bottom of the Excel files
master_df = master_df.dropna(subset=['Bank_Name'])

# Save the final masterpiece as a clean CSV file!
output_path = os.path.join(folder_path, 'Cleaned_UPI_Bank_Data.csv')
master_df.to_csv(output_path, index=False)

print("Data successfully cleaned, converted, and saved to your folder!")
print(master_df.head())
