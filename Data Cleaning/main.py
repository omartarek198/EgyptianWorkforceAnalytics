import pandas as pd

def Load_Data(file_path: str) -> pd.DataFrame:	
    df = pd.read_excel(file_path)
    return df

def Drop_Columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:  
    df = df.drop(columns=columns)
    return df
def TrimHeaders(df: pd.DataFrame) -> pd.DataFrame:  
    df.columns = df.columns.str.replace(' ', '')
    print(df.columns)
    return df
def Clean_YearsOfExperience(df: pd.DataFrame) -> pd.DataFrame:
    numeric_filter = pd.to_numeric(df["YearsofExperiences"], errors='coerce').notnull()

    df.loc[~numeric_filter, "YearsofExperiences"] = df.loc[~numeric_filter, "YearsofExperiences"].str.upper()
    df.loc[~numeric_filter, "YearsofExperiences"] = df.loc[~numeric_filter, "YearsofExperiences"].str.replace("YEARS", "")
    df.loc[~numeric_filter, "YearsofExperiences"] = df.loc[~numeric_filter, "YearsofExperiences"].str.replace("YEAR", "")
    df.loc[~numeric_filter, "YearsofExperiences"] = df.loc[~numeric_filter, "YearsofExperiences"].str.replace(">", "")
    df.loc[~numeric_filter, "YearsofExperiences"] = df.loc[~numeric_filter, "YearsofExperiences"].str.replace("<", "")
    df.loc[~numeric_filter, "YearsofExperiences"] = df.loc[~numeric_filter, "YearsofExperiences"].str.replace("~", "")

    df.loc[numeric_filter, "YearsofExperiences"] = pd.to_numeric(df.loc[numeric_filter, "YearsofExperiences"])

    df.loc[numeric_filter, "MonthsOfExperience"] = df.loc[numeric_filter, "YearsofExperiences"] * 12


    PercentageOfNan = df["MonthsOfExperience"].isna().sum() / len(df["MonthsOfExperience"]) * 100   
    
    print(f"Percentage of NaN in MonthsOfExperience: {PercentageOfNan}%")
    return df


def Save_Data(df: pd.DataFrame, file_path: str) -> None:        
    df.to_excel(file_path, index=False)
    return None

def Clean_Data(file_path: str) -> None:        
    df = Load_Data(file_path)
    df = Drop_Columns(df, ["طابع زمني"])
    df = TrimHeaders(df)
    df = Clean_YearsOfExperience(df)
    
    Save_Data(df, "Data\CleanData2.xlsx")
    print(df.head())
    return None

def main():
    file_path = "Data\RawData.xlsx"
    Clean_Data(file_path)   
    pass

main()