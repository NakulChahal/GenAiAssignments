Task 1: Load Data from CSV


```python
import pandas as pd
import requests
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
data=pd.read_csv('StudentDepressionDataset.csv')
df=pd.DataFrame(data)
```

3. print


```python
df.shape
```




    (27901, 18)




```python
df.columns
```




    Index(['id', 'Gender', 'Age', 'City', 'Profession', 'Academic Pressure',
           'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction',
           'Sleep Duration', 'Dietary Habits', 'Degree',
           'Have you ever had suicidal thoughts ?', 'Work/Study Hours',
           'Financial Stress', 'Family History of Mental Illness', 'Depression'],
          dtype='str')




```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Male</td>
      <td>33.0</td>
      <td>Visakhapatnam</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>8.97</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Healthy</td>
      <td>B.Pharm</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>Female</td>
      <td>24.0</td>
      <td>Bangalore</td>
      <td>Student</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>5.90</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>BSc</td>
      <td>No</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26</td>
      <td>Male</td>
      <td>31.0</td>
      <td>Srinagar</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>7.03</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BA</td>
      <td>No</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>Female</td>
      <td>28.0</td>
      <td>Varanasi</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>5.59</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>7-8 hours</td>
      <td>Moderate</td>
      <td>BCA</td>
      <td>Yes</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>Yes</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32</td>
      <td>Female</td>
      <td>25.0</td>
      <td>Jaipur</td>
      <td>Student</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>8.13</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>M.Tech</td>
      <td>Yes</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>No</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 27901 entries, 0 to 27900
    Data columns (total 18 columns):
     #   Column                                 Non-Null Count  Dtype  
    ---  ------                                 --------------  -----  
     0   id                                     27901 non-null  int64  
     1   Gender                                 27901 non-null  str    
     2   Age                                    27901 non-null  float64
     3   City                                   27901 non-null  str    
     4   Profession                             27901 non-null  str    
     5   Academic Pressure                      27901 non-null  float64
     6   Work Pressure                          27901 non-null  float64
     7   CGPA                                   27901 non-null  float64
     8   Study Satisfaction                     27901 non-null  float64
     9   Job Satisfaction                       27901 non-null  float64
     10  Sleep Duration                         27901 non-null  str    
     11  Dietary Habits                         27901 non-null  str    
     12  Degree                                 27901 non-null  str    
     13  Have you ever had suicidal thoughts ?  27901 non-null  str    
     14  Work/Study Hours                       27901 non-null  float64
     15  Financial Stress                       27898 non-null  float64
     16  Family History of Mental Illness       27901 non-null  str    
     17  Depression                             27901 non-null  int64  
    dtypes: float64(8), int64(2), str(8)
    memory usage: 5.2 MB



```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>27896</th>
      <td>140685</td>
      <td>Female</td>
      <td>27.0</td>
      <td>Surat</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5.75</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>Class 12</td>
      <td>Yes</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27897</th>
      <td>140686</td>
      <td>Male</td>
      <td>27.0</td>
      <td>Ludhiana</td>
      <td>Student</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>9.40</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>MSc</td>
      <td>No</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27898</th>
      <td>140689</td>
      <td>Male</td>
      <td>31.0</td>
      <td>Faridabad</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>6.61</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>MD</td>
      <td>No</td>
      <td>12.0</td>
      <td>2.0</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27899</th>
      <td>140690</td>
      <td>Female</td>
      <td>18.0</td>
      <td>Ludhiana</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>6.88</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>Class 12</td>
      <td>Yes</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27900</th>
      <td>140699</td>
      <td>Male</td>
      <td>27.0</td>
      <td>Patna</td>
      <td>Student</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>9.24</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BCA</td>
      <td>Yes</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>Yes</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19850</th>
      <td>100608</td>
      <td>Female</td>
      <td>34.0</td>
      <td>Surat</td>
      <td>Student</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>7.25</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>M.Pharm</td>
      <td>No</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14202</th>
      <td>71832</td>
      <td>Male</td>
      <td>19.0</td>
      <td>Chennai</td>
      <td>Student</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>5.08</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>More than 8 hours</td>
      <td>Moderate</td>
      <td>Class 12</td>
      <td>No</td>
      <td>6.0</td>
      <td>2.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27322</th>
      <td>137784</td>
      <td>Male</td>
      <td>28.0</td>
      <td>Pune</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>8.54</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>More than 8 hours</td>
      <td>Unhealthy</td>
      <td>BE</td>
      <td>Yes</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27652</th>
      <td>139429</td>
      <td>Female</td>
      <td>20.0</td>
      <td>Lucknow</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>9.21</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>Class 12</td>
      <td>Yes</td>
      <td>11.0</td>
      <td>4.0</td>
      <td>Yes</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5208</th>
      <td>26291</td>
      <td>Female</td>
      <td>31.0</td>
      <td>Pune</td>
      <td>Student</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>6.82</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>7-8 hours</td>
      <td>Unhealthy</td>
      <td>M.Tech</td>
      <td>Yes</td>
      <td>12.0</td>
      <td>5.0</td>
      <td>No</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Age</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27898.000000</td>
      <td>27901.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>70442.149421</td>
      <td>25.822300</td>
      <td>3.141214</td>
      <td>0.000430</td>
      <td>7.656104</td>
      <td>2.943837</td>
      <td>0.000681</td>
      <td>7.156984</td>
      <td>3.139867</td>
      <td>0.585499</td>
    </tr>
    <tr>
      <th>std</th>
      <td>40641.175216</td>
      <td>4.905687</td>
      <td>1.381465</td>
      <td>0.043992</td>
      <td>1.470707</td>
      <td>1.361148</td>
      <td>0.044394</td>
      <td>3.707642</td>
      <td>1.437347</td>
      <td>0.492645</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.000000</td>
      <td>18.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>35039.000000</td>
      <td>21.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>6.290000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>70684.000000</td>
      <td>25.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>7.770000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>8.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>105818.000000</td>
      <td>30.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>8.920000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>10.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>140699.000000</td>
      <td>59.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>10.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>12.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().sum()
```




    id                                       0
    Gender                                   0
    Age                                      0
    City                                     0
    Profession                               0
    Academic Pressure                        0
    Work Pressure                            0
    CGPA                                     0
    Study Satisfaction                       0
    Job Satisfaction                         0
    Sleep Duration                           0
    Dietary Habits                           0
    Degree                                   0
    Have you ever had suicidal thoughts ?    0
    Work/Study Hours                         0
    Financial Stress                         3
    Family History of Mental Illness         0
    Depression                               0
    dtype: int64




```python
# find duplicate rows
df.duplicated().sum()
```




    np.int64(0)



Task : 2 Load Data from JSON


```python
# load data from the json
datajson=pd.read_json('recent_movies_2024_2026.json')

