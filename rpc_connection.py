from web3 import Web3, HTTPProvider
import statistics

'''
rpc_connection.py provides the RPCConnection class that currently connects to the Ethereum
blockchain via the Ankr URL. This class consists of various functions for beginners 
interacting with Web3.

Author: BowTiedApu
'''
class RPCConnection:
    def __init__(self, url):
        self.url = url
        self.web3 = Web3(HTTPProvider(self.url))

    def connect(self):
        if (web3.isConnected()):
            print('Already connected')
        else:
            self.web3 = Web3(HTTPProvider(self.url))

    def get_block_number(self):
        if (self.web3.isConnected()):
            return self.web3.eth.block_number
        else:
            print('Not connected to a node, returning a negative (garbage) value')
            return -1

    def get_distance_from_latest_block(self, current_block_num):
        if (self.web3.isConnected()):
            # TODO: Currently assuming ideal input, need to change this to handle garbage input
            return self.web3.eth.block_number - current_block_num
        else:
            print('Not connected to a node, returning a negative (garbage) value')
            return -1

    def get_balance_of_address(self, address):
        if (self.web3.isConnected()):
            # TODO: Currently assuming ideal input, need to change this to handle garbage input
            return self.web3.eth.getBalance(address)
        else:
            print('Not connected to a node, returning a negative (garbage) value')
            return -1
    
    def get_txn_by_hash(self, txn_hash):
        if (self.web3.isConnected()):
            return self.web3.eth.getTransaction(txn_hash)
        else:
            print('Not connected to a node, returning a negative (garbage) value')
            return -1

    def display_txn_details_for_block(self, block_num):
        block = self.web3.eth.getBlock(block_num, True)
        for txn in block.transactions:
            print(txn)
    
    def get_gas_price_estimate_from_last_block(self):
        gas_pxs = []
        block = self.web3.eth.getBlock(self.get_block_number(), True)
        for txn in block.transactions:
            gas_pxs.append(int(txn.gasPrice))
        
        return statistics.mean(gas_pxs)

    def convert_from_wei_to_eth(self, wei):
        return self.web3.fromWei(wei, 'ether')

    def create_account_from_private_key(self, private_key):
        return self.web3.eth.account.from_key(private_key)
