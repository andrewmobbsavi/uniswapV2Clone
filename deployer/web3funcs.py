
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

    #Set the token contract so we can work with it
    tokenContract = web3.eth.contract(address=address_to, abi=tokenabi)

    #Prepare the transaction and function interaction
    mintTokensTx = tokenContract.functions.mint(account_from["address"]).build_transaction(
        {
            "from": Web3.to_checksum_address(account_from["address"]),
            "nonce": web3.eth.get_transaction_count(
                Web3.to_checksum_address(account_from["address"])
            ),
        }
    )

    #Sign tx with Private Key
    tx_create = web3.eth.account.sign_transaction(mintTokensTx, account_from["private_key"])

    # 7. Send tx and wait for receipt
    tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Tx successful with hash: { tx_receipt.transactionHash.hex() }")