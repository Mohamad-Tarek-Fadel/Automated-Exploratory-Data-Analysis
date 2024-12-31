import pandas as pd
import random


data = {
    'Name': [f'Person_{i}' for i in range(1, 1001)],  
    'Age': [random.randint(18, 65) for _ in range(1000)],  
    'Gender': [random.choice(['Male', 'Female']) for _ in range(1000)],  
    'Department': [random.choice(['HR', 'IT', 'Finance', 'Marketing']) for _ in range(1000)], 
    'Salary': [random.randint(30000, 120000) for _ in range(1000)],  
    'Join_Date': pd.date_range(start='2010-01-01', periods=1000, freq='W').strftime('%Y-%m-%d').tolist(),  
    'Performance_Score': [round(random.uniform(1.0, 5.0), 2) for _ in range(1000)],  
    'Promoted': [random.choice([0, 1]) for _ in range(1000)]  
}


df = pd.DataFrame(data)


file_path = r"D:\Alcamp\Automated Exploratory Data Analysis\large_sample_data.csv"
df.to_csv(file_path, index=False)

print(f"File created successfully at: {file_path}")
