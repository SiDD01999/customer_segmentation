def create_features(data):
    customer_data = data.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',
        'Quantity': 'sum',
        'TotalAmount': 'sum',
        'InvoiceDate': 'max'
    }).reset_index()

    customer_data.columns = ['CustomerID', 'NumPurchases', 'TotalQuantity', 'TotalSpent', 'LastPurchaseDate']
    customer_data['Recency'] = (data['InvoiceDate'].max() - customer_data['LastPurchaseDate']).dt.days
    return customer_data
