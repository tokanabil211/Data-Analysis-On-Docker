import matplotlib.pyplot as plt
import pandas as pd
from model import kmeans_clustering

def create_age_histogram(df):
    plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig('vis.png')

    # Specify the columns for K-means clustering
    columns_for_kmeans = ['Age', 'Fare'] # Replace with your actual column names
    
    # Call the kmeans_clustering function
    kmeans_clustering(df, columns_for_kmeans)

if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("train_titanic.csv")
    
    # Call the create_age_histogram function
    create_age_histogram(df)

