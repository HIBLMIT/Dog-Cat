import pandas as pd

# s1=pd.Series([100,200,300],index=['x','y','z'])
# print(s1.index)
s1=pd.Series([1,2,3],index=[1,2,3],name='A')
s2=pd.Series([10,20,30],index=[1,2,3],name='B')
s3=pd.Series([100,200,300],index=[1,2,3],name='C')

df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)
df.to_excel("C:\Temp1\Book1.xlsx")
print("Done!")
