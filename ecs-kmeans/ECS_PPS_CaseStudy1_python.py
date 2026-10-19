# customer_segmentation.py

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. LOAD DATA
# -----------------------------
def load_data(file_path):
    print("\nLoading Data...")
    df = pd.read_csv(file_path)
    print("\nData Loaded Successfully")
    return df

# -----------------------------
# 2. DATA SANITIZATION
# -----------------------------
def clean_data(df): 
    print("\nCleaning Data...")

    # Remove duplicate records
    print("\nCleaning: Removing all Duplicate Records...")
    df = df.drop_duplicates()

    # Handle missing values
    print("\nCleaning: Replacing missing purchase amounts with median...")
    df['PurchaseAmount'] = df['PurchaseAmount'].fillna(df['PurchaseAmount'].median())

    print("\nCleaning: Replacing missing categories with Unknown...")
    df['ProductCategory'] = df['ProductCategory'].fillna("Unknown")
    
    # Remove invalid entries
    print("\nCleaning: Removing all records with Negative and zero Amounts...")
    df = df[df['PurchaseAmount'] > 0].reset_index(drop=True)
    
    # Convert date column
    print("\nCleaning: Converting Purchase Date values to date format...")
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')

    # Drop rows with invalid dates
    print("\nCleaning: Removing all records Invalid Dates...")
    df = df.dropna(subset=['TransactionDate'])

    return df

# -----------------------------
# 3. FEATURE ENGINEERING
# -----------------------------
def create_features(df):
    print("\nCreating Features...")

    # Purchase Frequency
    print("\nFeature: Purchase Frequency...")
    purchase_freq = df.groupby('CustomerID')['TransactionID'].count().reset_index()
    purchase_freq.columns = ['CustomerID', 'PurchaseFrequency']
    
    
    # Average Order Value
    print("\nFeature: Average Order Value...")
    aov = df.groupby('CustomerID')['PurchaseAmount'] \
        .mean() \
        .reset_index(name='AvgOrderValue')

    # Product Category Count (diversity)
    print("\nFeature: Diversity...")
    diversity = df.groupby('CustomerID')['ProductCategory'] \
              .nunique() \
              .reset_index(name='Diversity')

    # Merge all features
    print("\nMerging Features...")
    features =freq.merge(aov, on='CustomerID') \
                        .merge(diversity, on='CustomerID')

    return features

# -----------------------------
# 4. APPLY K-MEANS
# -----------------------------
def apply_kmeans(features, k=4):
    print("\nApplying K-Means Clustering...")

    # Selects the features and excludes CustomerID
    MergFeat= features[['Frequency', 'AvgOrderValue', 'Diversity']]

    # Scaling the data(z=(x−μ)/σ [μ-mean,σ= standard deviation,x=og value,z=how far from avg])
    scaler = StandardScaler()            
    scaled_data = scaler.fit_transform(MergFeat)

    # Applying K-Means
    kmeans = KMeans(n_clusters=k, random_state=42)
    features['Cluster'] = kmeans.fit_predict(scaled_data)

    return features, kmeans

# -----------------------------
# 5. SAVE OUTPUT
# -----------------------------
def save_results(features, output_file):
    print("\nSaving Results...")
    features.to_csv(output_file, index=False)
    print(f"\nResults saved to {output_file}")

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    input_file = "customer_transactions.csv"
    output_file = "segmented_customers.csv"

    df = load_data(input_file)
    df = clean_data(df)
    features = create_features(df)
    features.to_csv("features.csv", index=False)
    features, model = apply_kmeans(features, k=4)
    save_results(features, output_file)

    print("\nCluster Summary:")
    print(features.groupby('Cluster').mean())
if __name__=="__main__":
    main()

    
    
    
