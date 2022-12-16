'''
This class will be returning values_ which will be used as values to store in the database table.
'''
import requests

class Fetch():

    def __init__(self,url):
        self.response = requests.get(url)
        self.response = self.response.json()

        # Since the dict format data cannot be used to store in the database,
        # We will take out the values and pass them to the query.

    def get_values_(self):
        values_ = []  # To store the values in str format

        for key, value in self.response.items():
            '''
            Some values in our response are in list format, we cannot pass them in to the query,
            so we will convert the list of urls into a single string
            '''
            if isinstance(value, list):            # To filter the list of urls against characters, planets, etc
                values_.append(", ".join(value))   # Joining the urls and making one single string
            else:
                values_.append(value)              # Appending values like, title, producer, director, etc
        return values_


# f= Fetch("https://swapi.dev/api/films/2")
# print(f.get_keys())
# print(f.get_values_())
# print(f.response)