import constants
import chainfuncs
import utilsCustom
import tokenDefinitions


print(f"Deploying DEX and test tokens to {constants.RPC_ENDPOINT}. Each step may take a while if running for the first time because the various compilers need to be downloaded.")
print("Please be patient...")
print("If the process takes longer than 10 minutes, then something has gone wrong.")

utilsCustom.checkAnvil()

#Deploy tokens and create array of dictionaries with token details including deploy address
tokenContracts = chainfuncs.deployTokens(utilsCustom, tokenDefinitions, constants.PRIVATE_KEY, constants.RPC_ENDPOINT, constants.SEPARATOR)

#Deploy Uniswap V2 Core and create array of dictionaries with contract details including deploy address
v2CoreContracts = chainfuncs.deployV2CoreContracts(utilsCustom, constants.RPC_ENDPOINT, constants.PRIVATE_KEY, constants.FEE_RECIPIENT, constants.SEPARATOR)

v2PeripheryContracts = chainfuncs.deployV2Periphery(constants.RPC_ENDPOINT, constants.PRIVATE_KEY, v2CoreContracts['UniswapV2Factory']['contractAddress'], tokenContracts[0]['contractAddress'], utilsCustom, constants.SEPARATOR)


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




