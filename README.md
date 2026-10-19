Ecommerce Customer Segmentation:

A machine learning project that groups e-commerce customers into segments based on their purchasing behavior using K-Means clustering. 
The goal is to help businesses understand customer patterns and support more personalized marketing, recommendations, and customer-retention strategies.

Problem Statement:

Many online platforms send the same promotions to all customers. This can lead to:
- Low conversion rates
- Poor customer engagement
- Inefficient marketing spending
This project explores customer segmentation using three behavioral features: purchase frequency, average order value, and product-category diversity.


💡 Solution
The workflow processes transaction data, cleans and transforms it into customer-level features, standardizes the features, 
and applies K-Means clustering with K = 4. Each customer is assigned a cluster label, 
and the resulting segmentation is exported to a CSV file for further analysis.


✨ Key Features
- Load transaction data from a CSV file using Pandas
- Remove duplicate records
- Handle missing purchase amounts using the median
- Replace missing product categories with "Unknown"
- Filter out non-positive purchase amounts
- Convert transaction dates and remove invalid dates
- Create customer-level behavioral features
- Standardize features using StandardScaler
- Segment customers using K-Means clustering
- Export features and cluster labels to CSV files

  
🧰 Tech Stack
- Python
- Pandas — data loading, cleaning, and aggregation
- NumPy — numerical computing
- Scikit-learn — feature scaling and K-Means clustering

  
📂 Dataset
The presentation describes a synthetic dataset of 1,000 customer transactions with fields such as:

Field                  Description
CustomerID	           Identifier for a customer
TransactionID	         Identifier for a transaction
PurchaseAmount	       Amount spent in a transaction
ProductCategory	       Category of the purchased product
TransactionDate	       Date of the transaction
The dataset is synthetic and is intended for demonstrating the workflow, not for making claims about real customer behavior.


⚙️ Workflow
1. Data collection — generate or provide transaction data in CSV format.
2. Data loading — read the CSV into a Pandas DataFrame.
3. Data sanitization — remove duplicates, handle missing values, filter invalid purchase amounts, and validate dates.
4. Feature engineering — aggregate transactions by customer to calculate:
   - Purchase Frequency: number of transactions per customer
   - Average Order Value: mean purchase amount per customer
   - Category Diversity: number of unique product categories purchased
5. Data normalization — use StandardScaler so features with different scales contribute more fairly to clustering.
6. K-Means clustering — fit K-Means with four clusters and assign a cluster label to each customer.
7. Output generation — save the customer features and cluster labels to CSV files.
   
Architecture:

Transaction CSV
      ↓
Load Data (Pandas)
      ↓
Clean & Validate Data
      ↓
Customer-Level Feature Engineering
      ↓
StandardScaler
      ↓
K-Means (K = 4)
      ↓
Cluster Labels
      ↓
segmented_customers.csv
      ↓
Customer Analysis & Marketing Use Cases



🗂️ Expected Project Files
The workflow described in the presentation uses these files:
.
├── ecs_clustering.py
├── customer_transactions.csv
├── features.csv
└── segmented_customers.csv
- ecs_clustering.py — main Python workflow
- customer_transactions.csv — input transaction dataset
- features.csv — customer-level engineered features
- segmented_customers.csv — customer features with assigned cluster labels
The CSV files are generated or supplied at runtime; include them in the repository only if you intend to publish them.


🚀 Getting Started

1. Clone the repository
git clone <your-repository-url>
cd <your-repository-folder>

2. Install dependencies
python -m pip install pandas numpy scikit-learn

4. Prepare the input data
Place a CSV file named customer_transactions.csv in the project directory. It should contain the columns used by the script:
- CustomerID
- TransactionID
- PurchaseAmount
- ProductCategory
- TransactionDate
  
4. Run the project
python ecs_clustering.py
The workflow is designed to write features.csv and segmented_customers.csv to the working directory.

Note: Check that the function and column names in your final Python script match the dataset schema before running it. The code excerpts in the presentation contain some naming inconsistencies, so the exact script may need adjustment.



📊 Output
The segmented output contains customer-level features and a Cluster label. These labels indicate the cluster assigned by the algorithm; cluster numbers do not automatically correspond to business categories such as “VIP” or “discount-sensitive.” Those interpretations require examining the characteristics of each cluster.

The presentation proposes using the results to support:
- Personalized product recommendations
- Targeted marketing campaigns
- Customer-retention strategies
🧪 Testing
The project presentation lists unit testing and integration testing as testing stages. Before relying on the results, verify:
- The input file exists and has the required columns
- Missing and invalid values are handled as expected
- Feature aggregation produces one row per customer
- The clustering step returns a label for each customer
- Output CSV files are created with the expected columns
No quantitative model-evaluation results are specified in the presentation.


⚠️ Limitations
- Uses synthetic data rather than verified real-world transactions
- Limited dataset size and a small set of behavioral features
- The number of clusters is fixed at four
- Results may be sensitive to centroid initialization and outliers
- K-Means works best for cluster structures suited to its assumptions
- No model-evaluation metrics are reported
- No real-time processing or business-system integration
- Cluster labels are not automatically translated into business interpretations
- Data quality and preprocessing affect the results
🔮 Future Enhancements
- Integrate real-time transaction data
- Compare K-Means with DBSCAN and hierarchical clustering
- Add recommendation-system capabilities for personalized product suggestions
- Build an interactive dashboard using Power BI or Tableau
- Integrate with e-commerce platforms to support marketing workflows
- Evaluate clustering quality using appropriate metrics and validate results on real-world data

  
🌍 Potential Applications
The segmentation approach could be adapted to other domains:
- Banking and FinTech: customer and credit-risk segmentation
- OTT platforms: grouping users by viewing habits and genre preferences
- Food delivery: identifying cuisine preferences and ordering patterns
- Retail: distinguishing frequent shoppers and spending patterns
- Subscription services: exploring usage patterns associated with retention
- Digital marketing: improving audience targeting
These are potential applications of the general approach, not outcomes validated by this project.


👥 Team
Group A — GITAM, BTech (CSE)

Team member	Contributions listed in the presentation
Manasvi	Application design, feature engineering, testing, and documentation
Nishi Ranvitha	K-Means clustering, testing, and documentation
Mythily	Data sanitization, testing, and documentation
Hitesh	Data generation, testing, and documentation
Tilak Raj	Data loading, testing, and documentation


📚 References
- Scikit-learn: Clustering
- Pandas Documentation
- NumPy Documentation
- IBM: What is clustering?
- Python
- Jupyter
- Visual Studio Code

  
📄 Project Note
This is an educational project demonstrating a customer-segmentation workflow with synthetic transaction data. It is a decision-support prototype, not a production-ready marketing system.
Built as a BTech CSE project at GITAM.
