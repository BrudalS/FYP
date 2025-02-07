from sklearn.cluster import KMeans
import numpy as np

def run_kmeans(data):
    """Run K-means clustering on user behavior data."""
    kmeans = KMeans(n_clusters=3)  # Example, can be personalized
    kmeans.fit(data)
    return kmeans.labels_
