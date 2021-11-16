###curiousfish.py
###version2.0
###written by Carolin Sommer-Trembo and Jens-Uwe Sommer
###released 16/11/2021


#import packages
import pandas
import sys
import numpy as np
import glob

#definition data range (your grid)
#this program is ment for a square test tank. Here you can define your grid (X and Y axes)
X = 34
Y = 13

#his helps if area is devided into different parts for which you would like to have separate calculations
#e.g how much of the rocky area did the fish explore compared to the sandy area?
XRock = 17
YRock = 13


#Iterate over all csv files
w = 0
#in the following line fill in name of your input file(s)
filename = glob.iglob("id*.csv")
#name your OutputFile
with open("OutputTable.csv", "w") as outfile:
    print("ID",",", "swimming_distance",",","total_sites_visited",",","percentage_total_area_visited",",","total_sites_rock",",","percentage_area_rock",",",
          "total_sites_sand",",","percentage_area_sand",",",
          "habitat_preference",",","habitat_preference_normed",",","border_sites",",","percentage_border_sites",",","percentage_border_sites_normed",file = outfile)
    for item in filename:
        w = w + 1
        print(item)
        data = pandas.read_csv(item)
        VisitedSites = np.zeros((35,14))
        VisitedSitesRock = np.zeros((18,14))
        #calculate swimming distance and percentage of visited area
        dist = 0
        lastx = data.iloc[0,0]
        lasty = data.iloc[0,1]
        #print(lastx, lasty)
        z = 0
        for k in data.iterrows():
            VisitedSites[data.iloc[z,0], data.iloc[z,1]] = 1
            if data.iloc[z,0] < 18:
                VisitedSitesRock[data.iloc[z,0], data.iloc[z,1]] = 1
            if z > 0:
                dist = dist + ((data.iloc[z,0]-lastx)**2 + (data.iloc[z,1]-lasty)**2)**(0.5)
                lastx = data.iloc[z,0]
                lasty = data.iloc[z,1]
            z = z + 1
        TotalSites = 0
        BorderSites = 0
        for x in np.nditer(VisitedSites):
            TotalSites = TotalSites + x
        for l in range(1,35):
            BorderSites = BorderSites + VisitedSites[l,1]
            BorderSites = BorderSites + VisitedSites[l,13]
        for m in range(2,13):
            BorderSites = BorderSites + VisitedSites[1,m]
            BorderSites = BorderSites + VisitedSites[34,m]
        TotalSitesRock = 0
        for x in np.nditer(VisitedSitesRock):
            TotalSitesRock = TotalSitesRock + x
        q = BorderSites/(68 + 22)
        p = (TotalSites - BorderSites)/(X * Y - 68 - 22)

        print(item[2:len(item)-4],",",dist,",",TotalSites,",",TotalSites/(X * Y),",",TotalSitesRock,",",TotalSitesRock/(XRock * YRock),",",TotalSites - TotalSitesRock,",",
        (TotalSites - TotalSitesRock)/((X - XRock)*(Y)),",",-TotalSites + 2 * TotalSitesRock,",",(-TotalSites + 2 * TotalSitesRock)/(TotalSites),",",
        BorderSites,",", BorderSites/TotalSites,",", (q - p)/(q + p),file = outfile)






