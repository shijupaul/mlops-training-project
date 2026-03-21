import pandas as pd

def main():
    # Load the dataset
    df = pd.read_csv('data/data.csv')

    # Display the first few rows of the dataset
    print(df.head())

main()    