import constants

'''
Here we define the tokens and pass them to the main application

Returns an array of dictionaries containing token information
'''
def defineTokens():
    tokenArray = [{
            "tokenName": constants.BASE_TOKEN_NAME,
            "tokenCode": constants.BASE_TOKEN_CODE,
            "tokenDecimals": constants.BASE_DECIMALS
          },{
            "tokenName": "Abalone",
            "tokenCode": "ABLN",
            "tokenDecimals": constants.BASE_DECIMALS
          },{
            "tokenName": "Bream",
            "tokenCode": "BREM",
            "tokenDecimals": constants.BASE_DECIMALS
          },{
            "tokenName": "Carp",
            "tokenCode": "CARP",
            "tokenDecimals": constants.BASE_DECIMALS
          },{
            "tokenName": "Dolphin",
            "tokenCode": "DLPH",
            "tokenDecimals": constants.BASE_DECIMALS
          }
    ]

    return tokenArray