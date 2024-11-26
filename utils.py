import pandas as pd


def read_dat_file(file_path, column_names, delimiter='::'):
    """Read a '.dat' file into a DataFrame with custom column names."""
    
    try:
        df = pd.read_csv(file_path, sep=delimiter, header=None, names=column_names, engine='python')
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
