import pandas as pd

bikes = pd.read_csv('london_merged.csv')
bikes.info()

row_count = bikes.shape[0]
print(row_count)

columns = bikes.shape[1]
print(columns)

print(bikes)

count = bikes['weather_code'].value_counts()
print(count)

count = bikes['season'].value_counts()
print(count)

# specifying the column names that I want to use
new_cols_dict = {'timestamp':'time',
                 'cnt':'count',
                 't1':'temp_real',
                 't2':'temp_feel',
                 'hum':'humidity_percent',
                 'wind_speed':'wind_speed_kph',
                 'weather_code':'weather',
                 'is_holiday':'is_holiday',
                 'is_weekend':'is_weekend',
                 'season':'season'
                 }

# Renaming the columns to the specified column names
bikes.rename(columns=new_cols_dict, inplace=True)

# changing the humidity values to percentage
bikes.humidity_percent = bikes.humidity_percent / 100

# creating a season dictionary so that we can connect the integers 0-3 to the actual written value
season_dict =  {'0.0':'spring',
                '1.0':'summer',
                '2.0':'autumn',
                '3.0':'winter'
                }

# creating a weather dictionary so that we can connect the integers to the actual written value
weather_dict = {'1.0':'Clear',
                '2.0':'Scattered clouds',
                '3.0':'Broken clouds',
                '4.0':'Cloudy',
                '7.0':'Rain',
                '10.0':'Rain with thunderstorm',
                '26.0':'Snowfall'
                }
# changing the seasons column data type to string
bikes.season = bikes.season.astype('str')
# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')
# mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)

# checking our df to see if the mappings are ok
print(bikes.head())

# writing the final dataframe to an excel file that we will use in our Tableau visualisation.
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')