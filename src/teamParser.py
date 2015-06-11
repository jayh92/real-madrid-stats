import json
from io import StringIO

class Player:
    def __init__(self, player):
        self.id = player[u'id']
        self.name = player[u'name']
        self.position = player[u'position']
        self.number = player[u'jerseyNumber']
        self.dob = player[u'dateOfBirth']
        self.country = player[u'nationality']
        self.contractExpires = player[u'contractUntil']
        self.marketValue = player[u'marketValue']


class TeamParser:
    def __init__(self, players):
        self.players = players.json() # json object 
        self.playerList = {}
        self.currentPlayer = None # current player
        self.url = players.url # API endpoint
        self.playerCount = self.getPlayerCount() # how many players on this team
        self.setPlayerData()
        
        self.printTeamInfo()


    # done
    def printPlayerData(self, pos):
        playerNo = pos + 1

        playerStr = str(playerNo) + ': ' + self.playerList[pos].name + '\n\tID: ' + str(self.playerList[pos].id) + \
        '\n\tPosition: ' + self.playerList[pos].position + '\n\tNumber: ' + str(self.playerList[pos].number) + \
        '\n\tDOB: ' + str(self.playerList[pos].dob) + '\n\tCountry: ' + str(self.playerList[pos].country) \
        + '\n\tContract Expires: ' + str(self.playerList[pos].contractExpires) + '\n\tMarket Value: ' + \
        self.playerList[pos].marketValue

        print(playerStr + '\n')

    # done
    def setPlayerData(self):
        players = self.players[u'players']
        count = 0

        for player in players:
            self.playerList[count] = self.getPlayerInfo(player)
            count += 1
                 
    # done       
    def getPlayerInfo(self, player):
        return Player(player)

    # done
    def getPlayerCount(self):
        return self.players['count']

    # done
    def getUrl(self):
        return self.url

    # done
    def setUrl(self, url):
        self.url = url

    # done
    def setPlayer(self, player):
        self.currentPlayer = player

    # done
    def getPlayer(self):
        return self.currentPlayer

    # done
    def printPlayers(self):
        print(self.players)

    def printPlayers2(self):
        for i in range(self.playerCount):
            self.printPlayerData(i)

    def printTeamInfo(self):
        titleStr = '\n*****************************************\n' + \
                   '*************** REAL MADRID *************\n' + \
                   '*****************************************\n' + \
                   '******    Players on Roster: ' + str(self.playerCount) + \
                   '    ******\n*****************************************\n'
        print (titleStr)
        self.printPlayers2()
        endStr = '*****************************************\n'
        print (endStr)
