import pandas as pd
 
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']

df = pd.DataFrame(lst)
print(df)


import pandas as pd
 
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
df = pd.DataFrame(data)
 
print(df)


import pandas as pd
 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
df = pd.DataFrame(data)
 
print(df[['Name', 'Qualification']])

import pandas as pd

 
dict = {'First Score':[100, 90, 85, 95],
        'Second Score': [30, 45, 56, 40],
        'Third Score':[55, 40, 80, 98]}

df = pd.DataFrame(dict)
 
print(df.isnull())

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 


#refer to the named index:
print(df.loc["day2"])