import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def kmeans_clustering(data):
    numerical_features = data.select_dtypes(include=np.number).columns

    imputer = SimpleImputer(strategy='mean')
    data_imputed = imputer.fit_transform(data[numerical_features])

    scaler = StandardScaler()
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
    X_scaled = scaler.fit_transform(X)

    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.show()

    kmeans = KMeans(n_clusters=5, random_state=42)
    data['Cluster'] = kmeans.fit_predict(X_scaled)

    kmeans_score = silhouette_score(X_scaled, kmeans.labels_)
    print(f'Silhouette Score: {kmeans_score:.2f}')

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=data, palette='viridis', s=100)
    plt.title('Customer Segments')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend(title='Cluster')
    plt.show()