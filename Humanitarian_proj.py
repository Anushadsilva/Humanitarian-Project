
import pandas as pd
economies_df1 = pd.read_csv('economies1.csv')
economies_df2 = pd.read_csv('economies2.csv')
pd.set_option('display_max_columns', None)
economies_df = economies_df.merge(economies_df1,economies_df2, how = 'left', on = "Country")


economies_df_duplicates = economies_df[economies_df_duplicated()]
print(economies_df_duplicates)


economies_df = economies_df.drop_duplicates()

economies_df_missing = economies_df[economies_df.isnull().any(axis = 1)]
print(economies_df_missing)

economies_df['imports'].fillna(economics_df['imports'].mean(), inplace = True )
print(economies_df)


Q1 = economies_df.quantile(0.25)
Q3 = economies_df.quantile(0.75)
IQR = Q3 - Q1
economies_df_outliers = economies_df[((economies_df < (Q1 - 1.5 * IQR)) / (economies_df > (Q3 + 1.5 * IQR))).any(axis = 1)]
print(economies_df_outliers)

economies_df.to_csv('economies_clean.csv', encoding=UTF-8 , index = false)
final_df = pd.read_csv('economies_clean.csv')
print(final_df(head()))

financial_df = final_df.sort_values(by ='child_mort',ascending = False)
financial_df = financial_df.head()
print(financial_df)



