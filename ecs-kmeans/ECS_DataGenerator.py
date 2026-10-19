# generate_data.py

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

num_records = 1000     
num_customers = 100 

categories = ['Electronics', 'Clothing', 'Groceries', 'Books', 'Home']

data = []

for transaction_id in range(num_records):

    customer_id = random.randint(1000, 1000 + num_customers - 1)

    record = {
        "CustomerID": customer_id,
        "TransactionID": f"T{transaction_id}",

        # mix of valid, missing, invalid values
        "PurchaseAmount": np.random.choice([
            round(np.random.uniform(10, 500), 2),
            None,
            -50
        ]),

        "ProductCategory": random.choice(categories + [None]),

        "TransactionDate": random.choice([
            datetime.now() - timedelta(days=random.randint(0, 365)),
            "invalid_date"
        ])
    }

    data.append(record)

df = pd.DataFrame(data)

# Optional: shuffle for randomness
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("customer_transactions.csv", index=False)

print("Dataset generated with EXACTLY 1000 records!")
