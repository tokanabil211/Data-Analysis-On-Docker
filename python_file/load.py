import pandas as pd
import sys
from dpre import dpre
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python load.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    data = load_data(file_path)
    if data is not None:
        print("Data loaded successfully.")
        df=dpre(data)
