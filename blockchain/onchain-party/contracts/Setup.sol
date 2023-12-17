pragma solidity ^0.8.22;

import {OnChainParty} from "./OnChainParty.sol";

contract Setup {
    OnChainParty public immutable TARGET;
    constructor() payable {
        TARGET = new OnChainParty{value: msg.value}();
    }

    function isSolved() public view returns (bool) {
        return  address(TARGET).balance == 0;
    }
}
