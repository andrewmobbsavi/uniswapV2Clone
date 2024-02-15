import os


"""
Adds token to the blockchain
"""
def deployToken(tokenName, tokenCode, tokenDecimals, privateKey, endpoint, separator):
    print(separator)
    print(f"Creating {tokenName} token ({tokenCode})")
    output = os.popen(f"cd ../erc20; forge create --rpc-url {endpoint} --private-key {privateKey} src/Token.sol:Token 
                      --constructor-args '{tokenName}' '{tokenCode}' {tokenDecimals}").read()
    
    print(f"{tokenName} token deployed...")

    return output

'''
Deploys tokens to chain and gets addresses. Returns dictionary of token details and address
'''
def deployTokens(utilsCustom, tokenDefinitions, privateKey, endpoint, separator):
    #Perhaps need to change this to named dictionary rather than array. See if need arises
    tokens = []
    for token in tokenDefinitions.defineTokens():
        baseTokenOutput = deployToken(token["tokenName"], token["tokenCode"], token["tokenDecimals"], privateKey, endpoint, separator)
        tokenAddress = utilsCustom.getDeploymentAddress(baseTokenOutput)
        tokens.append({
            "tokenName": token["tokenName"],
            "tokenCode": token["tokenCode"],
            "tokenDecimals": token["tokenDecimals"],
            "contractAddress": tokenAddress
    })
        
    return tokens

"""
Deploy V2 Core
"""
def deployV2erc20(endpoint, privateKey, separator):
    print(separator)
    print(f"Deploying the Uniswap V2 Core ERC20 Contract...")
    output = os.popen(f"cd ../uniswapv2core; forge create --rpc-url {endpoint} --private-key {privateKey} src/UniswapV2ERC20.sol:UniswapV2ERC20").read()
    print(f"Uniswap V2 ERC20 Core Contract deployed...")
    return output

def deployV2Factory(endpoint, privateKey, feeRecipient, separator):
    print(separator)
    print(f"Deploying the Uniswap V2 Core UniswapV2Factory Contract...")
    output = os.popen(f"cd ../uniswapv2core; forge create --rpc-url {endpoint} --private-key {privateKey} src/UniswapV2Factory.sol:UniswapV2Factory 
                      --constructor-args '{feeRecipient}'").read()
    print(f"Uniswap V2 UniswapV2Factory Core Contract deployed...")
    return output

def deployV2Pair(endpoint, privateKey, separator):
    print(separator)
    print(f"Deploying the Uniswap V2 Core UniswapV2Pair Contract...")
    output = os.popen(f"cd ../uniswapv2core; forge create --rpc-url {endpoint} --private-key {privateKey} src/UniswapV2Pair.sol:UniswapV2Pair").read()
    print(f"Uniswap V2 UniswapV2Pair Core Contract deployed...")
    return output


def deployV2CoreContracts(utilsCustom, endpoint, privateKey, feeRecipient, separator):
    coreV2Erc20Output = deployV2erc20(endpoint, privateKey, separator)
    coreV2FactoryOutput = deployV2Factory(endpoint, privateKey, feeRecipient, separator)
    coreV2PairOutput = deployV2Pair(endpoint, privateKey, separator)

    v2Core = {
            "UniswapV2ERC20": {
                "contractAddress": utilsCustom.getDeploymentAddress(coreV2Erc20Output)
            },
            "UniswapV2Factory": {
                "contractAddress": utilsCustom.getDeploymentAddress(coreV2FactoryOutput)
            },
            "UniswapV2Pair": {
                "contractAddress": utilsCustom.getDeploymentAddress(coreV2PairOutput)
            },
        }

    return v2Core



"""
Deploy V2 Periphery
"""

'''
Periphery consists of only Router 02, despite the fact that 01 and Migrator exist in the repo
We do not need Router 01 or the Migrator to create a working DEX
'''
def deployV2Periphery(endpoint, privateKey, factoryAddress, wethAddress, utilsCustom, separator):
    print(separator)
    print(f"Deploying the Uniswap V2 Core Router2 Contract...")

    UniswapV2Router02Output = os.popen(f"cd ../uniswapv2periphery; forge create --rpc-url {endpoint} --private-key {privateKey} 
                                       src/UniswapV2Router02.sol:UniswapV2Router02 --constructor-args '{factoryAddress}' '{wethAddress}'").read()
    print(f"Uniswap V2 Periphery UniswapV2Router02 Core Contract deployed...")

    v2Periphery = {
            "UniswapV2Router02": {
                "contractAddress": utilsCustom.getDeploymentAddress(UniswapV2Router02Output)
            }
        }

    return v2Periphery
    