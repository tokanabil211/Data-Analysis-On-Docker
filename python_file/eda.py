import pandas as pd
from vis import create_age_histogram

import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def eda(df):
    numeric_df = df.select_dtypes(include=[np.number])
    columns = numeric_df.columns
    results = np.zeros((len(columns), len(columns)))

    for i in range(len(columns)):
        for j in range(len(columns)):
            col1 = numeric_df[columns[i]]
            col2 = numeric_df[columns[j]]
            similarity = cosine_similarity(col1, col2)
            results[i, j] = similarity

    with open('eda-in-1.txt', 'w') as f:
        for i in range(len(columns)):
            for j in range(len(columns)):
                f.write(f'Cosine similarity between {columns[i]} and {columns[j]}: {results[i, j]}\n')

        # Calculate and write mean and median
        for col in columns:
            mean_val = numeric_df[col].mean()
            median_val = numeric_df[col].median()
            f.write(f'{col} has Mean of: {mean_val} and a Median of {median_val}\n')

        # Analyze and write correlation between columns
        correlation_matrix = numeric_df.corr()
        f.write('\nCorrelation between different features:\n')
        f.write(correlation_matrix.to_string())

        Highest_fare = df['Fare'].max()
        Biggest_family_size = df['FamilySize'].max()

        f.write(f'\n\nHighest Fare: {Highest_fare}\n')
        f.write(f'Biggest Family Size: {Biggest_family_size}\n')

    with open('eda-in-2.txt', 'w') as f:
        # Write additional insights here
        f.write(df.describe().to_string())

    with open('eda-in-3.txt', 'w') as f:  
        f.write("\nInsight 3: Distribution of passengers by sex\n") # Write additional insights here
        f.write(df.value_counts().to_string())

    print("Exploratory data analysis completed.")

# Example usage:
    create_age_histogram(df)
