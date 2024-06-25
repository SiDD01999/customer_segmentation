import matplotlib.pyplot as plt
import seaborn as sns


def plot_histograms(customer_data):
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    sns.histplot(customer_data['NumPurchases'], bins=30, kde=True)
    plt.title('Number of Purchases')
    plt.xlabel('Number of Purchases')
    plt.ylabel('Frequency')
    plt.savefig('images/number_of_purchases_histogram.png')

    plt.subplot(2, 2, 2)
    sns.histplot(customer_data['TotalQuantity'], bins=30, kde=True)
    plt.title('Total Quantity Purchased')
    plt.xlabel('Total Quantity')
    plt.ylabel('Frequency')
    plt.savefig('images/total_quantity_histogram.png')

    plt.subplot(2, 2, 3)
    sns.histplot(customer_data['TotalSpent'], bins=30, kde=True)
    plt.title('Total Amount Spent')
    plt.xlabel('Total Spent')
    plt.ylabel('Frequency')
    plt.savefig('images/total_spent_histogram.png')

    plt.subplot(2, 2, 4)
    sns.histplot(customer_data['Recency'], bins=30, kde=True)
    plt.title('Recency of Last Purchase')
    plt.xlabel('Recency (Days)')
    plt.ylabel('Frequency')
    plt.savefig('images/recency_histogram.png')

    plt.tight_layout()
    plt.show()


def plot_clusters(customer_data):
    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    components = pca.fit_transform(customer_data[['NumPurchases', 'TotalQuantity', 'TotalSpent', 'Recency']])

    customer_data['PCA1'] = components[:, 0]
    customer_data['PCA2'] = components[:, 1]

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=customer_data, x='PCA1', y='PCA2', hue='Cluster', palette='viridis')
    plt.title('Customer Segments')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(title='Cluster')
    plt.savefig('images/cluster_scatter_plot.png')
    plt.show()
