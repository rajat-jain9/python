import pandas as pd
import matplotlib as plt
from matplotlib import style
style.use("fivethirtyeight")

pd.set_option('display.max_rows',10000)
pd.set_option('display.max_columns',100)
pd.set_option('display.max_colwidth',20)
pd.set_option('display.width',None)

class Display:
    def displayData(self,filePath):
        df = pd.read_excel(filePath)
        df2 = df.set_index("#")
        print(df2)
        df.plot()
        plt.show()
d1 = Display()
d1.displayData("./test data_Malkajgiri.xlsx")
#d1.displayData("./SampleXLSFile_904kb.xls")