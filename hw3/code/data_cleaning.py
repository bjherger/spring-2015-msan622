#!/usr/bin/env python
"""
coding=utf-8
"""
# imports
# *********************************
import pandas as pd
# global variables
# *********************************


__author__ = 'bjherger'
__version__ = '1.0'
__email__ = '13herger@gmail.com'
__status__ = 'Development'
__maintainer__ = 'bjherger'


# functions
# *********************************

def main():
    df = pd.read_csv('../data/seatbelts.csv')
    # df['time'] = df['months_after_1_69'].apply(pd.to_datetime, unit = 'M')
    df= pd.DataFrame(df)
    df['date'] = pd.date_range(start='01/01/1969', end='12/31/1984', freq='M')
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y%m%d'))
    df = df[[ u'DriversKilled', u'front', u'rear', u'date']]
    df = df.rename(columns={'DriversKilled': 'Drivers killed',
                            'front': 'Front seat passangers killed',
                            'rear': 'Rear seat passangers killed'})

    df.to_csv('../data/seatbelts_full.csv', sep='\t', index=False)


# main
# *********************************

if __name__ == '__main__':
    main()


