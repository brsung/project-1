import pandas as pd
import re

# File path
file_path = r"Data\wu student names.xlsx"

# Read the Excel file
df_raw = pd.read_excel(file_path, header=None)  # No header in the file
data = df_raw.iloc[0, 0]  # Extract the content of cell A1

# Clean the data string by ensuring no leading/trailing commas
data = data.strip().lstrip(',').rstrip(',')

# Define regex pattern to extract names and emails
pattern = r'\s*([^<,]+)\s*<([^>]+)>'

# Find all matches using re.findall
matches = re.findall(pattern, data)

# Create a DataFrame
df_cleaned = pd.DataFrame(matches, columns=["names", "email"])

# Strip extra whitespace from names and emails
df_cleaned["names"] = df_cleaned["names"].str.strip()
df_cleaned["email"] = df_cleaned["email"].str.strip()

# Display the cleaned DataFrame
print(df_cleaned)

# Save to a new Excel file (optional)
df_cleaned.to_excel("Data\cleaned_student_data.xlsx", index=False)