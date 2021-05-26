import pandas as pd

df=pd.read_excel('C:\Temp1\output.xlsx',index_col='ID')
# print(df.head())
df.to_excel("C:\Temp1\output2.xlsx")

# people=pd.read_excel('C:\Temp1\People.xlsx',header=None)
# people.columns=['ID','Type','Title','FirstName','MiddleName','LastName']
# people.set_index('ID',inplace=True)
# print(people.columns)
# people.to_excel("C:\Temp1\People.xlsx")
print("Done!")
# print(people.shape)
# print(people.head(3))
# print('==============================')
# print(people.tail(3))