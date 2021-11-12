import pandas as pd
import json
df = pd.read_csv('file/StudentsPerformance.csv')
educationlevel= df['parental level of education'].unique()
meanMath=df['math score'].mean()
meanread=df['reading score'].mean()
meanwrite=df['writing score'].mean()
data={'educationlevel':educationlevel.tolist(),'average':{'meanMath':meanMath,'meanread':meanread,
                                                          'meanwrite':meanwrite}}

with open('file/output.json','w')as output:
    json.dump(data,output,indent=4)

