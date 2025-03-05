import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_age_group_distribution(data):
    data_plot = data.copy()
    age_bins = [18, 26, 36, 46, 56, 66, 100]
    data_plot['Age Group'] = pd.cut(data['Age'], bins=age_bins, labels=["18-25", "26-35", "36-45", "46-55", "56-65", "65+"])

    plt.figure(figsize=(10, 6))
    sns.countplot(data=data_plot, x='Age Group', palette='viridis')
    plt.title('Most Common Age Groups of Customers')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.show()

def plot_spending_score_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Spending Score (1-100)'], kde=True, color='green')
    plt.title('Spending Score Distribution')
    plt.xlabel('Spending Score (1-100)')
    plt.ylabel('Frequency')
    plt.show()

def plot_spending_score_pie(data):
    spending_counts = data['Spending Score (1-100)'].value_counts(bins=5)
    spending_labels = [f'{int(bin.left)}-{int(bin.right)}' for bin in spending_counts.index]

    plt.figure(figsize=(8, 8))
    plt.pie(spending_counts, labels=spending_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Customer Distribution by Spending Score')
    plt.show()

def plot_spending_score_by_gender(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='Genre', y='Spending Score (1-100)', palette='Set1')
    plt.title('Spending Score by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Spending Score (1-100)')
    plt.show()

def plot_average_income_by_age(data):
    data_plot = data.copy()
    # Ensure 'Age Group' column is created
    age_bins = [18, 26, 36, 46, 56, 66, 100]
    data_plot['Age Group'] = pd.cut(data['Age'], bins=age_bins, labels=["18-25", "26-35", "36-45", "46-55", "56-65", "65+"])
    
    average_income_by_age = data_plot.groupby('Age Group')['Annual Income (k$)'].mean()

    plt.figure(figsize=(10, 6))
    average_income_by_age.plot(kind='bar', color='purple')
    plt.title('Average Annual Income by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Annual Income (k$)')
    plt.show()

def plot_correlation_heatmap(data):
    numeric_df = data.select_dtypes(include=[np.number])
    corr = numeric_df.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()