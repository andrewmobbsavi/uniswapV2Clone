from dotenv import load_dotenv
import os

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
FEE_RECIPIENT = os.getenv("FEE_RECIPIENT")
RPC_ENDPOINT = os.getenv("RPC_ENDPOINT")

BASE_TOKEN_NAME = "Wrapped Eth"
BASE_TOKEN_CODE = "WETH"

BASE_DECIMALS = 18

SEPARATOR = "----------------------------------------------------------------------------------------------------"

