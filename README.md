# Customer Segmentation Analysis

This project performs a customer segmentation analysis on an e-commerce dataset. The goal is to identify distinct customer segments based on their purchasing behavior and provide insights that can inform targeted marketing strategies.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Steps](#steps)
- [Running the Project](#running-the-project)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)

## Project Overview

Customer segmentation involves dividing a customer base into distinct groups that share similar characteristics. This project uses clustering techniques to segment customers based on the following features:
- Number of purchases
- Total quantity purchased
- Total amount spent
- Recency (days since last purchase)

## Dataset

The dataset used in this project is an e-commerce dataset containing transactional data. The file is located at:
[Online Retail Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx)



## Steps

1. **Load Data**:
   - The data is loaded from an Excel file using `pandas`.

2. **Clean Data**:
   - Missing values are handled, and any necessary data cleaning steps are performed.

3. **Create Features**:
   - Features such as the number of purchases, total quantity, total amount spent, and recency are created for each customer.

4. **Standardize Features**:
   - The features are standardized to ensure they have a mean of 0 and a standard deviation of 1, which is important for clustering.

5. **Perform Clustering**:
   - K-means clustering is used to segment customers into three clusters based on their purchasing behavior.

6. **Plot Histograms**:
   - Histograms are created to visualize the distribution of each feature.

7. **Plot Clusters**:
   - A scatter plot is created to visualize the customer segments in a two-dimensional space using PCA.

## Running the Project

To run this project, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone <repository-url>

2. **Navigate to the project directory**:

   ```sh
   cd customer_segmentation

3. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
3. **Run the script**:

   ```sh
   python src/main.py
   
# Visualizations
## Histograms
1. **Number of Purchases Histogram**:

Shows the distribution of the number of purchases made by customers.
2. **Total Quantity Histogram**:

Displays the distribution of the total quantity of items purchased.
3. **Total Spent Histogram**:

Illustrates the distribution of the total amount spent by customers.
4. **Recency Histogram**:

Depicts the distribution of recency, indicating how recently customers made a purchase.
# Clusters
1. **Cluster Scatter Plot**:

Visualizes the customer segments identified by the clustering algorithm. Each color represents a different cluster, showing how customers are grouped based on their purchasing behavior.
# Conclusion
This project successfully segments customers into distinct groups based on their purchasing behavior. The insights derived from this analysis can inform targeted marketing strategies, such as personalized promotions and re-engagement campaigns.# customer_segmentation
