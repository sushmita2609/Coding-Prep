import random
import math
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
                    level=logging.INFO, filename='NoGuessing.log')


class Guess:
    def __init__(self, upper, lower):
        self.upper = upper
        self.lower = lower

    def guess_number(self):
        x = random.randint(self.lower, self.upper)
        print("\n\tYou've only ", round(math.log(self.upper - self.lower + 1, 2)), " chances to guess the integer!\n")
        count = 0
        while count < math.log(self.upper - self.lower + 1, 2):
            count += 1
            g = int(input("Guess a number:- "))
            if x == g:
                print("Congratulations you did it in ", count, " try")
                logging.info('success')
                break
            elif x > g:
                print("You guessed too small!")
            elif x < g:
                print("You Guessed too high!")
        if count > math.log(self.upper - self.lower + 1, 2):
                print("\nThe number is %d" % x)
                print("\tBetter Luck Next time!")
                logging.info('fail to guess')
        logging.info('exit')



if __name__ == "__main__":
    print("===welcome to Number Guessing game===")
    logging.info('start')
    try:
        lr = int(input("Enter Lower bound: "))
        up = int(input("Enter Upper bound: "))
        gu = Guess(up, lr)
        gu.guess_number()
    except:
        print('upper value should be greater than lower value')
        logging.error("ValueError Upper value is smaller than lower value")
        logging.info('exit')

