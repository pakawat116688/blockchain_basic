import hashlib
import json
from time import time
from random import randint

# สร้าง class blockchain ไว้ใช้งาน
class Blockchain(object):
    
    # constructor
    def __init__(self):
        self.chain = []
        self.transaction = []
        self.hash_value = [] 
        self.first_block(previous_hash="first Block", proof="miner GOD")

    # สำหรับการสร้างบล็อกแรกขึ้นมา ซึ่งจะทำงานพร้อม constructor
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

    # ใช้ในการสร้างบล็อกใหม่ขึ้นมาต่อกันเป็น chain
    def new_block(self,proof):
        block = {
            'index': len(self.chain) + 1,
            'time_stamp': time(),
            'transactions': self.transaction,
            'proof': proof,
            'previous_hash': self.hash(self.chain[-1]),
        }
        self.hash_value.append(self.hash(self.chain[-1]))
        self.transaction = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]

    # ใช้ในการสร้างข้อมูลใหม่ขึ้นมาเพื่อนำไปเก็บลงใน block
    def new_transaction(self, sales_team, buyer_team, amount, player):
        transaction = {
            'Sales_team': sales_team,
            'Buyer_team': buyer_team,
            'Amount': amount,
            'Player': player
        }
        self.transaction.append(transaction)

        return self.last_block['index'] + 1

    # สร้างค่า hash ของแต่ละ block ขึ้นมา
    def hash(self, block):
        string_obj = json.dumps(block, sort_keys=True)
        block_str = string_obj.encode()
        
        raw_hash = hashlib.sha256(block_str)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    # ตรวจสอบความถูกต้องว่าข้อมูลถูกแก้ไขหรือไหม
    def data_verification(self,block_number):
        print("self.hash_value[block_number]",self.hash_value[block_number])
        print("self.hash(self.chain[block_number])",self.hash(self.chain[block_number]))
        return self.hash(self.chain[block_number]) == self.hash_value[block_number]

    # แสดงข้อมูลในบล็อกนั้นออกมาให้ผู้ใช้งานเห็นข้อมูล
    def show(self,block_number):
        return json.dumps(self.chain[block_number],indent=4)

    # แสดงข้อมูลในบล็อกนั้นออกมาให้ผู้ใช้งานเห็นข้อมูล
    def show_all(self):
        return json.dumps(self.chain,indent=4)


# global variable OOP Blockchain()
blockchain = Blockchain()

# function สำหรับทำการเพิ่มค่าข้อมูลเข้าไป
def add_data():
    sales_team = input("sales_team: ")
    buyer_team = input("buyer_team: ")
    player = input("player: ")
    amount = input("amount: ")
    _tx = blockchain.new_transaction(sales_team, buyer_team, amount, player)
    ramdom = randint(1,100)
    miner = "miner"+str(ramdom)
    blockchain.new_block(miner)
    print() #ให้ขึ้นบรรทัดใหม่

# function สำหรับแสดงข้อมูล
def view_info():
    block_number = int(input("Choose number of block do you want to see: "))
    print("Blockchain: ",blockchain.show(block_number-1))
    data_verification = blockchain.data_verification(block_number-2)
    print("Data Verification :",data_verification,"\n") 

# main ของการทำงานหลัก
while True:
    print("Transfer choose:1")
    print("View information choose:2")
    print("View information (All) choose:3")
    print("Out blockchain choose:4")
    choose = input("Choose:")
    if choose == "1":
        add_data()
    elif choose == "2":
        view_info()
    elif choose == "3":
        blockchain.show_all()
    elif choose == "4":
        break