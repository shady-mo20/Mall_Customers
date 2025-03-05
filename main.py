import pandas as pd
from load_data import load_data, preprocess_data
from eda import plot_age_group_distribution, plot_spending_score_distribution, plot_spending_score_pie, plot_spending_score_by_gender, plot_average_income_by_age, plot_correlation_heatmap
from kmeans_clustering import kmeans_clustering
from hierarchical_clustering import hierarchical_clustering

def main():
    data = load_data()
    data = preprocess_data(data)

    plot_age_group_distribution(data)
    plot_spending_score_distribution(data)
    plot_spending_score_pie(data)
    plot_spending_score_by_gender(data)
    plot_average_income_by_age(data)
    plot_correlation_heatmap(data)

    kmeans_clustering(data)
    hierarchical_clustering(data)

if __name__ == "__main__":
    main()