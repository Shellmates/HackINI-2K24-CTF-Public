// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {EtherVault} from "./EtherVault.sol";

contract Setup {
    EtherVault public immutable TARGET;
   
    constructor() payable {
        TARGET = new EtherVault{value: 99 ether}(bytes16(keccak256(abi.encode(blockhash(block.number), block.timestamp))));
    }

    function isSolved() public view returns (bool) {
        return TARGET.getBalance() == 0;
    }

}