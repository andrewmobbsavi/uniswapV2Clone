
from web3 import Web3
import constants
import json
import time



def getAbi(abiPath):
    with open(abiPath) as f:
        info_json = json.load(f)

    abi = info_json["abi"]
    return abi

'''
Prepares the contract for the RPC call
'''
def prepareRPC(contractAddress, abiLocation):
    tokenabi = getAbi(abiLocation)

    web3 = Web3(Web3.HTTPProvider(constants.RPC_ENDPOINT))

    accountFrom = {
        'private_key': constants.PRIVATE_KEY,
        'address': constants.FEE_RECIPIENT,
    }

    #set the token contract so we can work with it
    tokenContract = web3.eth.contract(address=contractAddress, abi=tokenabi)

    return web3, accountFrom, tokenContract


def submitTransaction(web3, tx, privateKey):
    #Sign tx with Private Key
    txCreate = web3.eth.account.sign_transaction(tx, privateKey)

    # 7. Send tx and wait for receipt
    txHash = web3.eth.send_raw_transaction(txCreate.rawTransaction)
    txReceipt = web3.eth.wait_for_transaction_receipt(txHash)

    return txReceipt


'''
Add liquidity to Uniswap V2 pair, or create new pair.
This calls the periphery router to add liquidity

address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline

'''
def addLiquidity(contractAddress, tokenA, tokenB, amountADesired, amountBDesired, amountAMin, amountBMin, recipientAddress, deadline, abiLocation):
    # tokenabi = getAbi("../uniswapv2periphery/out/UniswapV2Router02.sol/UniswapV2Router02.json")
    rpcParams = prepareRPC(contractAddress, abiLocation)

    print(
        f'Attempting to add liquidity from { rpcParams[1]["address"] } to { contractAddress }'
    )

    #Prepare the transaction and function interaction
    addLiquidityTx = rpcParams[2].functions.addLiquidity(rpcParams[1]["address"], tokenA, tokenB, amountADesired, amountBDesired, amountAMin, amountBMin, recipientAddress, deadline).build_transaction(
        {
            "from": Web3.to_checksum_address(rpcParams[1]["address"]),
            "nonce": rpcParams[0].eth.get_transaction_count(
                Web3.to_checksum_address(rpcParams[1]["address"])
            ),
        }
    )

'''
Mints new tokens on an ERC20 token
'''
#https://docs.moonbeam.network/builders/build/eth-api/libraries/web3py/
def mintToken(contractAddress, abiLocation):
    rpcParams = prepareRPC(contractAddress, abiLocation)

    print(
        f'Attempting to send transaction from { rpcParams[1]["address"] } to { contractAddress }'
    )

    #Prepare the transaction and function interaction
    mintTokensTx = rpcParams[2].functions.mint(rpcParams[1]["address"]).build_transaction(
        {
            "from": Web3.to_checksum_address(rpcParams[1]["address"]),
            "nonce": rpcParams[0].eth.get_transaction_count(
                Web3.to_checksum_address(rpcParams[1]["address"])
            ),
        }
    )

    txReceipt = submitTransaction(rpcParams[0], mintTokensTx, rpcParams[1]["private_key"])

    print(f"\n\nTx successful with hash: { txReceipt.transactionHash.hex() }\n\n")