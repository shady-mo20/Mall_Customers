أعتذر على الخطأ الذي وقع! إليك الملف كامل بصيغة **Markdown**:

```markdown
# Customer Segmentation - EDA and Clustering

## Overview
This project provides an exploratory data analysis (EDA) and clustering-based customer segmentation using a dataset of mall customers. The goal is to understand customer behavior and segment them into groups based on key features like age, annual income, and spending score. This analysis helps in identifying valuable customer groups, understanding their behavior, and making data-driven marketing decisions.

### Key Features:
- **Exploratory Data Analysis (EDA):** Analyzing and visualizing the key aspects of customer data.
- **K-means Clustering:** Using the K-means algorithm to segment customers into distinct groups based on their annual income and spending score.
- **Hierarchical Clustering:** Visualizing the results of hierarchical clustering using a dendrogram.
- **Elbow Method:** Finding the optimal number of clusters using the elbow method.
- **Correlation Analysis:** Analyzing correlations between variables like age, income, and spending scores.

---

## Table of Contents
1. [Installation](#installation)
2. [Dataset](#dataset)
3. [Usage](#usage)
4. [Results](#results)
5. [Clustering Techniques](#clustering-techniques)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

To run this project locally, you'll need to have Python installed. You can set up a Python environment with the following dependencies:

1. Clone this repository:

```bash
git clone https://github.com/yourusername/customer-segmentation.git
cd customer-segmentation
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Dataset

This project uses a dataset of mall customers. The dataset contains the following columns:

- **CustomerID:** Unique ID for each customer (dropped in preprocessing).
- **Genre:** Gender of the customer (Male/Female).
- **Age:** Age of the customer.
- **Annual Income (k$):** Annual income of the customer in thousands of dollars.
- **Spending Score (1-100):** Spending score assigned to the customer (higher score indicates higher spending behavior).

The dataset is stored in `Mall_Customers.csv` and should be placed in the same directory as the project scripts.

---

## Usage

After installing the dependencies and setting up the environment, you can run the scripts in the following sequence:

1. **Load Data:**
   - The `load_data.py` script loads and preprocesses the customer dataset, handles missing values, and maps categorical values.

2. **Exploratory Data Analysis (EDA):**
   - The `eda.py` script generates various plots to explore the distribution of data, including:
     - Age group distribution
     - Spending score distribution
     - Spending score by gender
     - Average income by age group

3. **Clustering:**
   - **K-means Clustering:** The `kmeans_clustering.py` script segments customers based on their annual income and spending score using the K-means algorithm.
   - **Hierarchical Clustering:** The `hierarchical_clustering.py` script performs hierarchical clustering and visualizes the results with a dendrogram.

4. **Main Script:**
   - The `main.py` script serves as the entry point to run the entire analysis, generating visualizations and performing clustering on the customer data.

To run the analysis:

```bash
python main.py
```

---

## Results

### 1. Most Common Age Groups of Customers:
The bar chart displays the distribution of customers across age groups. The "26-35" age group has the highest number of customers, followed by "18-25", with "65+" being the least represented.

### 2. Spending Score Distribution:
A histogram with a slight peak around the 30-50 spending score range helps identify how customers are distributed based on their spending behaviors.

### 3. Spending Score by Gender:
A box plot showing the distribution of spending scores for males and females, highlighting that males generally have slightly lower spending scores on average compared to females.

### 4. K-means Clustering:
The K-means clustering scatter plot reveals five well-separated customer segments based on annual income and spending score.

### 5. Elbow Method:
The elbow method plot helps determine the optimal number of clusters for K-means clustering, suggesting five clusters as the best choice.

### 6. Correlation Heatmap:
The correlation heatmap shows weak correlations between variables such as age, income, and spending score, indicating limited relationships among these features.

### 7. Average Annual Income by Age Group:
The bar chart highlights the average annual income for each age group, with "26-35" and "36-45" groups having the highest incomes.

### 8. Customer Distribution by Spending Score:
A pie chart illustrating the proportion of customers in different spending score ranges, with the majority falling within the "40-59" range.

### 9. Dendrogram:
The hierarchical clustering dendrogram visually groups customers based on their similarities, helping to identify natural clusters within the data.

---

## Clustering Techniques

### 1. K-means Clustering:
   - **Goal:** Segment customers into distinct groups based on their spending score and annual income.
   - **Method:** The K-means algorithm was used to cluster the customers into five distinct groups. The optimal number of clusters was determined using the Elbow Method.

### 2. Hierarchical Clustering:
   - **Goal:** Understand the hierarchical relationships between customer segments.
   - **Method:** The Ward linkage method was used to generate a dendrogram, visually representing the hierarchical clusters based on customer features.

---

## Contributing

We welcome contributions to this project. If you would like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new pull request

Please make sure your code follows the [PEP 8](https://pep8.org/) style guide and include tests for any new features or bug fixes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Pandas** and **NumPy** for data manipulation and analysis.
- **Matplotlib** and **Seaborn** for visualization.
- **Scikit-learn** for clustering and data preprocessing.
```

الآن الملف مكتوب بشكل كامل باستخدام **Markdown**، يمكنك نسخه مباشرة إلى ملف `README.md` في مشروعك على GitHub!
