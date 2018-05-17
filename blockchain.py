import hashlib
import json
from testwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class BlockChain(object):
    def __init__(self):
	self.chain = []
	self.current_transaction = []
        
        # create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """create a new block and add it to the chain
	    :param proof:<int> the proof given by the proof of work algorithm
            :param previous_hash: <str> hash of the previous block
            :return <dict> new block
	"""

        block = {
	    'index': len(self.chain) + 1,
            'timestamp': time(),
	    'transaction': self.current_transaction,
            'proof': proof,
	    'previous_hash': previous_hash or self.hash(self.chain[-1]),
	}
	
	#reset the current list of transactions
        self.current_transaction = []
	self.chain.append(block)
	return block

    def new_transaction(self, sender, recipient, amount):
        """ add a new transaction to the list of transactions
	    :param sender: <str> address of the sender
            :param recipient: <str> address of the recipient
	    :param amount: <int> amount
	    :return <int> the index of the block that will hold this transaction
        """
	self.current_transaction.append({
	    'sender': sender,
            'recipient': recipient,
	    'amount': atmount,
	})
	return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hash a block
        """
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
	return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # return the last block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
	"""
        :param last_proof: <int>
        :return: <int>
        """
	proof = 0
        while self.valid_proof(last_proof, proof) is False:
	    proof += 1

	return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
	
	guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  

# instantiate our node
app = Flask(__name__)

# generate a globally unique address for the node
node_identifier =  str(uuid4()).replace('-','') 

# instantiate the blockchain
blockchain = BlockChain()

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # 给工作量证明的节点提供奖励.
    # 发送者为 "0" 表明是新挖出的币
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    block = blockchain.new_block(proof)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('transactions/new',methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', method=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

# https://learnblockchain.cn/2017/10/27/build_blockchain_by_python/
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
