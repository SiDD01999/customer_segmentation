from logging import exception

import pandas as pd
from openai import RateLimitError

import openai
from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.clustering import standardize_data, perform_clustering
from src.visualization import plot_histograms, plot_clusters

# Load data
file_path = 'C:\\Users\\siddc\\OneDrive\\Desktop\\DATA SCIENCE\\New folder\\customer_segmentation\\data\\Online Retail.xlsx'
data = load_data(file_path)

# Clean data
cleaned_data = clean_data(data)

# Create features
customer_data = create_features(cleaned_data)

# Standardize features
features = customer_data[['NumPurchases', 'TotalQuantity', 'TotalSpent', 'Recency']]
scaled_features = standardize_data(features)

# Perform clustering
clusters, kmeans = perform_clustering(scaled_features, n_clusters=3)
customer_data['Cluster'] = clusters

# Plot histograms
plot_histograms(customer_data)

# Plot clusters
plot_clusters(customer_data)