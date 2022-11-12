from rpc_connection import RPCConnection

def main():
    url = 'https://rpc.ankr.com/eth'
    rc = RPCConnection(url)

    block_num = rc.get_block_number()
    print('Current block number is:', block_num)

    distance = rc.get_distance_from_latest_block(1337)
    print('Distance from the current block number is:', distance)

    # To get an example address, search for a few on etherscan
    balance = rc.get_balance_of_address('0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5')
    print('Current balance:', balance)

    txn = rc.get_txn_by_hash('0x2968f078c8645d98a3bc9de7c4a7b3d4bd844e8ae9c98782baabe5a3ea5937c0')
    print('Transaction details:', txn)

    print('Starting to display transactions for block:', block_num)
    rc.display_txn_details_for_block(block_num)
    print('Completed displaying transactions for block:', block_num)

    gas_px = rc.get_gas_price_estimate_from_last_block()
    print('Gas price from last block:',gas_px)

    gas_px_eth = rc.convert_from_wei_to_eth(gas_px)
    print('Gas price from last block in ETH:',gas_px_eth)
    
    # Do not push your own private key to GitHub, ever.
    public_key = rc.create_account_from_private_key('0xTestReplaceWithTestPrivateKeyForDevOnly')
    print('Public key address creating from private key:', public_key.address)

main()