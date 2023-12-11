import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))
data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
# print(data['temp'].max())

monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
# print(f'{monday_temp * 9/5 + 32} F degrees.')

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')

# Isolate fur color from data set

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirells_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirells_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirells_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirells_count)
print(red_squirells_count)
print(black_squirells_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirells_count, red_squirells_count, black_squirells_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirell_count.csv')
