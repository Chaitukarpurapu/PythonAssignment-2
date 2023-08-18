'''This module contains the business logic of weather API'''

#sample dictionary to construct the logic
dct = {'city': {'coord': {'lat': 48.1371, 'lon': 11.5754},
          'country': 'DE',
          'id': 2867714,
          'name': 'Munich',
          'population': 1260391},
 'cnt': 96,
 'cod': '200',
 'list': [{'clouds': {'all': 77},
           'dt': 1553709600,
           'dt_txt': '2019-03-27 18:00:00',
           'main': {'grnd_level': 971.745,
                    'humidity': 100,
                    'pressure': 1031.934,
                    'sea_level': 1031.934,
                    'temp': 278.76,
                    'temp_kf': -0.8,
                    'temp_max': 279.558,
                    'temp_min': 278.76},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'broken clouds',
                        'icon': '04n',
                        'id': 803,
                        'main': 'Clouds'}],
           'wind': {'deg': 40.932, 'speed': 1.6}},
          {'clouds': {'all': 24},
           'dt': 1553713200,
           'dt_txt': '2019-03-27 19:00:00',
           'main': {'grnd_level': 972.411,
                    'humidity': 100,
                    'pressure': 1033.061,
                    'sea_level': 1033.061,
                    'temp': 278.4,
                    'temp_kf': -0.6,
                    'temp_max': 279,
                    'temp_min': 278.4},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'few clouds',
                        'icon': '02n',
                        'id': 801,
                        'main': 'Clouds'}],
           'wind': {'deg': 46.416, 'speed': 1.49}}]}

# res = dct['list']
# dt = '2019-03-27 18:00:00'
# dct1={}
# for i in res:
#     dct1[i.pop('dt_txt')] = i
# # print(res)
# # def get_temperature(res,dt):
# for key,value in dct1.items():
#     print(key)
#     print(value)

class WeatherInfo:
    '''
    This WhetherInfo class has methods which gives information about temperature, pressure and
    wind speed
    '''
    def __init__(self,res_dct):
        self.res_dct = res_dct

    def temperature_info(self,date):
        '''
        This method gives info about the temperature of specific date
        :param date: This is the date attribute should be given by user.
        :return: List of temperatures at mentioned date
        '''
        lst = []
        for i in self.res_dct:
            res_date = i['dt_txt'].split()[0]
            if date == res_date:
                lst.append(f"Date -{i['dt_txt']} Temperature - {i['main']['temp']}")
        if lst:
            return lst
        else:
            return f'The date {date} you entered is not matching in the entries, Please check the prompt'

    def wind_speed_info(self,date):
        '''
        This method gives info about the wind speed of specific date
        :param date: This is the date attribute should be given by user
        :return: List of wind speeds at mentioned date
        '''
        lst = []
        for i in self.res_dct:
            res_date = i['dt_txt'].split()[0]
            if date == res_date:
                lst.append(f"Date -{i['dt_txt']} Wind Speed - {i['wind']['speed']}")
        if lst:
            return lst
        else:
            return f'The date {date} you entered is not matching in the entries, Please check the prompt'

    def pressure_info(self,date):
        '''
        This method gives info about the pressure of specific date
        :param date: This is the date attribute should be given by user
        :return: List of pressures at mentioned date
        '''
        lst = []
        for i in self.res_dct:
            res_date = i['dt_txt'].split()[0]
            if date == res_date:
                lst.append(f"Date -{i['dt_txt']} Pressure - {i['main']['pressure']}")
        if lst:
            return lst
        else:
            return f'The date {date} you entered is not matching in the entries, Please check the prompt'

    def display_date_time(self):
        '''
        This method is used to display the dates present in the response
        :return: List of dates in the response
        '''
        lst = []
        try:
            for i in self.res_dct:
                lst.append(i['dt_txt'])
        except:
            return f'Please check the res_dct is dictionary and have dt_txt key in it'
        return lst
    def display_lst(self,lst):
        '''
        This method print items in the list
        :param lst:
        :return: None
        '''
        if type(lst) == type([]):
            for i in lst:
                print(i)
        else:
            print(lst)

if __name__ == '__main__':
    wobj = WeatherInfo(dct['list'])

    print(wobj.temperature_info('2019-03-27'))
    print(wobj.pressure_info('2019-03-27'))
    print(wobj.wind_speed_info('2019-03-27'))
