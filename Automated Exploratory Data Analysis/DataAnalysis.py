import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data():
    
    file_path = r"D:\Alcamp\Automated Exploratory Data Analysis\large_sample_data.csv"
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded. Shape: {data.shape}")
        print(data.info())
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def summarize_data(data):
    print("\n--- Summary of Numerical Features ---")
    print(data.describe())
    
    print("\n--- Summary of Categorical Features ---")
    cat_features = data.select_dtypes(include=['object', 'category'])
    for col in cat_features.columns:
        print(f"\nColumn: {col}")
        print(cat_features[col].value_counts())
    
    print("\n--- Missing Data Overview ---")
    missing_data = data.isnull().mean() * 100
    print(missing_data[missing_data > 0])


def preprocess_data(data):
    
    for col in data.columns:
        if data[col].isnull().any():
            if data[col].dtype in ['int64', 'float64']:
                data[col].fillna(data[col].median(), inplace=True)
            else:
                data[col].fillna(data[col].mode()[0], inplace=True)
    
    
    cat_features = data.select_dtypes(include=['object', 'category'])
    for col in cat_features.columns:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
    
    
    num_features = data.select_dtypes(include=['int64', 'float64'])
    scaler = StandardScaler()
    data[num_features.columns] = scaler.fit_transform(num_features)
    
    print("\n--- Data Pre-processing Completed ---")
    return data


def visualize_data(data):
    num_features = data.select_dtypes(include=['int64', 'float64'])
    cat_features = data.select_dtypes(include=['object', 'category'])
    
    
    for col in num_features.columns:
        plt.figure(figsize=(10, 4))
        sns.histplot(data[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()
        
        plt.figure(figsize=(10, 4))
        sns.boxplot(x=data[col])
        plt.title(f"Boxplot of {col}")
        plt.show()
    
    
    for col in cat_features.columns:
        plt.figure(figsize=(10, 4))
        sns.countplot(y=data[col])
        plt.title(f"Count Plot of {col}")
        plt.show()
    
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()


def main():
    print("Automated EDA Tool")
    data = load_data()
    if data is not None:
        summarize_data(data)
        processed_data = preprocess_data(data)
        visualize_data(processed_data)

if __name__ == "__main__":
    main()