```


```python
# data into datafram
df=pd.DataFrame(datajson)
```


```python
# show the total rows and columns
df.shape
```




    (916, 20)




```python
# get the information about the data like column null values,data type
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 916 entries, 0 to 915
    Data columns (total 20 columns):
     #   Column              Non-Null Count  Dtype  
    ---  ------              --------------  -----  
     0   title               916 non-null    str    
     1   release_year        916 non-null    int64  
     2   release_month       916 non-null    str    
     3   release_day         916 non-null    str    
     4   genres              916 non-null    str    
     5   rating_out_of_10    916 non-null    float64
     6   vote_count          916 non-null    int64  
     7   runtime_minutes     916 non-null    int64  
     8   box_office_usd      916 non-null    int64  
     9   budget_usd          916 non-null    int64  
     10  director            916 non-null    str    
     11  screenwriter        916 non-null    str    
     12  cast                916 non-null    str    
     13  production_company  916 non-null    str    
     14  content_rating      916 non-null    str    
     15  language            916 non-null    str    
     16  country             916 non-null    str    
     17  synopsis            916 non-null    str    
     18  wikipedia_url       916 non-null    str    
     19  poster_url          916 non-null    str    
    dtypes: float64(1), int64(5), str(14)
    memory usage: 666.8 KB



```python
# show thw column name
df.columns
```




    Index(['title', 'release_year', 'release_month', 'release_day', 'genres',
           'rating_out_of_10', 'vote_count', 'runtime_minutes', 'box_office_usd',
           'budget_usd', 'director', 'screenwriter', 'cast', 'production_company',
           'content_rating', 'language', 'country', 'synopsis', 'wikipedia_url',
           'poster_url'],
          dtype='str')




```python
# get the first tom 5 rows
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>release_year</th>
      <th>release_month</th>
      <th>release_day</th>
      <th>genres</th>
      <th>rating_out_of_10</th>
      <th>vote_count</th>
      <th>runtime_minutes</th>
      <th>box_office_usd</th>
      <th>budget_usd</th>
      <th>director</th>
      <th>screenwriter</th>
      <th>cast</th>
      <th>production_company</th>
      <th>content_rating</th>
      <th>language</th>
      <th>country</th>
      <th>synopsis</th>
      <th>wikipedia_url</th>
      <th>poster_url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Mummy Murders</td>
      <td>2024</td>
      <td>January</td>
      <td>2</td>
      <td>Horror, Mystery, Thriller</td>
      <td>7.8</td>
      <td>280952</td>
      <td>138</td>
      <td>45264640</td>
      <td>12501632</td>
      <td></td>
      <td>Will Donahue</td>
      <td>Colin Bressler, Leila Annastasia Scott, Jason ...</td>
      <td>Gravitas Ventures</td>
      <td>R</td>
      <td>English</td>
      <td>United States</td>
      <td>'The Mummy Murders' (2024) is a feature film d...</td>
      <td>https://en.wikipedia.org/wiki/The_Mummy_Murders</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DarkGame</td>
      <td>2024</td>
      <td>January</td>
      <td>4</td>
      <td>Horror, Mystery, Thriller</td>
      <td>7.6</td>
      <td>109812</td>
      <td>103</td>
      <td>40487340</td>
      <td>11440392</td>
      <td>Howard J. Ford</td>
      <td>Gary Grant,Niall Johnson</td>
      <td>Ed Westwick, Andrew P. Stephen, Natalya Tsvetk...</td>
      <td>Gravitas Ventures</td>
      <td>R</td>
      <td>English</td>
      <td>United States</td>
      <td>'DarkGame' (2024) is a feature film directed b...</td>
      <td>https://en.wikipedia.org/wiki/DarkGame</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>He Went That Way</td>
      <td>2024</td>
      <td>January</td>
      <td></td>
      <td>Sci-Fi, Adventure</td>
      <td>7.4</td>
      <td>234187</td>
      <td>128</td>
      <td>29375529</td>
      <td>22583686</td>
      <td>Jeffrey Darling</td>
      <td>Evan M. Wiener</td>
      <td>Jacob Elordi,Zachary Quinto,Patrick J. Adams</td>
      <td>Vertical Entertainment/Mister Smith Entertainment</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'He Went That Way' (2024) is a feature film di...</td>
      <td>https://en.wikipedia.org/wiki/He_Went_That_Way</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Painter</td>
      <td>2024</td>
      <td>January</td>
      <td></td>
      <td>Sci-Fi, Adventure</td>
      <td>9.2</td>
      <td>165532</td>
      <td>158</td>
      <td>28225644</td>
      <td>21817096</td>
      <td>Kimani Ray Smith</td>
      <td>Brian Buccellato</td>
      <td>Charlie Weber,Jon Voight,Marie Avgeropoulos, M...</td>
      <td>Republic Pictures</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'The Painter' (2024) is a feature film directe...</td>
      <td>https://en.wikipedia.org/wiki/The_Painter_(202...</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Bricklayer</td>
      <td>2024</td>
      <td>January</td>
      <td></td>
      <td>Sci-Fi, Adventure</td>
      <td>7.1</td>
      <td>227023</td>
      <td>92</td>
      <td>29255541</td>
      <td>22503694</td>
      <td>Renny Harlin</td>
      <td>Hanna Weg, Matt Johnson</td>
      <td>Aaron Eckhart,Nina Dobrev,Tim Blake Nelson,Ilf...</td>
      <td>Vertical Entertainment/Millennium Media</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'The Bricklayer' (2024) is a feature film dire...</td>
      <td>https://en.wikipedia.org/wiki/The_Bricklayer</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get the random 5 records 
df.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>release_year</th>
      <th>release_month</th>
      <th>release_day</th>
      <th>genres</th>
      <th>rating_out_of_10</th>
      <th>vote_count</th>
      <th>runtime_minutes</th>
      <th>box_office_usd</th>
      <th>budget_usd</th>
      <th>director</th>
      <th>screenwriter</th>
      <th>cast</th>
      <th>production_company</th>
      <th>content_rating</th>
      <th>language</th>
      <th>country</th>
      <th>synopsis</th>
      <th>wikipedia_url</th>
      <th>poster_url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>906</th>
      <td>In Waves</td>
      <td>2026</td>
      <td>December</td>
      <td></td>
      <td>Sci-Fi, Adventure</td>
      <td>8.0</td>
      <td>104041</td>
      <td>149</td>
      <td>27195747</td>
      <td>21130498</td>
      <td>Phuong Mai Nguyen</td>
      <td>Fanny Burdino, Samuel Doux</td>
      <td>Will Sharpe,Stephanie Hsu</td>
      <td>Netflix/Anonymous Content</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'In Waves' (2026) is a feature film directed b...</td>
      <td>https://en.wikipedia.org/wiki/In_Waves</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>749</th>
      <td>Influenced</td>
      <td>2026</td>
      <td>May</td>
      <td></td>
      <td>Sci-Fi, Adventure</td>
      <td>7.1</td>
      <td>161353</td>
      <td>137</td>
      <td>28155651</td>
      <td>21770434</td>
      <td>Rachel Israel</td>
      <td>Jill Kargman, Carol Hartsell, Sean Crespo</td>
      <td>Jill Kargman,Laura Bell Bundy,Justin Bartha,Eu...</td>
      <td>Brainstorm Media/ Menemsha Films</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'Influenced' (2026) is a feature film directed...</td>
      <td>https://en.wikipedia.org/wiki/Influenced_(film)</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>227</th>
      <td>Subservience</td>
      <td>2024</td>
      <td>September</td>
      <td></td>
      <td>Action, Thriller</td>
      <td>7.9</td>
      <td>208914</td>
      <td>151</td>
      <td>28952238</td>
      <td>22301492</td>
      <td>S.K. Dale</td>
      <td>Will Honley, April Maguire</td>
      <td>Megan Fox,Michele Morrone,Madeline Zima</td>
      <td>XYZ Films/Millennium Media</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'Subservience' (2024) is a feature film direct...</td>
      <td>https://en.wikipedia.org/wiki/Subservience</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>733</th>
      <td>Original Sound</td>
      <td>2026</td>
      <td>April</td>
      <td></td>
      <td>Comedy</td>
      <td>6.1</td>
      <td>231600</td>
      <td>115</td>
      <td>29332200</td>
      <td>22554800</td>
      <td>Gregory Jbara</td>
      <td>Adam Seidel</td>
      <td>Eric Stoltz,Bridget Moynahan,Laura Marano,Davi...</td>
      <td>Cromono International</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'Original Sound' (2026) is a feature film dire...</td>
      <td>https://en.wikipedia.org/wiki/Original_Sound</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
    <tr>
      <th>850</th>
      <td>Don't Move</td>
      <td>2026</td>
      <td>September</td>
      <td></td>
      <td>Sci-Fi, Adventure</td>
      <td>6.5</td>
      <td>133891</td>
      <td>149</td>
      <td>27695697</td>
      <td>21463798</td>
      <td></td>
      <td>James Murray, Darren Wearmouth</td>
      <td>Maclain Nelson, Lyndsy Fonseca,Russ,Tom Cavana...</td>
      <td>Impractical Studios / Redline Entertainment</td>
      <td>PG-13</td>
      <td>English</td>
      <td>United States</td>
      <td>'Don't Move' (2026) is a feature film directed...</td>
      <td>https://en.wikipedia.org/wiki/Don%27t_Move</td>
      <td>https://images.unsplash.com/photo-148959984992...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# desribe the data as count,mean,std etc.
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>release_year</th>
      <th>rating_out_of_10</th>
      <th>vote_count</th>
      <th>runtime_minutes</th>
      <th>box_office_usd</th>
      <th>budget_usd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>916.000000</td>
      <td>916.000000</td>
      <td>916.000000</td>
      <td>916.000000</td>
      <td>9.160000e+02</td>
      <td>9.160000e+02</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2024.975983</td>
      <td>7.588755</td>
      <td>190883.281659</td>
      <td>128.033843</td>
      <td>4.112292e+07</td>
      <td>2.450549e+07</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.816143</td>
      <td>0.959322</td>
      <td>97582.137783</td>
      <td>21.704472</td>
      <td>6.774094e+07</td>
      <td>2.138200e+07</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2024.000000</td>
      <td>6.000000</td>
      <td>7128.000000</td>
      <td>90.000000</td>
      <td>2.531260e+07</td>
      <td>1.084931e+07</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2024.000000</td>
      <td>6.800000</td>
      <td>119065.500000</td>
      <td>110.750000</td>
      <td>2.784818e+07</td>
      <td>2.111606e+07</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2025.000000</td>
      <td>7.600000</td>
      <td>179263.000000</td>
      <td>129.000000</td>
      <td>2.908222e+07</td>
      <td>2.199819e+07</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2026.000000</td>
      <td>8.400000</td>
      <td>253092.000000</td>
      <td>146.000000</td>
      <td>3.139283e+07</td>
      <td>2.302142e+07</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2026.000000</td>
      <td>9.200000</td>
      <td>452490.000000</td>
      <td>164.000000</td>
      <td>5.107004e+08</td>
      <td>1.712464e+08</td>
    </tr>
  </tbody>
</table>
</div>




```python
# check the null data 
df.isnull().sum()
```




    title                 0
    release_year          0
    release_month         0
    release_day           0
    genres                0
    rating_out_of_10      0
    vote_count            0
    runtime_minutes       0
    box_office_usd        0
    budget_usd            0
    director              0
    screenwriter          0
    cast                  0
    production_company    0
    content_rating        0
    language              0
    country               0
    synopsis              0
    wikipedia_url         0
    poster_url            0
    dtype: int64




```python

