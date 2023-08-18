import api_client
from weather import WeatherInfo

def dsiplay_temperature_info():
    '''This function is to display temperature as per the user requirement'''
    dt_lst = weather_info.display_date_time()
    weather_info.display_lst(dt_lst)
    user_in = input("Enter date in this format 'yyyy-mm-dd'")
    wi = weather_info.temperature_info(user_in)
    weather_info.display_lst(wi)

def dsiplay_pressure_info():
    '''This function is to display pressure as per the user requirement'''
    dt_lst = weather_info.display_date_time()
    weather_info.display_lst(dt_lst)
    user_in = input("Enter date in this format 'yyyy-mm-dd'")
    wi = weather_info.pressure_info(user_in)
    weather_info.display_lst(wi)

def dsiplay_wind_speed_info():
    '''This function is to display wind_speed as per the user requirement'''
    dt_lst = weather_info.display_date_time()
    weather_info.display_lst(dt_lst)
    user_in = input("Enter date in this format 'yyyy-mm-dd'")
    wi = weather_info.wind_speed_info(user_in)
    weather_info.display_lst(wi)

if __name__ == '__main__':
    url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
    api_res = api_client.get_req(url)
    res_lst = api_res['list']
    weather_info = WeatherInfo(res_lst)
    while True:
        user_input = int(input('1. Get Temperature 2. Get Wind Speed 3. Get Pressure 0. Exit'))
        if user_input==0:
            print('Thank you')
            break
        elif user_input == 1:
            dsiplay_temperature_info()
        elif user_input == 2:
            dsiplay_wind_speed_info()
        elif user_input == 3:
            dsiplay_pressure_info()