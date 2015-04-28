#!/usr/bin/env python
"""
coding=utf-8
"""
# imports
# *********************************
import pandas as pd
import numpy as np
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
    df = pd.read_csv('../data/movies.csv', )
    # df['genre'] = 0
    df['genre'] = np.nan
    genre_list = ['Action', 'Animation', 'Comedy', 'Drama', 'Documentary', 'Romance', 'Short']
    for genre in genre_list:
        df[genre] =  df[genre].replace({1: genre, 0: np.nan})
        df['genre'] = df['genre'].fillna(df[genre])

    df['genre'] = df['genre'].fillna('')

    df.to_csv('../data/movies_with_genre.csv')

    df_subset =df[df['votes'] > 40000]

    df_subset.to_csv('../data/movies_with_genre_subset.csv')
    avg_rating_df =  df.groupby(['year', 'genre']).mean()['rating'].unstack()
    avg_rating_df = avg_rating_df[['Action', 'Comedy', 'Romance']]
    avg_rating_df = avg_rating_df[avg_rating_df.index > 1966]

    avg_rating_df['Action'] = avg_rating_df['Action'].round(2)
    avg_rating_df['Comedy'] = avg_rating_df['Comedy'].round(2)
    avg_rating_df['Romance'] = avg_rating_df['Romance'].round(2)

    avg_rating_df['date'] = avg_rating_df.index

    avg_rating_df.to_csv('../data/avg_rating_by_genre.csv',  sep='\t', index=False)


# main
# *********************************

if __name__ == '__main__':
    main()