# get the duplicate data
df.duplicated().sum()
```




    np.int64(0)



Task :3 Load Data from sql database


```python
# load the db
db_path = "sample.sqlite"

# make connection
connection = sqlite3.connect(db_path)

# get the data from the table
df = pd.read_sql_query("SELECT * FROM employee;", connection)

print(df)

connection.close()
```

       id          name        department   salary
    0   1   Aarav Mehta       Engineering  75000.0
    1   2   Diya Sharma   Human Resources  62000.0
    2   3   Kabir Singh             Sales  68000.0
    3   4    Isha Patel         Marketing  64000.0
    4   5   Rohan Verma           Finance  72000.0
    5   6  Ananya Gupta       Engineering  82000.0
    6   7    Vikram Rao        Operations  67000.0
    7   8    Meera Nair  Customer Support  54000.0
    8   9  Arjun Kapoor             Sales  71000.0
    9  10    Sneha Iyer         Marketing  66000.0



```python
df=pd.DataFrame(df)
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>department</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Aarav Mehta</td>
      <td>Engineering</td>
      <td>75000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Diya Sharma</td>
      <td>Human Resources</td>
      <td>62000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Kabir Singh</td>
      <td>Sales</td>
      <td>68000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Isha Patel</td>
      <td>Marketing</td>
      <td>64000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Rohan Verma</td>
      <td>Finance</td>
      <td>72000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>department</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Sneha Iyer</td>
      <td>Marketing</td>
      <td>66000.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Meera Nair</td>
      <td>Customer Support</td>
      <td>54000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Kabir Singh</td>
      <td>Sales</td>
      <td>68000.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Vikram Rao</td>
      <td>Operations</td>
      <td>67000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Isha Patel</td>
      <td>Marketing</td>
      <td>64000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 10 entries, 0 to 9
    Data columns (total 4 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   id          10 non-null     int64  
     1   name        10 non-null     str    
     2   department  10 non-null     str    
     3   salary      10 non-null     float64
    dtypes: float64(1), int64(1), str(2)
    memory usage: 658.0 bytes



```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>department</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Ananya Gupta</td>
      <td>Engineering</td>
      <td>82000.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Vikram Rao</td>
      <td>Operations</td>
      <td>67000.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Meera Nair</td>
      <td>Customer Support</td>
      <td>54000.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Arjun Kapoor</td>
      <td>Sales</td>
      <td>71000.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Sneha Iyer</td>
      <td>Marketing</td>
      <td>66000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10.00000</td>
      <td>10.0000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.50000</td>
      <td>68100.0000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.02765</td>
      <td>7622.3356</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.00000</td>
      <td>54000.0000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.25000</td>
      <td>64500.0000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.50000</td>
      <td>67500.0000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.75000</td>
      <td>71750.0000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>10.00000</td>
      <td>82000.0000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().sum()
```




    id            0
    name          0
    department    0
    salary        0
    dtype: int64




```python
df.duplicated().sum()
```




    np.int64(0)




```python
df.shape
```




    (10, 4)



Task 4: API Mini Project(TMDB API)


```python
# get the data from the api
final_res = pd.DataFrame()

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers = {
        "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZDY0MzU1ZjUyYjU5ZjliMDdkMzc0NjliZjcwNjkwOSIsIm5iZiI6MTc4MzMyNjMzNy4xOTYsInN1YiI6IjZhNGI2NjgxYTE3YWVmOGE3MmU2NjQ5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.q6lCRYo6eTyQ6DFGfY_CULHDB1c27VTUD383Dba2GkE"
}
response = requests.get(url, headers=headers)

df = pd.DataFrame(response.json()['results'])
# print(df.columns)
df = df[['id', 'title','original_language','original_title', 'overview', 'popularity', 'release_date', 'softcore', 'video', 'vote_average','vote_count']]

# Append df to final_res
final_res = pd.concat([final_res, df], ignore_index=False)
print(final_res.shape)
final_res.head()
```

    (20, 11)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>title</th>
      <th>original_language</th>
      <th>original_title</th>
      <th>overview</th>
      <th>popularity</th>
      <th>release_date</th>
      <th>softcore</th>
      <th>video</th>
      <th>vote_average</th>
      <th>vote_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>969681</td>
      <td>Spider-Man: Brand New Day</td>
      <td>en</td>
      <td>Spider-Man: Brand New Day</td>
      <td>Fighting crime full-time as Spider-Man in a wo...</td>
      <td>1346.7581</td>
      <td>2026-07-29</td>
      <td>False</td>
      <td>False</td>
      <td>7.894</td>
      <td>2158</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1368337</td>
      <td>The Odyssey</td>
      <td>en</td>
      <td>The Odyssey</td>
      <td>Odysseus, the legendary King of Ithaca, embark...</td>
      <td>620.9085</td>
      <td>2026-07-15</td>
      <td>False</td>
      <td>False</td>
      <td>7.992</td>
      <td>3192</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1288445</td>
      <td>Mutiny</td>
      <td>en</td>
      <td>Mutiny</td>
      <td>After witnessing his billionaire boss' murder ...</td>
      <td>534.5399</td>
      <td>2026-08-19</td>
      <td>False</td>
      <td>False</td>
      <td>6.538</td>
      <td>170</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1323244</td>
      <td>Rage of Stars</td>
      <td>en</td>
      <td>Rage of Stars</td>
      <td>A story about a woman from the International S...</td>
      <td>317.4746</td>
      <td>2026-08-06</td>
      <td>False</td>
      <td>False</td>
      <td>5.545</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1084244</td>
      <td>Toy Story 5</td>
      <td>en</td>
      <td>Toy Story 5</td>
      <td>When Bonnie receives a Lilypad tablet as a gif...</td>
      <td>308.0179</td>
      <td>2026-06-17</td>
      <td>False</td>
      <td>False</td>
      <td>8.224</td>
      <td>1638</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv("tmdb_movies.csv", index=False)
```


```python
df=pd.DataFrame(pd.read_csv('tmdb_movies.csv'))
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>title</th>
      <th>original_language</th>
      <th>original_title</th>
      <th>overview</th>
      <th>popularity</th>
      <th>release_date</th>
      <th>softcore</th>
      <th>video</th>
      <th>vote_average</th>
      <th>vote_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>969681</td>
      <td>Spider-Man: Brand New Day</td>
      <td>en</td>
      <td>Spider-Man: Brand New Day</td>
      <td>Fighting crime full-time as Spider-Man in a wo...</td>
      <td>1346.7581</td>
      <td>2026-07-29</td>
      <td>False</td>
      <td>False</td>
      <td>7.894</td>
      <td>2158</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1368337</td>
      <td>The Odyssey</td>
      <td>en</td>
      <td>The Odyssey</td>
      <td>Odysseus, the legendary King of Ithaca, embark...</td>
      <td>620.9085</td>
      <td>2026-07-15</td>
      <td>False</td>
      <td>False</td>
      <td>7.992</td>
      <td>3192</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1288445</td>
      <td>Mutiny</td>
      <td>en</td>
      <td>Mutiny</td>
      <td>After witnessing his billionaire boss' murder ...</td>
      <td>534.5399</td>
      <td>2026-08-19</td>
      <td>False</td>
      <td>False</td>
      <td>6.538</td>
      <td>170</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1323244</td>
      <td>Rage of Stars</td>
      <td>en</td>
      <td>Rage of Stars</td>
      <td>A story about a woman from the International S...</td>
      <td>317.4746</td>
      <td>2026-08-06</td>
      <td>False</td>
      <td>False</td>
      <td>5.545</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1084244</td>
      <td>Toy Story 5</td>
      <td>en</td>
      <td>Toy Story 5</td>
      <td>When Bonnie receives a Lilypad tablet as a gif...</td>
      <td>308.0179</td>
      <td>2026-06-17</td>
      <td>False</td>
      <td>False</td>
      <td>8.224</td>
      <td>1638</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (20, 11)




```python
# pd.read_json('https://storage.googleapis.com/kagglesdsdata/datasets/11560031/18730015/recent_movies_2024_2026.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260821%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260821T061242Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=93171d491802c2392fa961c460afd25c78cdd105d552d6449ec3bae2c9961feaa8f08819887bfdbdfb892004da8c127d4af67c32a170d0b5ec9e455a470e82eb449cb969908d26fb015e9639c4fea47a8d29f6f8df1c22587be20f5edf460903a06595759f2e37f6e5fec998b713d86a15255229c771bd329b706e7efe5a8b54af62e99dc5248273eb7f1484b1a9687b93ca899ff0b39665eda1ee265f587eadce9325de933f364dc3383be71225d609825ba56c7aa3f00a8dcb467b1b5f364ce292648540509160854802e7a7aec7975904387de4f24c76fed8dcbee2b19bae41ad70e68ba72b95aface6ed9fdbe95107dad54e1e81a332af58520a05c3b29b')
```

Part 2-Data preprocessing & cleaning 

## Task 5: Understanding the Data

# 1. check dataset shape 


```python
data=pd.read_csv('StudentDepressionDataset.csv')
df=pd.DataFrame(data)
```


```python
df.shape
```




    (27901, 18)



# display column type


```python
print(df.dtypes)
```

    id                                         int64
    Gender                                       str
    Age                                      float64
    City                                         str
    Profession                                   str
    Academic Pressure                        float64
    Work Pressure                            float64
    CGPA                                     float64
    Study Satisfaction                       float64
    Job Satisfaction                         float64
    Sleep Duration                               str
    Dietary Habits                               str
    Degree                                       str
    Have you ever had suicidal thoughts ?        str
    Work/Study Hours                         float64
    Financial Stress                         float64
    Family History of Mental Illness             str
    Depression                                 int64
    dtype: object


identify numerical and categorical columns


```python
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 27901 entries, 0 to 27900
    Data columns (total 18 columns):
     #   Column                                 Non-Null Count  Dtype  
    ---  ------                                 --------------  -----  
     0   id                                     27901 non-null  int64  
     1   Gender                                 27901 non-null  str    
     2   Age                                    27901 non-null  float64
     3   City                                   27901 non-null  str    
     4   Profession                             27901 non-null  str    
     5   Academic Pressure                      27901 non-null  float64
     6   Work Pressure                          27901 non-null  float64
     7   CGPA                                   27901 non-null  float64
     8   Study Satisfaction                     27901 non-null  float64
     9   Job Satisfaction                       27901 non-null  float64
     10  Sleep Duration                         27901 non-null  str    
     11  Dietary Habits                         27901 non-null  str    
     12  Degree                                 27901 non-null  str    
     13  Have you ever had suicidal thoughts ?  27901 non-null  str    
     14  Work/Study Hours                       27901 non-null  float64
     15  Financial Stress                       27898 non-null  float64
     16  Family History of Mental Illness       27901 non-null  str    
     17  Depression                             27901 non-null  int64  
    dtypes: float64(8), int64(2), str(8)
    memory usage: 5.2 MB


check missing values


```python
df.isnull().sum()
```




    id                                       0
    Gender                                   0
    Age                                      0
    City                                     0
    Profession                               0
    Academic Pressure                        0
    Work Pressure                            0
    CGPA                                     0
    Study Satisfaction                       0
    Job Satisfaction                         0
    Sleep Duration                           0
    Dietary Habits                           0
    Degree                                   0
    Have you ever had suicidal thoughts ?    0
    Work/Study Hours                         0
    Financial Stress                         3
    Family History of Mental Illness         0
    Depression                               0
    dtype: int64



## Rest of the known 


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Male</td>
      <td>33.0</td>
      <td>Visakhapatnam</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>8.97</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Healthy</td>
      <td>B.Pharm</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>Female</td>
      <td>24.0</td>
      <td>Bangalore</td>
      <td>Student</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>5.90</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>BSc</td>
      <td>No</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26</td>
      <td>Male</td>
      <td>31.0</td>
      <td>Srinagar</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>7.03</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BA</td>
      <td>No</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>Female</td>
      <td>28.0</td>
      <td>Varanasi</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>5.59</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>7-8 hours</td>
      <td>Moderate</td>
      <td>BCA</td>
      <td>Yes</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>Yes</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32</td>
      <td>Female</td>
      <td>25.0</td>
      <td>Jaipur</td>
      <td>Student</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>8.13</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>M.Tech</td>
      <td>Yes</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>No</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>27896</th>
      <td>140685</td>
      <td>Female</td>
      <td>27.0</td>
      <td>Surat</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5.75</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>Class 12</td>
      <td>Yes</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27897</th>
      <td>140686</td>
      <td>Male</td>
      <td>27.0</td>
      <td>Ludhiana</td>
      <td>Student</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>9.40</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>MSc</td>
      <td>No</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27898</th>
      <td>140689</td>
      <td>Male</td>
      <td>31.0</td>
      <td>Faridabad</td>
      <td>Student</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>6.61</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>MD</td>
      <td>No</td>
      <td>12.0</td>
      <td>2.0</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27899</th>
      <td>140690</td>
      <td>Female</td>
      <td>18.0</td>
      <td>Ludhiana</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>6.88</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>Class 12</td>
      <td>Yes</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27900</th>
      <td>140699</td>
      <td>Male</td>
      <td>27.0</td>
      <td>Patna</td>
      <td>Student</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>9.24</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BCA</td>
      <td>Yes</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>Yes</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23326</th>
      <td>117583</td>
      <td>Female</td>
      <td>33.0</td>
      <td>Surat</td>
      <td>Student</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>9.89</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>7-8 hours</td>
      <td>Unhealthy</td>
      <td>PhD</td>
      <td>Yes</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10067</th>
      <td>50860</td>
      <td>Female</td>
      <td>24.0</td>
      <td>Srinagar</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>8.37</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Moderate</td>
      <td>M.Tech</td>
      <td>Yes</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12711</th>
      <td>64283</td>
      <td>Male</td>
      <td>33.0</td>
      <td>Ludhiana</td>
      <td>Student</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>6.75</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Unhealthy</td>
      <td>BA</td>
      <td>No</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>Yes</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23796</th>
      <td>119877</td>
      <td>Male</td>
      <td>29.0</td>
      <td>Kalyan</td>
      <td>Student</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>9.97</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>Less than 5 hours</td>
      <td>Moderate</td>
      <td>PhD</td>
      <td>No</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
    <tr>
      <th>763</th>
      <td>3940</td>
      <td>Male</td>
      <td>26.0</td>
      <td>Ghaziabad</td>
      <td>Student</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>7.70</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>LLM</td>
      <td>Yes</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Age</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27901.000000</td>
      <td>27898.000000</td>
      <td>27901.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>70442.149421</td>
      <td>25.822300</td>
      <td>3.141214</td>
      <td>0.000430</td>
      <td>7.656104</td>
      <td>2.943837</td>
      <td>0.000681</td>
      <td>7.156984</td>
      <td>3.139867</td>
      <td>0.585499</td>
    </tr>
    <tr>
      <th>std</th>
      <td>40641.175216</td>
      <td>4.905687</td>
      <td>1.381465</td>
      <td>0.043992</td>
      <td>1.470707</td>
      <td>1.361148</td>
      <td>0.044394</td>
      <td>3.707642</td>
      <td>1.437347</td>
      <td>0.492645</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.000000</td>
      <td>18.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>35039.000000</td>
      <td>21.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>6.290000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>70684.000000</td>
      <td>25.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>7.770000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>8.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>105818.000000</td>
      <td>30.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>8.920000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>10.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>140699.000000</td>
      <td>59.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>10.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>12.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 27901 entries, 0 to 27900
    Data columns (total 18 columns):
     #   Column                                 Non-Null Count  Dtype  
    ---  ------                                 --------------  -----  
     0   id                                     27901 non-null  int64  
     1   Gender                                 27901 non-null  str    
     2   Age                                    27901 non-null  float64
     3   City                                   27901 non-null  str    
     4   Profession                             27901 non-null  str    
     5   Academic Pressure                      27901 non-null  float64
     6   Work Pressure                          27901 non-null  float64
     7   CGPA                                   27901 non-null  float64
     8   Study Satisfaction                     27901 non-null  float64
     9   Job Satisfaction                       27901 non-null  float64
     10  Sleep Duration                         27901 non-null  str    
     11  Dietary Habits                         27901 non-null  str    
     12  Degree                                 27901 non-null  str    
     13  Have you ever had suicidal thoughts ?  27901 non-null  str    
     14  Work/Study Hours                       27901 non-null  float64
     15  Financial Stress                       27898 non-null  float64
     16  Family History of Mental Illness       27901 non-null  str    
     17  Depression                             27901 non-null  int64  
    dtypes: float64(8), int64(2), str(8)
    memory usage: 5.2 MB


## Task 6 Data Cleaning

## Handle missing values


```python
df.isnull().sum()
```




    id                                       0
    Gender                                   0
    Age                                      0
    City                                     0
    Profession                               0
    Academic Pressure                        0
    Work Pressure                            0
    CGPA                                     0
    Study Satisfaction                       0
    Job Satisfaction                         0
    Sleep Duration                           0
    Dietary Habits                           0
    Degree                                   0
    Have you ever had suicidal thoughts ?    0
    Work/Study Hours                         0
    Financial Stress                         3
    Family History of Mental Illness         0
    Depression                               0
    dtype: int64




```python
df['Financial Stress'].isnull().value_counts()
```




    Financial Stress
    False    27898
    True         3
    Name: count, dtype: int64




```python
df['Financial Stress'].mean()
```




    np.float64(3.1398666571080365)




```python
df['Financial Stress']=df['Financial Stress'].fillna(3.14,inplace=True)
```

    /var/folders/q2/jg_sv82d5z79tj_05d1fbrzr0000gn/T/ipykernel_12394/3918632623.py:1: ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    Such inplace method never works to update the original DataFrame or Series, because the intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' instead, to perform the operation inplace on the original object, or try to avoid an inplace operation using 'df[col] = df[col].method(value)'.
    
    See the documentation for a more detailed explanation: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html
      df['Financial Stress']=df['Financial Stress'].fillna(3.14,inplace=True)



```python
df['Financial Stress'].isnull().value_counts()
```




    Financial Stress
    False    27901
    Name: count, dtype: int64




```python
df['Dietary Habits'].value_counts()
```




    Dietary Habits
    Unhealthy    10317
    Moderate      9921
    Healthy       7651
    Others          12
    Name: count, dtype: int64




```python
# Find the most frequent category
mode_value = df['Dietary Habits'].mode()[0]
mode_value
# Replace 'Others' with the mode
df['Dietary Habits'] = df['Dietary Habits'].replace('Others', mode_value)
```


```python
df['Sleep Duration'].value_counts()
```




    Sleep Duration
    Less than 5 hours    8310
    7-8 hours            7346
    5-6 hours            6183
    More than 8 hours    6044
    Others                 18
    Name: count, dtype: int64




```python
# Find the most frequent Sleep Duration
mode_value = df['Sleep Duration'].mode()[0]
mode_value
# Replace 'Others' with the mode
df['Sleep Duration'] = df['Sleep Duration'].replace('Others', mode_value)
```


```python
df.isnull().sum()
```




    id                                       0
    Gender                                   0
    Age                                      0
    City                                     0
    Profession                               0
    Academic Pressure                        0
    Work Pressure                            0
    CGPA                                     0
    Study Satisfaction                       0
    Job Satisfaction                         0
    Sleep Duration                           0
    Dietary Habits                           0
    Degree                                   0
    Have you ever had suicidal thoughts ?    0
    Work/Study Hours                         0
    Financial Stress                         0
    Family History of Mental Illness         0
    Depression                               0
    dtype: int64



## remove duplicate if any


```python
df.duplicated().sum()
```




    np.int64(0)




```python
df.rename(columns={'Financial Stress': 'financial_stress'}, inplace=True)
```


```python
df.columns
```




    Index(['id', 'Gender', 'Age', 'City', 'Profession', 'Academic Pressure',
           'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction',
           'Sleep Duration', 'Dietary Habits', 'Degree',
           'Have you ever had suicidal thoughts ?', 'Work/Study Hours',
           'financial_stress', 'Family History of Mental Illness', 'Depression'],
          dtype='str')




```python
df['Depression'] = df['Depression'].astype('int32')
df['id'] = df['id'].astype('int32')

```


```python
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 27901 entries, 0 to 27900
    Data columns (total 18 columns):
     #   Column                                 Non-Null Count  Dtype  
    ---  ------                                 --------------  -----  
     0   id                                     27901 non-null  int32  
     1   Gender                                 27901 non-null  str    
     2   Age                                    27901 non-null  float64
     3   City                                   27901 non-null  str    
     4   Profession                             27901 non-null  str    
     5   Academic Pressure                      27901 non-null  float64
     6   Work Pressure                          27901 non-null  float64
     7   CGPA                                   27901 non-null  float64
     8   Study Satisfaction                     27901 non-null  float64
     9   Job Satisfaction                       27901 non-null  float64
     10  Sleep Duration                         27901 non-null  str    
     11  Dietary Habits                         27901 non-null  str    
     12  Degree                                 27901 non-null  str    
     13  Have you ever had suicidal thoughts ?  27901 non-null  str    
     14  Work/Study Hours                       27901 non-null  float64
     15  financial_stress                       27901 non-null  float64
     16  Family History of Mental Illness       27901 non-null  str    
     17  Depression                             27901 non-null  int32  
    dtypes: float64(8), int32(2), str(8)
    memory usage: 5.0 MB



```python
df['Profession'].value_counts()
df=df[df['Profession']=='Student']
```


```python
df.info()
```

    <class 'pandas.DataFrame'>
    Index: 27870 entries, 0 to 27900
    Data columns (total 18 columns):
     #   Column                                 Non-Null Count  Dtype  
    ---  ------                                 --------------  -----  
     0   id                                     27870 non-null  int32  
     1   Gender                                 27870 non-null  str    
     2   Age                                    27870 non-null  float64
     3   City                                   27870 non-null  str    
     4   Profession                             27870 non-null  str    
     5   Academic Pressure                      27870 non-null  float64
     6   Work Pressure                          27870 non-null  float64
     7   CGPA                                   27870 non-null  float64
     8   Study Satisfaction                     27870 non-null  float64
     9   Job Satisfaction                       27870 non-null  float64
     10  Sleep Duration                         27870 non-null  str    
     11  Dietary Habits                         27870 non-null  str    
     12  Degree                                 27870 non-null  str    
     13  Have you ever had suicidal thoughts ?  27870 non-null  str    
     14  Work/Study Hours                       27870 non-null  float64
     15  financial_stress                       27870 non-null  float64
     16  Family History of Mental Illness       27870 non-null  str    
     17  Depression                             27870 non-null  int32  
    dtypes: float64(8), int32(2), str(8)
    memory usage: 5.2 MB



```python
# collect the usable data
df=df[['Gender', 'Age', 'City', 'Academic Pressure',
       'Work Pressure', 'CGPA', 'Study Satisfaction', 
       'Sleep Duration', 'Dietary Habits', 'Degree', 'Work/Study Hours',
       'financial_stress', 'Family History of Mental Illness', 'Depression']]
```


```python
df.info()
```

    <class 'pandas.DataFrame'>
    Index: 27870 entries, 0 to 27900
    Data columns (total 14 columns):
     #   Column                            Non-Null Count  Dtype  
    ---  ------                            --------------  -----  
     0   Gender                            27870 non-null  str    
     1   Age                               27870 non-null  float64
     2   City                              27870 non-null  str    
     3   Academic Pressure                 27870 non-null  float64
     4   Work Pressure                     27870 non-null  float64
     5   CGPA                              27870 non-null  float64
     6   Study Satisfaction                27870 non-null  float64
     7   Sleep Duration                    27870 non-null  str    
     8   Dietary Habits                    27870 non-null  str    
     9   Degree                            27870 non-null  str    
     10  Work/Study Hours                  27870 non-null  float64
     11  financial_stress                  27870 non-null  float64
     12  Family History of Mental Illness  27870 non-null  str    
     13  Depression                        27870 non-null  int32  
    dtypes: float64(7), int32(1), str(6)
    memory usage: 4.2 MB


## Task 7 :Feature Preparation

## Lable encoding


```python
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
df['Family History of Mental Illness']=l.fit_transform(df['Family History of Mental Illness'])
```


```python
df['Family History of Mental Illness']
```




    0        0
    1        1
    2        1
    3        1
    4        0
            ..
    27896    1
    27897    1
    27898    0
    27899    0
    27900    1
    Name: Family History of Mental Illness, Length: 27870, dtype: int64




```python
nominal_data=df[['Gender','City','Sleep Duration','Dietary Habits','Degree']]
```


```python
nominal_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>City</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>Visakhapatnam</td>
      <td>5-6 hours</td>
      <td>Healthy</td>
      <td>B.Pharm</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>Bangalore</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>BSc</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Male</td>
      <td>Srinagar</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Female</td>
      <td>Varanasi</td>
      <td>7-8 hours</td>
      <td>Moderate</td>
      <td>BCA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Female</td>
      <td>Jaipur</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>M.Tech</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>27896</th>
      <td>Female</td>
      <td>Surat</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>Class 12</td>
    </tr>
    <tr>
      <th>27897</th>
      <td>Male</td>
      <td>Ludhiana</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>MSc</td>
    </tr>
    <tr>
      <th>27898</th>
      <td>Male</td>
      <td>Faridabad</td>
      <td>5-6 hours</td>
      <td>Unhealthy</td>
      <td>MD</td>
    </tr>
    <tr>
      <th>27899</th>
      <td>Female</td>
      <td>Ludhiana</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>Class 12</td>
    </tr>
    <tr>
      <th>27900</th>
      <td>Male</td>
      <td>Patna</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BCA</td>
    </tr>
  </tbody>
</table>
<p>27870 rows × 5 columns</p>
</div>




```python
nominal_data.value_counts()
```




    Gender  City       Sleep Duration     Dietary Habits  Degree  
    Male    Ahmedabad  Less than 5 hours  Unhealthy       Class 12    29
            Ludhiana   5-6 hours          Healthy         Class 12    25
    Female  Ludhiana   5-6 hours          Healthy         Class 12    24
    Male    Meerut     Less than 5 hours  Unhealthy       B.Tech      24
            Ahmedabad  More than 8 hours  Moderate        Class 12    24
                                                                      ..
    Female  Jaipur     More than 8 hours  Unhealthy       BBA          1
    Male    Ahmedabad  Less than 5 hours  Healthy         MCA          1
            Srinagar   More than 8 hours  Healthy         MBBS         1
            Ludhiana   Less than 5 hours  Healthy         MSc          1
            Faridabad  5-6 hours          Unhealthy       MD           1
    Name: count, Length: 11781, dtype: int64




```python
from sklearn.preprocessing import OneHotEncoder
o=OneHotEncoder()
nominal_data=o.fit_transform(nominal_data)
```


```python
nominal_data
```




    <Compressed Sparse Row sparse matrix of dtype 'float64'
    	with 139350 stored elements and shape (27870, 89)>



## Separate feature and taget column 


```python
# Features (X)
X = df[['Gender', 'Age', 'City', 'Academic Pressure',
        'Work Pressure', 'CGPA', 'Study Satisfaction',
        'Sleep Duration', 'Dietary Habits', 'Degree', 'Work/Study Hours',
        'financial_stress', 'Family History of Mental Illness']]

# Target (y)
y = df['Depression']
```

## PART 3- Exploratory Data Analysis

## Task 8 : Univariate Anasysis

## 1. plot distribution of numerical columns (histogram + KDE)


```python
sns.histplot(df['Age'], kde=True, bins=20)

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')

plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_95_0.png)
    



