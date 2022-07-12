####-- Intro Pandas is a great library in Python that gives us the power and opportunity to manipulate and analyze our data 
    #- this 3 sections below are the main core of Pandas:
        #A - Data Understanding
        #B - Data Cleaning
        #C - Data Analisys and Manipulation

##A - Data Understanding
#1 import the file directly from the github website

from re import T
import pandas as pd

url_data = (r'https://raw.githubusercontent.com/Fyevenes90/Useful-Pandas-methods-for-Data-Science/main/MKT_data.csv')

data_csv = pd.read_csv(url_data)
data_csv.shape

#2- df.head() returns the first 5 rows
data_csv.head()

#3- df.tail() return the last 5 rows
data_csv.tail()

#4- df.info() #provide info about row,columns#, data types, not nulls,
#So we can easily answer these questions :
    ###---Are there any missing values?
    ###---Is there any issue with the data type?

data_csv.info()

#5 df.describe() // returns stadistical summary of our numerical data by default. it includes count, mean, standar deviation, mini 1 st quantile, 2nd, 3rd, max values
data_csv.describe()

#6 columns  / show the columns name in a df
data_csv.columns


#7 lets get the count of null in the dataframe
data_csv.isnull().sum()

#8 lets check for duplicated
data_csv[data_csv.duplicated(keep =False)]


##B - Data Cleaning

#9 dropna() 
new_df = data_csv.dropna(inplace=True)
new_df.head()  

#10 df.drop_duplicates(inplace=True) / # inplace = True means we removed permanently.
data_csv.drop_duplicates(inplace=True) 
data_csv.shape

#11 dtypes / brings the data type per column / we can see that Dt_Customer should be a date            
data_csv.dtypes


#12 .to_datetime()
data_csv['Dt_Customer'] = pd.to_datetime(data_csv['Dt_Customer'])

#13 Lets create a new column with year, month, date
data_csv['year_customer'] = data_csv['Dt_Customer'].dt.year #year 
data_csv['month_customer'] = data_csv['Dt_Customer'].dt.month #month
data_csv['day_customer'] = data_csv['Dt_Customer'].dt.dayofweek #dayofweek as number 0 =monday & 6 = sunday


##C Data Analysis and Manipulation

#14 value_count
data_csv['Education'].value_counts()

#15 unique / will tell you the list unique items are in a column
data_csv['Education'].unique()

#16 nunique / will tell you how many # unique items are in a column
data_csv['Education'].nunique()

#17 sort_values()
data_csv.sort_values(by='Income', ascending=False)

#18 query / this is for fiter data
data_csv.query(' Income>666665.0 ')

#19 lets use the df[df['column_name'] > 666665]
data_csv[data_csv['Income'] > 666665]

#another alternative --> loc
data_csv.loc[data_csv['Income']> 666665]

#20 group by with aggregate funtions like mean
data_csv.groupby('Education')['Income'].mean()
    #Alternative way to do the same
data_csv.groupby('Education').agg({'Income':'mean'})


#21 Pivot table 
pd.pivot_table(data = data_csv, values = 'Income', index= 'Education', columns='Marital_Status')

#22 apply / this method gives us the ability to use any function inside
data_csv['Response'].unique() #check what we have in column Response
data_csv['Response'].apply(lambda x: 'Accepted' if x==1 else 'No Accepted')

#23 replace
data_csv.columns
data_csv['Marital_Status'].unique()
data_csv['Marital_Status'].replace(to_replace= ['Divorced','Widow', 'Alone','Absurd', 'YOLO'], value = 'Single')

#24 Lets export the data to csv
data_csv.to_csv('DF_MKT.csv', index= False)
