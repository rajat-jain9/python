import pandas as pd

df = pd.read_excel(r"./test data_Malkajgiri.xlsx")
#print(df)
df2 = df.set_index("#")
print(df2)

        ### 1) INDEXING######

print(df2.loc[1:5,"From":"To"])
print(df2.loc[: ,"To"])
print(df2.head(2))     OR   print(df2.loc[1:2,"ID":"Booking History"]) (For first two rows)
print(df2.tail(2)) (For Last two rows)
print(df2.loc[1, :])
print(df2.loc[1,"To"])
print(df2.loc[: ,"Start Time Hour"].mean())
print(df2.iloc[0:2,0:1])
print(df2.ix[0:2,"From":"To"])
df2["Start Time"] = df2["Start Time Hour"].map(str) + df2["Start Time Minutes"].map(str)
df2['Start Time'] = df[['Start Time Hour','Start Time Minutes']].apply(lambda x: ''.join(x), axis=1)
df['ColumnA'] = df[df.columns[3:5]].apply(lambda x: ','.join(x.dropna().astype(int).astype(str)),axis=1)
sd = df.reindex(column=['column name',[column name],..]) #To show only specific columns
        ### 2) MErging Two DaaFrames Having all common columns

#Let df1 and df2 are two DataFrames
merge = pd.merge(df1,df2) (This will print all common columns)
merge = pd.merge(df1,df2,on = "Any Common Column NAme") (Will print only specific common column)


        ### 3) JOIN Two DataFrames
joined = df1.join(df2)


        ### 4) TO change INdex
df2 = df.set_index("column name")



        ### 5) Rename Column Header
df = df.remname(column={"Start Time Hour","Start Time"})


        ### 6) Draw Graph using matplotlib
import matplotlib as plt
from matplotlib import style
style.use("fivethirtyeight")
df.plot()
plt.show()


        ### 7) Concatenation in DataFrames

concat = pd.concat([df1,df2])

        ### 8) Converting a csv file into html file(Data Munging)
csv = pd.read_csv('File Path',index_col=0)
csv.to_html('new.html') #(file will be downloaded in your current working directory)



        ### 9) Statistics using python(Mean,Median,Mode,Variance)
from statistics import mean
from statistocs import median
from statistics import mode
from statistics import variance
print(mean([1,2,2,3,4,4,5]))
print(median([1,2,2,3,4,4,5]))
print(mode([1,2,2,3,4,4,5]))
print(variance([1,2,2,3,4,4,5]))