# generate_data.py

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

num_records = 100


customer_ids = np.random.randint(1000, 2000, num_records)
categories = ['Electronics', 'Clothing', 'Groceries', 'Books', 'Home', None]

data = []

for i in range(num_records):
    record = {
        "CustomerID": customer_ids[i],
        "TransactionID": f"T{i}",
        "PurchaseAmount": np.random.choice([np.random.uniform(10, 500), None, -50]),  # invalid + missing
        "ProductCategory": random.choice(categories),
        "TransactionDate": random.choice([
            datetime.now() - timedelta(days=random.randint(0, 365)),
            "invalid_date"
        ])
    }
    data.append(record)

df = pd.DataFrame(data)

# Add duplicates intentionally
df = pd.concat([df, df.sample(20)])

df.to_csv("customer_transactions.csv", index=False)

print("Dataset generated: customer_transactions.csv")
