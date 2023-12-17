// SPDX-License-Identifier: No-License
pragma solidity ^0.8.22;

import {Ownable} from "./Ownable.sol";
import {ReentrancyGuard} from "./ReentrancyGuard.sol";

contract OnChainParty is Ownable, ReentrancyGuard {

    uint256 lockOwnerTransferTime = block.timestamp + 7 days * 52;
    address[] members;
    mapping(address => bool) isMember;

    bytes8 private secret;
    event Joined(address _newMember);

    constructor() payable Ownable(msg.sender){
        require(msg.value >= 3 ether);
        secret = bytes8(keccak256(abi.encode(msg.sender, bytes16(keccak256(abi.encode(uint256(blockhash(block.timestamp))))))));
        members.push(msg.sender);
        isMember[msg.sender] = true;
    }

    modifier onlyMember {
        require(isMember[msg.sender], "You need to join the club first!");
        _;
    }

    receive() external payable {
        require(msg.value >= 0.5 ether, "Common, we're rich, give more!");
        members.push(msg.sender);
        isMember[msg.sender] = true;

        emit Joined(msg.sender);
    }

    function leaveParty() external onlyMember nonReentrant {
        for (uint i =0; i < members.length; i++) {
            if (msg.sender == members[i]) {
                (bool success, ) = payable(msg.sender).call{value: 0.25 ether}("");
                require(success);
                isMember[msg.sender] = false;
            }
        }
    }

    function takeOwnership() external onlyMember {
        require(block.timestamp > lockOwnerTransferTime);
        _transferOwnership(msg.sender);
    }

    function withdraw() external onlyOwner {
        (bool success, ) = payable(owner).call{value: address(this).balance}("");
        require(success);
    }

    // is it your lucky day?
    function unlockVault(bytes16 _key) external onlyMember {
        require(uint32(bytes4(_key)) == uint32(randomize(secret)), "Hold on!");
        require(bytes8(uint64(uint128((_key << 32) >> 64))) == bytes8(uint64(uint160(msg.sender))), "Wait a minute!!");
        require(bytes4(uint32(uint128(_key))) == bytes4(abi.encodeWithSignature("unlockVault(bytes16)", bytes16("LET ME IIIIIIN"))), "Too close");

        (bool success, ) = payable(msg.sender).call{value: address(this).balance}("");
        require(success, "Something wrong happened");
    }

    function randomize(bytes8 _secret) private view returns(bytes4) {
        return bytes4(keccak256(abi.encode(_secret, block.prevrandao, keccak256(abi.encode(block.timestamp)))));
    }
}