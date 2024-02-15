#!/bin/bash
clear
printf "\x1B[32m"

printf " __ __  ____   ____ _____ __    __   ____  ____          ___      ___  ____  _       ___   __ __    ___  ____  \n"
printf "|  |  ||    \ |    / ___/|  |__|  | /    ||    \        |   \    /  _]|    \| |     /   \ |  |  |  /  _]|    \ \n"
printf "|  |  ||  _  | |  (   \_ |  |  |  ||  o  ||  o  )       |    \  /  [_ |  o  ) |    |     ||  |  | /  [_ |  D  )\n"
printf "|  |  ||  |  | |  |\__  ||  |  |  ||     ||   _/        |  D  ||    _]|   _/| |___ |  O  ||  ~  ||    _]|    / \n"
printf "|  :  ||  |  | |  |/  \ ||  |  |  ||  _  ||  |          |     ||   [_ |  |  |     ||     ||___, ||   [_ |    \ \n"
printf "|     ||  |  | |  |\    | \      / |  |  ||  |          |     ||     ||  |  |     ||     ||     ||     ||  .  \\n"
printf " \__,_||__|__||____|\___|  \_/\_/  |__|__||__|          |_____||_____||__|  |_____| \___/ |____/ |_____||__|\_|  V2 Periphery Local\n\n\n"
                                                                                                                       
printf "\n___________________________________________________________________________________________\n\n"

printf "Deploying Uniswap V2 Periphery contracts to local. Remember to start Anvil.\n\n"

printf "Your private key is: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80\n"
printf "Your address is: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266\n"

printf "\n___________________________________________________________________________________________\n"

printf "\nNOTES\n\n"
printf "\n"

printf "\n___________________________________________________________________________________________\n"

rm contract_info.txt

echo "UNISWAP V2 PERIHPERY" >> contract_info.txt

echo "_________________________" >> contract_info.txt

echo "UniswapV2Router02.sol" >> contract_info.txt

forge create --rpc-url 127.0.0.1:8545 --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 src/UniswapV2Router02.sol:UniswapV2Router02 | grep "Deployed to:" >> contract_info.txt

echo "UniswapV2Migrator.sol" >> contract_info.txt

forge create --rpc-url 127.0.0.1:8545 --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 src/UniswapV2Migrator.sol:UniswapV2Migrator | grep "Deployed to:" >> contract_info.txt

echo ""

printf "Uniswap V2 Core contracts deployed to local blockchain. View the addresses in: contract_info.txt\n\n"

printf "Remember to deploy Uniswap V2 Periphery contracts from the uniswapv2periphery repo. Run testDeploy.sh in that repo.\n\n\n"