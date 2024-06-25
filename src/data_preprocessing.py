import pandas as pd

def load_data(file_path):
    data = pd.read_excel(file_path, engine='openpyxl')
    return data

def clean_data(data):
    data = data.dropna(subset=['CustomerID'])
    data = data.drop_duplicates()
    data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['TotalAmount'] = data['Quantity'] * data['UnitPrice']
    return data
