import pandas as pd

# Define the file paths
input_excel_file = "/Users/femisokoya/Documents/GitHub/ddcc/ras2032.xls"
output_csv_file = "ddcc_melted_result.csv"

# Specify the worksheet name
worksheet_name = "Percentage_over_limit"

# Read the Excel file and skip the first 3 rows
df = pd.read_excel(input_excel_file, sheet_name=worksheet_name, skiprows=3)

# List of columns to melt
value_vars = ["Age 16 to 19", "Age 20 to 29", "Age 30 to 39", "Age 40 and over", "Total"]

# Melt the DataFrame with "value" as the name for the melted values
melted_df = pd.melt(df, id_vars=["Collision year", "Vehicle type"], value_vars=value_vars, var_name="Age Group", value_name="Percentage")

# Round the "Percentage" column to 2 decimal places
melted_df["Percentage"] = melted_df["Percentage"].round(2)

# Save the melted DataFrame to a CSV file
melted_df.to_csv(output_csv_file, index=False)

print(f"Data from '{worksheet_name}' worksheet in '{input_excel_file}' has been melted and saved to '{output_csv_file}' in CSV format with values rounded to 2 decimal places.")
