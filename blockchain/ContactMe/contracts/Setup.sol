// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;


contract Setup {
    bool public solved;

    constructor() payable {
        solved = false;
    }

    function makeACall(uint8 _hour) external {
        require(_hour == 7,"I'm not availabe at this hour, call me at 7.");
            solved = true;
    }

    function isSolved() public view returns (bool) {
        return solved == true;
    }

}