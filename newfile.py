import hashlib
import time

class Block:
    #index—this keeps track of the position of the block within the blockchain;
    #proofnumber—this is the number produced during the creation of a new bloc(mining)
    #pref_hash-this refers to the hash of the previous block within the chain
    #data—this gives a record of all transactions completed, such as the quantity bought
    #timestamp—this places a timestamp for the transactions.


    def __init__(self, index, proofnumber, previous_hash, data, timestamp=None):
        self.index = index
        self.proofnumber = proofnumber
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    #hashes the block
    def get_hash(self):
        block_string = f"{self.index}{self.proofnumber}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"{self.index}-{self.proofnumber}-{self.previous_hash}-{self.data}-{self.timestamp}"

class BlockChain():

    def __init__(self):
        #self.chain—this variable keeps all blocks;
        self.chain = []
        #self.current_data—this variable keeps all the completed transactions in the block;
        self.current_data = []
        self.nodes = set() 
        #self.build_genesis() — this method is used to create the initial block in the chain.  
        self.build_genesis()

    def build_genesis(self):
        self.build_block(proofnumber=0, previous_hash=0)

    def build_block(self, proofnumber=0, previous_hash=0):
        block = Block(
            index = len(self.chain), 
            proofnumber = proofnumber,
            previous_hash = previous_hash,
            data = self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(self, block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.get_hash != block.previous_hash:
            return False
        elif block.timestamp <= prev_block.timestamp:
            return False
        return True

    def new_data(self, sender, recipient, quantity):
        self.current_data.append({
            'sender':sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes 
        f is the previous f'
        f' is the new proof 
        '''
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):

        self.new_data(
            sender=0,
            recipient=details_miner,
            quantity=1
        )

        last_block = self.last_block

        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.get_hash
        block = self.build_block(proof_no, last_hash)

        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(self,block_data):
        return Block(
            block_data['index'],
            block_data['proofnumber'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp']
        )

blockchain = BlockChain()

print("***Mining MellowCoin about to start***")
print(blockchain.chain)

last_block = blockchain.last_block
last_proof_no = last_block.proofnumber
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",  #it implies that this node has created a new block
    recipient="Fake Name",  #let's send Quincy some coins!
    quantity=
    1,  #creating a new block (or identifying the proof number) is awarded with 1
)

last_hash = last_block.get_hash()
block = blockchain.build_block(proof_no, last_hash)

print("***Mining MellowCoin has been successful***")
print(blockchain.chain)