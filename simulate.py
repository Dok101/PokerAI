from pypokerengine.api.game import start_poker, setup_config
import sys
from MonteCarlo import MonteBot
from PokerAI import PokerAI
import numpy as np

if __name__ == '__main__':
    
    Poker_AI = PokerAI()

    # The stack log contains the stacks of the Data Blogger bot after each game (the initial stack is 100)
    stack_log = []
    for round in range(20000):
        p1 = Poker_AI
        p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = MonteBot()

        config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
        config.register_player(name="p1", algorithm=p1)
        config.register_player(name="p2", algorithm=p2)
        config.register_player(name="p3", algorithm=p3)
        config.register_player(name="p4", algorithm=p4)
        config.register_player(name="p5", algorithm=p5)
        config.register_player(name="p6", algorithm=p6)
        config.register_player(name="p7", algorithm=p7)
        config.register_player(name="p8", algorithm=p8)
        config.register_player(name="p9", algorithm=p9)
        config.register_player(name="p10", algorithm=p10)

        game_result = start_poker(config, verbose=0)
        stack_log.append([player['stack'] for player in game_result['players'] if player['uuid'] == Poker_AI.uuid])
        print('Avg. stack:', '%d' % (int(np.mean(stack_log))))
    sys.exit()

