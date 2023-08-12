# for deleting rest of the lines except top 100 lines (you can modify 100 to any number)

import os
import pandas as pd

# Directory containing the CSV files
products_folder = "Products"

# List all CSV files in the folder
csv_files = [filename for filename in os.listdir(products_folder) if filename.endswith(".csv")]

# Process each CSV file
for file in csv_files:
    file_path = os.path.join(products_folder, file)
    
    # Read the CSV file
    product_data = pd.read_csv(file_path)
    
    # Keep only the top 300 lines
    product_data = product_data.head(100)
    
    # Save the modified data back to the CSV file
    product_data.to_csv(file_path, index=False)
    
    print(f"Processed {file} and saved top 300 lines.")
