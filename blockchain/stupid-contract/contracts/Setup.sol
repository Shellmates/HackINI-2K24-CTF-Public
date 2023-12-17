pragma solidity ^0.8.13;


contract Setup {    
    address public TARGET;
    constructor() payable {
        bytes memory code =
            hex"606080600b6000396000f360033611600c575b600080fd5b63ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663c286503781146054576364d98f6e141560075760005460005260206000f35b3415600757600160005500";
        assembly {
            sstore(TARGET.slot, create(0, add(code, 0x20), mload(code)))
        }
    }

    function isSolved() public view returns (bool) {
        return  Setup(TARGET).isSolved();
    }
}