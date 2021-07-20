import json
import hashlib
from time import time


# main class
class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.pending_transaction = []
        self.add_new_block(previous_hash="money send one person to another", proof=100)

    # add this method used for add new blocks
    def add_new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'time of transaction': time(),
            'transaction': self.pending_transaction,
            'proof': proof,
            'previous hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transaction = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    # this method used to make dictionary of transaction details
    def new_transaction(self, send, reciever, amount):
        transaction = {
            'send': send,
            'recipient': reciever,
            'amount': amount,
        }
        self.pending_transaction.append(transaction)
        return self.last_block['index'] + 1

    # this method is used for make hashing of each block
    def hash(self, block):
        to_json = json.dumps(block, sort_keys=True)
        to_encode = to_json.encode()
        hashing = hashlib.sha256(to_encode)
        to_hex_digit = hashing.hexdigest()
        return to_hex_digit


block_chain = BlockChain()
t1 = block_chain.new_transaction("yadu", "vishnu", "2BTC")
t2 = block_chain.new_transaction("vyshak", "unni", "2BTC")
t3 = block_chain.new_transaction("nandu", "vishnu", "2BTC")
block_chain.add_new_block(10000)
t4 = block_chain.new_transaction("molty", "monu", '1 BTC')
t5 = block_chain.new_transaction("chinju", "unnimol", '7 BTC')
t6 = block_chain.new_transaction("jithu", "appu", '3 BTC')
block_chain.add_new_block(20000)
print(json.dumps(('block chain :', block_chain.chain), sort_keys=True, indent=2))
