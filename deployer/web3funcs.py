
from web3 import Web3
import constants
import json



def getAbi(abiPath):
    with open(abiPath) as f:
        info_json = json.load(f)

    abi = info_json["abi"]
    return abi

#https://docs.moonbeam.network/builders/build/eth-api/libraries/web3py/
def test(address_to):
    tokenabi = getAbi("../erc20/out/Token.sol/Token.json")


    web3 = Web3(Web3.HTTPProvider(constants.RPC_ENDPOINT))

    account_from = {
        'private_key': constants.PRIVATE_KEY,
        'address': constants.FEE_RECIPIENT,
    }

    print(
        f'Attempting to send transaction from { account_from["address"] } to { address_to }'
    )

    tokenContract = web3.eth.contract(address=address_to, abi=tokenabi)

    print(tokenContract)