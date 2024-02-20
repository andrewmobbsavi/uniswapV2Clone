// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    uint8 private decimalPlaces;

    constructor(string memory _tokenName, 
                string memory _tokenCode, 
                uint8 _decimalPlaces) ERC20 (_tokenName, _tokenCode) {
        decimalPlaces = _decimalPlaces;

        _mint(msg.sender, 1.0 * 1000000000000000000 ^ decimals());
    }

    function mint(address recipient) public {
        _mint(recipient, 1.0 * 1000000000000000000 ^ decimals());
    }

    function decimals() public view virtual override returns (uint8) {
        return decimalPlaces;
    }
}
