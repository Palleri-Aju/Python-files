'''                    
                        Experiment -14
Name :
Class: SE-IT
Div  :
Roll number:
--------------------------------------

Topic- Pandas in Python
AIM- Write a program to load data from .csv file and use different pandas function to clean and evaluate data.
'''
import pandas as pd

df = pd.read_csv('dirtydata.csv')
print("Original Dataset :")
print(df.to_string())

#Replace null values in calories column with mean value
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

#Convert all date column values to datetime format
df['Date'] = pd.to_datetime(df['Date'])

#Drop row where Date column contains NULL
df.dropna(subset=['Date'], inplace = True)

#Replace value of duration value in Row 7 by most frequent value in Duration column
x = df["Duration"].mode()[0]
df.loc[7, 'Duration'] = x

#remove duplicate rows from records
df.drop_duplicates(inplace = True)

print("-------------------------------------------------------------------------")
print("Cleaned Dataset :")
print(df.to_string())

#find the shape of dataset
print("Shape of dataset :")
print(df.shape)
print("Top 5 rows of dataset :")
print(df.head())
print("Last 5 rows of dataset :\n")
print(df.tail())
print("Any random 5 rows of dataset :\n")
print(df.sample(5))
print("Short statistic of dataset :\n")
print(df.describe())

'''
Output:

Original Dataset :

    Duration          Date  Pulse  Maxpulse  Calories
0         60  '2020/12/01'    110       130     409.1
1         60  '2020/12/02'    117       145     479.0
2         60  '2020/12/03'    103       135     340.0
3         45  '2020/12/04'    109       175     282.4
4         45  '2020/12/05'    117       148     406.0
5         60  '2020/12/06'    102       127     300.0
6         60  '2020/12/07'    110       136     374.0
7        450  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
9         60  '2020/12/10'     98       124     269.0
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
18        45  '2020/12/18'     90       112       NaN
19        60  '2020/12/19'    103       123     323.0
20        45  '2020/12/20'     97       125     243.0
21        60  '2020/12/21'    108       131     364.2
22        45           NaN    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60      20201226    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132       NaN
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
-------------------------------------------------------------------------
Cleaned Dataset :

    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130    409.10
1         60 2020-12-02    117       145    479.00
2         60 2020-12-03    103       135    340.00
3         45 2020-12-04    109       175    282.40
4         45 2020-12-05    117       148    406.00
5         60 2020-12-06    102       127    300.00
6         60 2020-12-07    110       136    374.00
7         60 2020-12-08    104       134    253.30
8         30 2020-12-09    109       133    195.10
9         60 2020-12-10     98       124    269.00
10        60 2020-12-11    103       147    329.30
11        60 2020-12-12    100       120    250.70
13        60 2020-12-13    106       128    345.30
14        60 2020-12-14    104       132    379.30
15        60 2020-12-15     98       123    275.00
16        60 2020-12-16     98       120    215.20
17        60 2020-12-17    100       120    300.00
18        45 2020-12-18     90       112    304.68
19        60 2020-12-19    103       123    323.00
20        45 2020-12-20     97       125    243.00
21        60 2020-12-21    108       131    364.20
23        60 2020-12-23    130       101    300.00
24        45 2020-12-24    105       132    246.00
25        60 2020-12-25    102       126    334.50
26        60 2020-12-26    100       120    250.00
27        60 2020-12-27     92       118    241.00
28        60 2020-12-28    103       132    304.68
29        60 2020-12-29    100       132    280.00
30        60 2020-12-30    102       129    380.30
31        60 2020-12-31     92       115    243.00
Shape of dataset :
(30, 5)

Top 5 rows of dataset :
   Duration       Date  Pulse  Maxpulse  Calories
0        60 2020-12-01    110       130     409.1
1        60 2020-12-02    117       145     479.0
2        60 2020-12-03    103       135     340.0
3        45 2020-12-04    109       175     282.4
4        45 2020-12-05    117       148     406.0

Last 5 rows of dataset :
    Duration       Date  Pulse  Maxpulse  Calories
27        60 2020-12-27     92       118    241.00
28        60 2020-12-28    103       132    304.68
29        60 2020-12-29    100       132    280.00
30        60 2020-12-30    102       129    380.30
31        60 2020-12-31     92       115    243.00

Any random 5 rows of dataset :
    Duration       Date  Pulse  Maxpulse  Calories
21        60 2020-12-21    108       131    364.20
4         45 2020-12-05    117       148    406.00
13        60 2020-12-13    106       128    345.30
3         45 2020-12-04    109       175    282.40
18        45 2020-12-18     90       112    304.68

Short statistic of dataset :
        Duration       Pulse    Maxpulse    Calories
count  30.000000   30.000000   30.000000   30.000000
mean   56.500000  103.733333  129.100000  307.235333
std     7.560104    8.042702   13.215325   65.050207
min    30.000000   90.000000  101.000000  195.100000
25%    60.000000  100.000000  120.750000  251.350000
50%    60.000000  103.000000  128.500000  300.000000
75%    60.000000  107.500000  132.750000  343.975000
max    60.000000  130.000000  175.000000  479.000000