```python
sns.histplot(data=df, x='Work Pressure',kde=True, bins=20)

plt.title('Work Pressure Distribution')
plt.xlabel('Work Pressure')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_96_0.png)
    



```python
sns.histplot(data=df, x='Academic Pressure',kde=True, bins=20)

plt.title('Academic Pressure Distribution')
plt.xlabel('Academic Pressure')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_97_0.png)
    



```python
sns.histplot(data=df, x='CGPA',kde=True, bins=20)

plt.title('CGPA Distribution')
plt.xlabel('CGPA')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_98_0.png)
    



```python
sns.histplot(data=df, x='Study Satisfaction',kde=True, bins=20)

plt.title('Study Satisfaction Distribution')
plt.xlabel('Study Satisfaction')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_99_0.png)
    



```python
sns.histplot(data=df, x='Work/Study Hours',kde=True, bins=20)

plt.title('Work/Study Hours Distribution')
plt.xlabel('Work/Study Hours')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_100_0.png)
    



```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Work/Study Hours</th>
      <th>financial_stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>33.0</td>
      <td>Visakhapatnam</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>8.97</td>
      <td>2.0</td>
      <td>5-6 hours</td>
      <td>Healthy</td>
      <td>B.Pharm</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>24.0</td>
      <td>Bangalore</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>5.90</td>
      <td>5.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>BSc</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Male</td>
      <td>31.0</td>
      <td>Srinagar</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>7.03</td>
      <td>5.0</td>
      <td>Less than 5 hours</td>
      <td>Healthy</td>
      <td>BA</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Female</td>
      <td>28.0</td>
      <td>Varanasi</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>5.59</td>
      <td>2.0</td>
      <td>7-8 hours</td>
      <td>Moderate</td>
      <td>BCA</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Female</td>
      <td>25.0</td>
      <td>Jaipur</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>8.13</td>
      <td>3.0</td>
      <td>5-6 hours</td>
      <td>Moderate</td>
      <td>M.Tech</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.histplot(data=df, x='financial_stress',kde=True)

