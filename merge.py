import os
import pandas as pd

# Directory containing the CSV files
products_folder = "Products"

# List all CSV files in the folder
csv_files = [filename for filename in os.listdir(products_folder) if filename.endswith(".csv")]

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate through each CSV file
for file in csv_files:
    file_path = os.path.join(products_folder, file)
    
    # Read the CSV file
    product_data = pd.read_csv(file_path)
    
    # Append the data to the merged DataFrame
    merged_data = merged_data.append(product_data, ignore_index=True)

# Save the merged data to a new CSV file
merged_file_path = os.path.join(products_folder, "Amazon-Products.csv")
merged_data.to_csv(merged_file_path, index=False)

print(f"Merged data saved to {merged_file_path}")
