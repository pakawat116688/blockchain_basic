import hashlib
import json
from time import time
from random import randint

string = "The time 03/jan/2009 chancellor on brink of second bailout for bank."

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.block = {}
        self.transaction = []
        self.first_block(previous_hash=string, proof=100)

    def new_block(self,previous_hash,proof):
        block = {
            'index': len(self.chain) + 1,
            'time_stamp': time(),
            'transactions': self.transaction,
            'proof': proof,
            'previous_hash': self.hash(self.chain[-1]),
        }
        self.transaction = []
        self.chain.append(block)

        return block

    def first_block(self,previous_hash,proof):
        block = {
            'index': len(self.chain) + 1,
            'time_stamp': time(),
            'transactions': self.transaction,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.transaction = []
        self.chain.append(block)

        return block
    
    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'ผู้ซื้อ': sender,
            'ผู้ขาย':recipient,
            'amount': amount
        }
        self.transaction.append(transaction)

        return self.last_block['index'] + 1

    def hash(self, block):
        string_obj = json.dumps(block, sort_keys=True)
        block_str = string_obj.encode()
        
        raw_hash = hashlib.sha256(block_str)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", "5 btc")
t1 = blockchain.new_transaction("Mike", "Satoshi", "10 btc")
t1 = blockchain.new_transaction("Doraemon", "Noi", "100 btc")
prev = randint(1,10)
prev_str = str(prev)
hex_hash = hashlib.sha256(prev_str.encode()).hexdigest()
blockchain.new_block(hex_hash,12345)
t1 = blockchain.new_transaction("Satoshi", "Mike", "5 btc")
t1 = blockchain.new_transaction("Mike", "Satoshi", "10 btc")
t1 = blockchain.new_transaction("Doraemon", "Noi", "100 btc")
prev = randint(1,10)
prev_str = str(prev)
hex_hash = hashlib.sha256(prev_str.encode()).hexdigest()
blockchain.new_block(hex_hash,12345)
t1 = blockchain.new_transaction("Satoshi", "Mike", "5 btc")
t1 = blockchain.new_transaction("Mike", "Satoshi", "10 btc")
t1 = blockchain.new_transaction("Doraemon", "Noi", "100 btc")
prev = randint(1,10)
prev_str = str(prev)
hex_hash = hashlib.sha256(prev_str.encode()).hexdigest()
blockchain.new_block(hex_hash,12345)

print("Blockchain: ",blockchain.chain)
