import random
from web3 import Web3


VALUE_RANGE_MON = [0.00001, 0.001]

w3 = Web3()
first_value = w3.to_wei(VALUE_RANGE_MON[0], 'ether')
second_value = w3.to_wei(VALUE_RANGE_MON[1], 'ether')
RANGE_SWAP = random.randint(first_value, second_value)

WAIT_TIME = [1, 10]
THREADS = 3