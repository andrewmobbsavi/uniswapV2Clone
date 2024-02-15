# Uniswap V2 Clone

Deploying a Uniswap V2 clone is tedious because of the numerous dependencies, many of which are outdated.

The Uniswap V2 Clone application provides a simple way to build and deploy a clone of the Uniswap V2 exchange to any chain which supports the Ethereum Virtual Machine.

The application requires Foundry to be installed. Foundry is a development library for smart contract development.

By default, the application currently deploys 5 tokens (1 base WETH token, and 4 miscellaneous tokens) to allow for testing.

The application deploys the Uniswap V2 Core contracts. From the Uniswap V2 Periphery, the application only deploys the Uniswap V2 Router02. Uniswap V2 Router01 is deprecated. The original Migrator contract from the V2 Periphery is also ignored; this file relates to V1 to V2 migration, which we do not require.

## Getting Started wtih Default Local Development

The following will deploy the Uniswap V2 contracts and 5 token contracts to a local blockchain running on Anvil

1. Install Foundry
2. Install Python 3
3. `pip install python-dotenv`
4. `cd deployer`
5. `cp .env.example .env`
6. `python3 deployer.py`


