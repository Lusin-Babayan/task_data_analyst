import pandas as pd

with open("Task_ Data_ Analyst.csv", "r", encoding='utf8') as file:

    file_csv = pd.read_csv(file)
    df = pd.DataFrame(file_csv) 
    print(df.columns)

    print(df['Row ID'].isnull().unique())
    for colname in df.columns:
        print(colname, df[df[colname].isnull() == True])

# To address missing values in the dataset, we can utilize the following approaches:
# 1. Impute with Mean or Median Values: Replace the missing values with the mean or median of the corresponding column.
# 2. Remove Rows with Missing Values: Delete rows that contain missing values. 

# In our case I would suggest drop rows with missing values as the proportion of missing values is small and does not substantially impact the dataset's size.

    df = df.dropna(subset=df.columns)
    df = df.dropna(subset=[' Bet Amount in Original Currency ', 'WinAmount in Original Currency'])
    print(df['Row ID'].isnull().unique())
    for colname in df.columns:
        print(colname, df[df[colname].isnull() == True])


    print(df['PlayerID'].is_unique)

    df['Bet Amount'] = df[' Bet Amount in Original Currency '].astype(str).str.replace(',', '').astype(float) * df['CurrencyRate'].astype(str).str.replace(',', '').astype(float)
    df['Win Amount'] = df['WinAmount in Original Currency'].astype(str).str.replace(',', '').astype(float) * df['CurrencyRate'].astype(str).str.replace(',', '').astype(float)
    print(df[[' Bet Amount in Original Currency ','CurrencyRate','Bet Amount']])
    print(df['Age'].min())
    df["Age Group"] = pd.cut(df['Age'],
                      bins=[df['Age'].min()-1, 39, 59, df['Age'].max()],
                      labels=['Adult(20-39)', 'Middle Age Adult(40-59)', 'Senior Adult(60+)'])
    
    df.to_excel("Task_ Data_ Analyst_Processedfgfg.xlsx")


