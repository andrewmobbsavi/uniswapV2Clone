import constants
import chainfuncs
import utilsCustom
import tokenDefinitions
import web3funcs
import time

'''
This will generate the abi only for the selected file
forge build --silent && jq '.abi' ./out/MyContract.sol/MyContract.json
'''

def deployContracts():
    print(f"Deploying DEX and test tokens to . Each step may take a while if running for the first time because the various compilers need to be downloaded.")
    print("Please be patient...")
    print("If the process takes longer than 10 minutes, then something has gone wrong.")

    utilsCustom.checkAnvil()

    #Deploy tokens and create array of dictionaries with token details including deploy address
    tokenContracts = chainfuncs.deployTokens(utilsCustom, tokenDefinitions, constants.PRIVATE_KEY, constants.RPC_ENDPOINT, constants.SEPARATOR)

    #Deploy Uniswap V2 Core and create array of dictionaries with contract details including deploy address
    v2CoreContracts = chainfuncs.deployV2CoreContracts(utilsCustom, constants.RPC_ENDPOINT, constants.PRIVATE_KEY, constants.FEE_RECIPIENT, constants.SEPARATOR)

    v2PeripheryContracts = chainfuncs.deployV2Periphery(constants.RPC_ENDPOINT, constants.PRIVATE_KEY, v2CoreContracts['UniswapV2Factory']['contractAddress'], 
                                                        tokenContracts[0]['contractAddress'], utilsCustom, constants.SEPARATOR)


    print(constants.SEPARATOR)
    print("Token Contracts")
    print(constants.SEPARATOR)
    print(tokenContracts)

    print(constants.SEPARATOR)
    print("V2 Core Contracts")
    print(constants.SEPARATOR)
    print(v2CoreContracts)

    print(constants.SEPARATOR)
    print("V2 Periphery Contracts")
    print(constants.SEPARATOR)
    print(v2PeripheryContracts)

    return tokenContracts, v2CoreContracts, v2PeripheryContracts


def mintTokens(contracts):
    if contracts:
        print("Minting tokens and assigning to owner account\n")
        
        for contract in contracts[0]:
            print("Minting " + contract['tokenCode'] + " from " + contract['contractAddress'])  
            web3funcs.mintToken(contract['contractAddress'], "../erc20/out/Token.sol/Token.json")

        return True
    else:
        print("\n\nERROR!\n\nNo DEX addresses found. Please choose option 1.\n\n")
        return False




def addLiquidity():
    deadline = int(time.time())
    deadline += 30
    web3funcs.addLiquidity(contractAddress, tokenA, tokenB, amountADesired, amountBDesired, amountAMin, amountBMin, recipientAddress, deadline, abiLocation)



def main():
    runme = True

    contracts = ()

    while runme:
        print("--------------------------")
        print("Uniswap Clone V2 Deployer")
        print("--------------------------\n")
        menu = str(input("Pick an option:\n\n"
                        "1. Deploy DEX contracts to local test environment\n"
                        "2. Mint tokens and assign to owner account " + constants.FEE_RECIPIENT + "\n"
                        "3. Create pair liquidity pools and assign to owner account " + constants.FEE_RECIPIENT + "\n"
                        "4. Start auto background trading on local test environment\n"
                        "x. Exit\n"
                        "\nOption Selected: "))
        if menu == "1":
            contracts = deployContracts()
        elif menu == "2": #Mint Tokens
            if not mintTokens(contracts):
                main()
        elif menu == "3":
            print("Creating pair liquidity pools\n")
            addLiquidity()
        elif menu == "x":
            print("Exiting...")
            runme = False


main()