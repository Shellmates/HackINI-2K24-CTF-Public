pragma solidity ^0.8.22;

contract Ownable {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    function _transferOwnership(address _owner) internal {
        owner = _owner;
    }
}