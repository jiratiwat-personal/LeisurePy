# import csv
#
# temps = []
# days = []
# conditions = []
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     for row in data:
#         days.append(row[0])
#         temps.append(row[1])
#         conditions.append(row[2])
# # remove first index
# del days[0]
# del temps[0]
# del conditions[0]
# print(days, temps, conditions)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# tempList = data["temp"].to_list()
# print(data.temp)
# print(tempList)
# average = sum(tempList) / len(tempList)
# print(average)
# print(data["temp"].max())

# get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
# mondayTempC = monday.temp.to_list()[0]
# mondayTempF = mondayTempC*1.8+32
# print(f"Monday temperature is {mondayTempC}C or {mondayTempF}F")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colorSeries = data["Primary Fur Color"].to_list()
numGray = len(data[data["Primary Fur Color"] == "Gray"]) # takes only the column with "Gray" value
numCinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
numBlack = len(data[data["Primary Fur Color"] == "Black"])
# for row in colorSeries:
#     if row == "Gray":
#         numGray += 1
#     if row == "Cinnamon":
#         numCinnamon += 1
#     if row == "Black":
#         numBlack += 1
print(f"Gray: {numGray}, Cinnamon: {numCinnamon}, Black: {numBlack}")
colorDict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [numGray, numCinnamon, numBlack]
}
colorTable = pandas.DataFrame(colorDict)
colorTable.to_csv("squirrel_count.csv")