plt.title('financial stress Distribution')
plt.xlabel('financial stress')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_102_0.png)
    



```python
sns.histplot(data=df, x='Family History of Mental Illness',kde=True,bins=2)

plt.title('Family History of Mental Illness Distribution')
plt.xlabel('Family History of Mental Illness')
plt.ylabel('Count')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_103_0.png)
    


## 2 count plot for categorical columns.


```python
## this method referance  getting from google
cat_cols = df.select_dtypes(include=['object', 'category']).columns

for col in cat_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col)
    plt.title(f'{col} Distribution')
    plt.xticks(rotation=45)
    plt.show()
```

    /var/folders/q2/jg_sv82d5z79tj_05d1fbrzr0000gn/T/ipykernel_12394/3512987570.py:2: Pandas4Warning: For backward compatibility, 'str' dtypes are included by select_dtypes when 'object' dtype is specified. This behavior is deprecated and will be removed in a future version. Explicitly pass 'str' to `include` to select them, or to `exclude` to remove them and silence this warning.
    See https://pandas.pydata.org/docs/user_guide/migration-3-strings.html#string-migration-select-dtypes for details on how to write code that works with pandas 2 and 3.
      cat_cols = df.select_dtypes(include=['object', 'category']).columns



    
![png](assignment13-ML_files/assignment13-ML_105_1.png)
    



    
![png](assignment13-ML_files/assignment13-ML_105_2.png)
    



    
![png](assignment13-ML_files/assignment13-ML_105_3.png)
    



    
![png](assignment13-ML_files/assignment13-ML_105_4.png)
    



    
![png](assignment13-ML_files/assignment13-ML_105_5.png)
    


## 3. identify outliers using boxplot


```python
sns.boxplot(x=df['Age'])

