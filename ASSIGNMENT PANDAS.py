#!/usr/bin/env python
# coding: utf-8

# PandasAssignment
# Q1. How do you load a CSV file into a Pandas DataFrame?
# 
# import pandas as pd
# 
# df = pd.read_csv('data.csv')
# 
# Q2. How do you check the data type of a column in a Pandas DataFrame?
# 
# To check the data type in pandas DataFrame we can use the “dtype” attribute. The attribute returns a series with the data type of each column.
# 
# result = df.dtypes
# 
# Q3. How do you select rows from a Pandas DataFrame based on a condition?
# 
# Q4. How do you rename columns in a Pandas DataFrame?
# 
# One way of renaming the columns in a Pandas Dataframe is by using the rename() function. This method is quite useful when we need to rename some selected columns because we need to specify information only for the columns which are to be renamed. 
# 
# Q5. How do you drop columns in a Pandas DataFrame?
# 
# The drop() method removes the specified row or column. By specifying the column axis ( axis='columns' ), the drop() method removes the specified column. By specifying the row axis ( axis='index' ), the drop() method removes the specified row.
# 
# Q6. How do you find the unique values in a column of a Pandas DataFrame?
# 
# You can get unique values in column (multiple columns) from pandas DataFrame using unique() or Series. unique() functions. unique() from Series is used to get unique values from a single column and the other one is used to get from multiple columns.
# 
# Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
# 
# df['column name'].isna().sum()
# 
# Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
# 
# In order to fill null values in a datasets, we use fillna(), replace() and interpolate() function these function replace NaN values with some value of their own.
# 
# Q9. How do you concatenate two Pandas DataFrames?
# 
# The concat() function in pandas is used to append either columns or rows from one DataFrame to another. The concat() function does all the heavy lifting of performing concatenation operations along an axis while performing optional set logic (union or intersection) of the indexes (if any) on the other axes.
# 
# Q10. How do you merge two Pandas DataFrames on a specific column?
# 
# We can merge two Pandas DataFrames on certain columns using the merge function by simply specifying the certain columns for merge. 
# 
# Syntax: DataFrame.merge(right, how=’inner’, on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, copy=True, indicator=False, validate=None)
# 
# Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
# Dataframe.aggregate() function is used to apply some aggregation across one or more column. Aggregate using callable, string, dict, or list of string/callables. Most frequently used aggregations are:
# 
# sum: Return the sum of the values for the requested axis
# min: Return the minimum of the values for the requested axis
# max: Return the maximum of the values for the requested axis
# 
# Syntax: DataFrame.aggregate(func, axis=0, *args, **kwargs)
# 
# 
# Parameters:
# func : callable, string, dictionary, or list of string/callables. Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. For a DataFrame, can pass a dict, if the keys are DataFrame column names.
# axis : (default 0) {0 or ‘index’, 1 or ‘columns’} 0 or ‘index’: apply function to each column. 1 or ‘columns’: apply function to each row.
# 
# Returns: Aggregated DataFrame
# 
# For link to CSV file Used in Code, click here
# 
# Example: Aggregate ‘sum’ and ‘min’ function across all the columns in data frame.
# 
# import pandas as pd
# df = pd.read_csv("nba.csv")
# df[:10]
# 
# 
# Aggregation works with only numeric type columns.
# 
# df.aggregate(['sum', 'min'])
# 
# Output:
# For each column which are having numeric values, minimum and sum of all values will be found.
#  
# 
# Q12. How do you pivot a Pandas DataFrame?
# 
# The pivot() function is used to reshaped a given DataFrame organized by given index / column values. This function does not support data aggregation, multiple values will result in a MultiIndex in the columns. Column to use to make new frame's index. If None, uses existing index.
# 
# Pivot can be specified by giving the index and column name as argument.
# 
# example:
# df.pivot(index="date",column = "city")
# 
# Q13. How do you change the data type of a column in a Pandas DataFrame?
# 
# Change column type in pandas using DataFrame.apply() 
# We can pass pandas.to_numeric, pandas.to_datetime, and pandas.to_timedelta as arguments to apply the apply() function to change the data type of one or more columns to numeric, DateTime, and time delta respectively. 
# 
# Q14. How do you sort a Pandas DataFrame by a specific column?
# 
# To sort the DataFrame based on the values in a single column, you’ll use .sort_values(). By default, this will return a new DataFrame sorted in ascending order. It does not modify the original DataFrame.
# 
# Sorting by a Column in Ascending Order
# To use .sort_values(), you pass a single argument to the method containing the name of the column you want to sort by.
# By passing False to ascending, you reverse the sort order. Now your DataFrame is sorted in descending order
# 
# Q15. How do you create a copy of a Pandas DataFrame?
# 
# The copy() method returns a copy of the DataFrame. By default, the copy is a "deep copy" meaning that any changes made in the original DataFrame will NOT be reflected in the copy.
# 
# Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
# 
# Q17. How do you calculate the mean of a column in a Pandas DataFrame?
# 
# To get column average or mean from pandas DataFrame use either mean() and describe() method. The DataFrame. mean() method is used to return the mean of the values for the requested axis.
# 
# Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
# 
# In pandas, the std() function is used to find the standard Deviation of the series. The mean can be simply defined as the average of numbers. In pandas, the mean() function is used to find the mean of the series.
# 
# Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
# 
# Correlation is used to summarize the strength and direction of the linear association between two quantitative variables. It is denoted by r and values between -1 and +1. A positive value for r indicates a positive association, and a negative value for r indicates a negative association.
# 
# By using corr() function we can get the correlation between two columns in the dataframe.
# 
# Q20. How do you select specific columns in a DataFrame using their labels?
# 
# This is the most basic way to select a single column from a dataframe, just put the string name of the column in brackets. Returns a pandas series. Passing a list in the brackets lets you select multiple columns at the same time
# 
# Q21. How do you select specific rows in a DataFrame using their indexes?
# 
# The iloc[ ] is used for selection based on position. It is similar to loc[] indexer but it takes only integer values to make selections. 
# 
# Q22. How do you sort a DataFrame by a specific column?
# 
# To sort the DataFrame based on the values in a single column, you'll use . sort_values() . By default, this will return a new DataFrame sorted in ascending order. It does not modify the original DataFrame.
# 
# Q23. How do you create a new column in a DataFrame based on the values of another column?
# 
# Consider we are creating a new col called total which is sum of col A and B
# 
# df["total"]=df['A']+df['B']
# 
# Q24. How do you remove duplicates from a DataFrame?
# 
# The drop_duplicates() method removes duplicate rows. Use the subset parameter if only some specified columns should be considered when looking for duplicates.
# 
# Q25. What is the difference between .loc and .iloc in Pandas?
# 
# The main distinction between loc and iloc is: loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer position-based, so you have to specify rows and columns by their integer position values (0-based integer position)

# In[ ]:




