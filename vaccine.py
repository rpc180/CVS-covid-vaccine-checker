'''
This is a python script that requires you have python installed, or in a cloud environment.

This script scrapes the CVS website looking for vaccine appointments in the cities you list.
To update for your area, update the locations marked with ### below.

If you receive an error that says something is not install, type

pip install beepy

in your terminal.
'''



import requests
import time
import beepy


def findAVaccine():
    hours_to_run = 3 ###Update this to set the number of hours you want the script to run.
    max_time = time.time() + hours_to_run*60*60
    while time.time() < max_time:

        state = 'IL' ###Update with your state abbreviation. Be sure to use all CAPS, e.g. RI

        response = requests.get("https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{}.json?vaccineinfo".format(state.lower()), headers={"Referer":"https://www.cvs.com/immunizations/covid-19-vaccine"})
        payload = response.json()

        mappings = {}
        for item in payload["responsePayloadData"]["data"][state]:
            mappings[item.get('city')] = item.get('status')

        print(time.ctime())
        cities = ['BELLEVILLE', 'CHICAGO', 'DEKALB', 'WAUKEGAN'] ###Update with your cities nearby
        for city in cities:
            print(city, mappings[city])

        for key in mappings.keys():
            if (key in cities) and (mappings[key] != 'Fully Booked'):
                beepy.beep(sound = 'coin')
                break
            else:
                pass

        time.sleep(60) ##This runs every 60 seconds. Update here if you'd like it to go every 10min (600sec)
        print('\n')

findAVaccine() ###this final line runs the function. Your terminal will output the cities every 60seconds