plt.title('Boxplot of Age')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_107_0.png)
    



```python
sns.boxplot(x=df['CGPA'])

plt.title('Boxplot of CGPA')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_108_0.png)
    



```python
cat_cols = df.select_dtypes(include=['number', 'category']).columns

for col in cat_cols:
    plt.figure(figsize=(8, 3))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_109_0.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_1.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_2.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_3.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_4.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_5.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_6.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_7.png)
    



    
![png](assignment13-ML_files/assignment13-ML_109_8.png)
    


## Task 9 :Bivariate Analysis


```python
# 1.Numerical vs Numerical
sns.scatterplot(data=df, x='Age', y='CGPA')

plt.title('Age vs CGPA')
plt.xlabel('Age')
plt.ylabel('CGPA')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_111_0.png)
    



```python
sns.scatterplot(data=df, x='Work/Study Hours', y='financial_stress')

plt.title('Work/Study Hours vs Financial Stress')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_112_0.png)
    



```python
sns.scatterplot(data=df, x='Academic Pressure', y='Sleep Duration')

plt.title('Academic Pressure vs Sleep Duration')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_113_0.png)
    



```python
sns.scatterplot(data=df, x='Gender', y='Study Satisfaction')

plt.title('Gender vs Study Satisfaction')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_114_0.png)
    


