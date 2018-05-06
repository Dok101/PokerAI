from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import _pick_unused_card, _fill_community_card, gen_cards
import numpy as np

class PokerAI(BasePokerPlayer):

    def __init__ (self):
        self.num = input('What version is this?') #To use all Ryzen's cores, run the script multiple times. Maybe implement multithreading later?
        self.cards = [[0 for a in range(367)] for b in range(5)] #Initialise Cards object
        self.row = 0 #Which row of the cards object am I writing to
        self.cardnum = 0#To determine which order this card came in e.g. hole card = 0, 1
    
    global converter
    converter = {'HA':1,'H2':2,'H3':3,'H4':4,'H5':5,'H6':6,'H7':7,'H8':8,'H9':9,'HT':10,'HJ':11,'HQ':12,'HK':13,'CA':14,'C2':15,'C3':16,'C4':17,'C5':18,'C6':19,'C7':20,'C8':21,'C9':22,'CT':23,'CJ':24,'CQ':25,'CK':26,'SA':27,'S2':28,'S3':29,'S4':30,'S5':31,'S6':32,'S7':33,'S8':34,'S9':35,'ST':36,'SJ':37,'SQ':38,'SK':39,'DA':40,'D2':41,'D3':42,'D4':43,'D5':44,'D6':45,'D7':46,'D8':47,'D9':48,'DT':49,'DJ':50,'DQ':51,'DK':52}

    def receive_game_start_message(self, game_info):
        self.num_players = 10

    def receive_round_start_message(self, round_count, hole_card, seats):
        for c in range (0,5):
            for card in hole_card:
                self.cards[c][converter[str(card)] + (52 * self.cardnum) - 1] = 1 
                self.cardnum += 1
            self.cards[c][-1] = 1
            self.cardnum = 0
        self.cardnum = 2
    def receive_street_start_message(self, street, round_state):
        print (street)
        print (round_state)
        self.row += 1
        for j in range(0, len(round_state['community_card'])):
            self.cards[self.row][converter[str(round_state['community_card'][j])] + (52 * self.cardnum) - 1] = 1 
            self.cardnum += 1
        self.cardnum = 2
        num = 0

        for l in range (1, 10):
            if str(round_state['seats'][l]['state']) == 'participating':
                num += 1
            else:
                continue
        self.cards[self.row][364] = int(num)
        self.cards[self.row][365] = int(round_state['pot']['main']['amount'])

        if str(round_state['seats'][0]['state']) != 'participating':
            self.cards[self.row][-1] = 0

    def receive_game_update_message(self, action, round_state):
        pass

    def declare_action(self, valid_actions, hole_card, round_state):
        actions = [item for item in valid_actions if item['action'] in ['call']]
        action = 'call'
        amount = valid_actions[1]['amount']
        if amount < 100:
            return action, amount
        else:
            return 'fold', 0

    def receive_round_result_message(self, winners, hand_info, round_state):
        index = [1, 4, 5, 6]
        is_winner = self.uuid in [item['uuid'] for item in winners]
        dataFile = open(r'C:\Users\Devin\Desktop\PokerBot\HandData' + str(self.num) + '.txt', 'a')
        del self.cards[0]
        numCols = 0
        for a in range (0, 4):
            if self.cards[a][-1] == 0:
                continue
            else:
                for b in range (0, 366):
                    dataFile.write('{} '.format(self.cards[a][b]))
                dataFile.write('\n')
                numCols += 1
        resultsFile = open(r'C:\Users\Devin\Desktop\PokerBot\HandResults' + str(self.num) + '.txt', 'a')
        for d in range (0, numCols):
            if (is_winner):
                resultsFile.write('1' + '\n')
            else:
                resultsFile.write('0' + '\n')
        self.cards = [[0 for a in range(367)] for b in range(5)]
        self.row = 0
        self.cardnum = 0

def setup_ai():
    return PokerAI()
