
# for generating random numbers
from random import randrange

class RPSPlayer():
    name = ""
    move = 0
    pastmoves = []


    def __init__(self,playername):
        name = playername

    #decides move based on how much of each move opponent plays,
    def my_rps_play_strategy(pastmoves):
        rocknum = 0
        scissornum = 0
        papernum = 0

        #finds raw amount of rock,paper,and scissors moves
        # assumes that past moves only holds opponents moves
        for i in pastmoves:
            if i == 0:
                rocknum += 1
            if i == 1:
                papernum += 1
            if i == 2:
                scissornum += 1

        # total amount played
        totalnum = rocknum + scissornum + papernum

        #probability (1 to 100) for the next move, based on how often opponent has played the winning and tieing
        # conditions for that move
        rockprob = ((1 - (scissornum + rocknum)/totalnum) * 100)
        paperprob = ((1 - (rocknum + papernum)/totalnum) * 100)
        scissorprob = ((1- (papernum + scissornum)/totalnum) * 100)

        #random number from 1 to 100, used for determining what move to make
        randprob = randrange(1,100)

        if randprob < rockprob:
            move = 0
        if randprob > rockprob & randprob < (rockprob + paperprob):
            move = 1
        else:
            move = 2