# correlation heatmap


```python
# heatmap for the Age , CPA and Financial stress
corr = df[['Age', 'CGPA', 'financial_stress']].corr()

plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

plt.title('Correlation Heatmap')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_116_0.png)
    



```python
# syntax suggested  from the google
num_df = df.select_dtypes(include='number')

# Correlation matrix
corr = num_df.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

plt.title('Correlation Heatmap')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_117_0.png)
    


## Categorical vs Numerical

## Bar plot


```python
sns.barplot(data=df, x='Gender', y='Age')

plt.title('Gender vs Age')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_120_0.png)
    



```python
sns.barplot(data=df, x='Dietary Habits', y='CGPA')

plt.title('Dietary Habits vs CGPA')
plt.xticks(rotation=45)
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_121_0.png)
    



```python
sns.barplot(data=df, x='Sleep Duration', y='financial_stress')

plt.title('Sleep Duration vs Financial Stress')
plt.xticks(rotation=45)
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_122_0.png)
    


# Boxp lot


```python
sns.boxplot(data=df, x='Gender', y='Age')

plt.title('Gender vs Age')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_124_0.png)
    



```python
sns.boxplot(data=df, x='Dietary Habits', y='CGPA')

plt.title('Dietary Habits vs CGPA')
plt.xticks(rotation=45)
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_125_0.png)
    



```python
sns.boxplot(data=df, x='Age', y='Depression')

