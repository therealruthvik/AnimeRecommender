import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
        # error bad lines will delete all rows and dropna will drop none values - for cleaning data

        required_cols = {'Name','Genres','sypnopsis'}

        missing = required_cols - set(df.columns) #checking if we missing any columns from required cols in csv file
        if missing:
            raise ValueError("Missing column in CSV File")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + "Overview: " + df["sypnopsis"] + "Genres: " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv



