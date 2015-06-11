import requests
from teamParser import TeamParser

class ConsumeApi:
    def __init__(self):
        self.headers = {'X-Auth-Token': 'cf310facc79747d7a896173e62b04b4d'}
        self.url = 'http://api.football-data.org/alpha/teams/86/players'

    # Return JSON response object of all Real Madrid's players
    def getRealMadridPlayers(self):
        players = requests.get(self.url, headers=self.headers)
        return players

# Start the application
def main():
    p = ConsumeApi().getRealMadridPlayers()
    parser = TeamParser(p)                

if __name__=="__main__":
    main()