plt.title('Age vs Depression')
plt.xticks(rotation=45)
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_126_0.png)
    



```python
sns.boxplot(data=df, x='Sleep Duration', y='financial_stress')

plt.title('Sleep Duration vs Financial Stress')
plt.xticks(rotation=45)
plt.show()
```


    
![png](assignment13-ML_files/assignment13-ML_127_0.png)
    


## Task 10. Insights and Observations

1. **Age Distribution:** The age variable shows that most observations are concentrated within a particular age range, while a few observations may represent unusually young or old individuals.

2. **Gender Pattern:** The distribution of males and females is not completely equal, indicating that one gender is more represented in the dataset.

3. **Correlation:** Numerical variables show different levels of correlation. Some variables have a stronger relationship with each other, while others have weak or almost no relationship.

4. **Outliers:** Some numerical columns contain extreme values that differ significantly from the majority of observations. These outliers should be investigated before applying machine learning models.

5. **Missing Values:** Some columns contain missing/null values. These values need to be handled appropriately using methods such as mean/median/mode imputation or removal.

6. **Categorical Data Quality:** Some categorical values may have inconsistent representations, such as `"Other"` or different spellings/capitalization. These should be standardized before analysis.

7. **Relationship Between Variables:** The relationship between categorical and numerical variables can be observed using plots such as bar plots and box plots, which help identify differences in numerical values across categories.

8. **Data Cleaning:** Overall, the dataset requires preprocessing such as handling missing values, standardizing categorical values, checking outliers, and converting columns to appropriate data types before further analysis or machine learning.

