// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {ShellCoin} from "./ShellCoin.sol";

contract Setup {
    ShellCoin public immutable TARGET;
   
    constructor() payable {
        TARGET = new ShellCoin();
    }


    function isSolved() public view returns (bool) { 
        // Just a random address to match the narrative
        return TARGET.balanceOf(0xAf57Ac75f227363bB9D4d61872d81DE340BCc395) == 133713371333337;
    }

}