import pandas as pd

# Read CSV file
data = pd.read_csv("sample_data.csv")

# Remove empty rows
data = data.dropna()

# Department-wise average salary
summary = data.groupby("Department")["Salary"].mean().reset_index()

# Save to Excel
summary.to_excel("output_report.xlsx", index=False)

print("Automation complete! Excel report generated.")
