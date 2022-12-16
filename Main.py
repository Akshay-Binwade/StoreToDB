'''
This project is for illustration purpose of connecting and storing data to DATABASE.
'''

import pymysql
from fetch_data import Fetch


def Store():
    '''
    film is an example here to store the info in the respective database
    '''

    connector = pymysql.connect(host="localhost",user="root",password="root",database="practice")
    mycursor = connector.cursor()

    url = "https://swapi.dev/api/films/2"

    fetch_obj = Fetch(url)          # This is object instantiation

    values_ = tuple(fetch_obj.get_values_())   # The get_values() method will be returning list of values.

    # print(values_)
    try:
        # mycursor.execute("use practice;")
        # To pass the command to the mysql we have to use .execute followed by command.
        mycursor.execute(f"""INSERT INTO film (title, episode_id, opening_crawl, director, producer, release_date, characters, planets, starships,vehicles,species, created, edited, url) VALUES {values_};""")
        # We here are passing the columns and values in the insert command
        connector.commit()
        print("done")

    except:
        print("Database Error")


Store()