import pandas as pd


file_path = 'final_filtered_countries.csv'
df = pd.read_csv(file_path)

print("Original DataFrame head:")
print(df.head())
print(f"\nOriginal DataFrame shape: {df.shape}")


columns_to_drop = ['GiniIndex', 'HomicideRate', 'PovertyShare']

columns_to_drop = [col for col in columns_to_drop if col in df.columns]
df_clean = df.drop(columns=columns_to_drop)


df_clean.columns = [
    col.strip().replace(' ', '_').replace('-', '_').replace(':', '')
    .replace(',', '').replace('(', '').replace(')', '')
    for col in df_clean.columns
]

print("\nDataFrame head after initial cleaning and renaming columns:")
print(df_clean.head())


def remove_outliers_iqr(df_input, year_col='Year'):
    df_out = pd.DataFrame()

    df_input[year_col] = df_input[year_col].astype(int)
    years = sorted(df_input[year_col].unique()) 

    for year in years:
        df_year = df_input[df_input[year_col] == year].copy()
        
        numeric_cols = df_year.select_dtypes(include=['float64', 'int64']).columns
        
        for col in numeric_cols:
            if col == year_col: 
                continue
            
          
            if df_year[col].isnull().all():
                print(f"Skipping column '{col}' for year {year} as all values are NaN.")
                continue

            Q1 = df_year[col].quantile(0.25)
            Q3 = df_year[col].quantile(0.75)
            IQR = Q3 - Q1

           
            if IQR == 0:
               
                lower_bound = Q1
                upper_bound = Q3
            else:
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
            
           
            df_year = df_year[(df_year[col] >= lower_bound) & (df_year[col] <= upper_bound) | df_year[col].isnull()]
            
        df_out = pd.concat([df_out, df_year], axis=0)
        
    return df_out.reset_index(drop=True)


cleaned_df_iqr = remove_outliers_iqr(df_clean.copy()) # Use .copy() to avoid SettingWithCopyWarning

print("\nDataFrame head after removing outliers:")
print(cleaned_df_iqr.head())
print(f"\nDataFrame shape after removing outliers: {cleaned_df_iqr.shape}")


if df_clean['Year'].nunique() > 0:
    first_year = sorted(df_clean['Year'].unique())[0]
    original_rows_first_year = df_clean[df_clean['Year'] == first_year].shape[0]
    cleaned_rows_first_year = cleaned_df_iqr[cleaned_df_iqr['Year'] == first_year].shape[0]
    print(f"\nYear {first_year}:")
    print(f"  Original rows: {original_rows_first_year}")
    print(f"  Rows after outlier removal: {cleaned_rows_first_year}")
    print(f"  Rows removed: {original_rows_first_year - cleaned_rows_first_year}")

