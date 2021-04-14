import mysql.connector

import pandas as pd
import numpy as np

class FoodInfo:
    def __init__(self):
        self.dataset = pd.read_csv("Dataset/epi_r.csv")

    def getFoodInfoByName(self, FoodName):
        ContentInfo='\nFood Nutrients and basic Info: \n'
        counter=1
        added= False
        data = self.dataset[self.dataset["title"] == FoodName]

        for columns in data:
            if(counter<=6):
                ContentInfo += "\n"+str(columns)+":"+str(data[columns].values)+"\n"

            elif(data[columns].values>0):
               if(added==False):
                   ContentInfo += "\nFood Ingredients and advanced info are as follows : \n\n"
                   added=True
               ContentInfo += ""+str(columns)  + "\n"


            counter=counter+1

        return (ContentInfo)




    def getfoodInfoById(self,FoodId):
        #indexing in sql is with 1 so used -1
        foodTitle=self.dataset.iloc[FoodId-1]['title']
        InfoList=self.getFoodInfoByName(foodTitle)
        return (InfoList)






fd=FoodInfo()
b= fd.getFoodInfoByName("Lentil, Apple, and Turkey Wrap ")
a= fd.getfoodInfoById(77)
print(a)
print(a)

