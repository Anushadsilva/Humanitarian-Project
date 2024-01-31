# Humanitarian-Project
Project Description : This project is to demonstrate data wrangling with Python. In this project we identify which Asian countries require most financial assistance from humanitarian groups. We need to organize the data using tools and techniques and also with the use of numpy and pandas library.

Dataset Description :
There are 2 dataset used in this project which contains information on the Asian Countries.
Columns: Country, health, income, child_mort, inflation, life_expec, total_fer, exports, imports, gdpp

Load the dataset:
Use read_csv to load the 2 datasets

Merge the dataset:
Using a common column merge the 2 dataset using merge() and display all the columns using print()

Finding & handling Duplicate data:
Use duplicate() to find the duplicates in the dataset and drop them using drop duplicates().

Find and handle missing data in dataset:
Using isnull() find the missing data and then use fillna() to fill the missing value with mean(imports) using mean()

Finding outliers:
Using the IQR method find the outliers
Use the quantile() to find the q1 and q3 values for the gdpp column

Export the data to CSV:
export the dataset to csv using to_csv method

Sorting:
Use the sorting() to sort child_mort column and display the top 5 using head() to get the list of asian countries that needs financial assistanceby humanitarian group

