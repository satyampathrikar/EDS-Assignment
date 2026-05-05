import pandas as pd

# Create sample data
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [80, 90, 85]
})

# Merge (like SQL join)
merged = pd.merge(df1, df2, on="ID")
print("Merged Data:\n", merged)

# Concatenate
concat = pd.concat([df1, df2], axis=1)
print("Concatenated Data:\n", concat)



#  Handling Missing Data
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, None, 90]
}

df = pd.DataFrame(data)

print("Original:\n", df)

# Fill missing values
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("After Filling:\n", df)


#  Filtering & Sorting Data

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, 70, 90]
})

# Filter
filtered = df[df["Marks"] > 75]

# Sort
sorted_df = df.sort_values(by="Marks", ascending=False)

print("Filtered:\n", filtered)
print("Sorted:\n", sorted_df)

#  Time Series Data Handling

import pandas as pd

# Create date range
dates = pd.date_range(start="2024-01-01", periods=5)

df = pd.DataFrame({
    "Date": dates,
    "Sales": [100, 150, 200, 250, 300]
})

# Set Date as index
df.set_index("Date", inplace=True)

print("Time Series Data:\n", df)

# Monthly resampling (example)
monthly = df.resample("ME").sum()

print("Monthly Data:\n", monthly)


# Applying Functions

df = pd.DataFrame({
    "Marks": [50, 60, 70]
})

# Apply function
df["Double"] = df["Marks"].apply(lambda x: x * 2)

print(df)