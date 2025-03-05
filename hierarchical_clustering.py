import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

def hierarchical_clustering(data):
    data['Genre'] = pd.to_numeric(data['Genre'], errors='coerce')

    data = data.replace([np.inf, -np.inf], np.nan)

    imputer = SimpleImputer(strategy='mean')
    data_imputed = imputer.fit_transform(data)

    Z = linkage(data_imputed, method='ward')

    plt.figure(figsize=(12, 6))
    dendrogram(Z, truncate_mode='level', p=5)
    plt.title('Dendrogram')
    plt.show()