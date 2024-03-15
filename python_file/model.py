import pandas as pd
from sklearn.cluster import KMeans

def kmeans_clustering(df, columns):
    """
    Perform K-means clustering on the specified columns of the DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame.
        columns (list): List of column names to use for K-means clustering.

    Returns:
        None
    """
    # Select columns for K-means
    kmeans_data = df[columns]
    
    # Fit K-means model
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(kmeans_data)
    
    # Get the number of records in each cluster
    cluster_counts = pd.Series(kmeans.labels_).value_counts().sort_index()
    
    # Save the number of records in each cluster to a text file
    cluster_counts.to_csv("k.txt", header=False)

    print("Cluster counts saved to k.txt")

