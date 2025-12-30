import re
import csv

# File path
input_file = r'C:\Users\simde\Downloads\Data\Induc_WU.TXT'

# Pattern to match lines with frequency and inductance data
pattern = r"\d+\s+FREQ:\s+([\d.]+[kM]?Hz)\s+Ls\s+:\s+([\d.]+\s+\wH)"

# Data storage
data = []

# Read and process the file
with open(input_file, 'r') as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            freq = match.group(1)
            inductance = match.group(2)
            data.append({'Frequency': freq, 'Inductance': inductance})

# Output as CSV
output_file = r'C:\Users\simde\Downloads\Data\extracted_values.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Frequency', 'Inductance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print(f"Data extracted and saved to {output_file}")
