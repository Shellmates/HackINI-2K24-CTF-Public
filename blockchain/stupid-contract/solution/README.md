# Stupid Contract

## Write-up

This challenge requires knowledge about EVM-the environment of smart contracts execution.<br>
To solve the contract, we need to return `true` from the `target` when `isSolved` is called:
```solidity
function isSolved() public view returns (bool) {
    return  Setup(TARGET).isSolved();
}
```
This time, we don't have the Solidity code, instead we have the bytecode:
```hex
606080600b6000396000f360033611600c575b600080fd5b63ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663c286503781146054576364d98f6e141560075760005460005260206000f35b3415600757600160005500
```
Once a smart contract code is compiled to bytecode, it contains two parts:
- **creation bytecode**: it initializes the contract's state (executes `constructor` logic) and **returns the runtime bytecode**
- **runtime bytecode**: The actual contract's logic bytecode that is stored within the contract account in the `code` field.<br>
So, first thing to do is to separate the given bytecode to `creation` and `runtime`, we know that the opcode for `RETURN` is `f3`, and because the `creation` bytecode **returns** the `runtime` bytecode, we need to find the first occurance of `f3`, anything behind it is the `runtime` bytecode:
- **creation bytecode**: `606080600b6000396000f3`
- **runtime bytecode**: `60033611600c575b600080fd5b63ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663c286503781146054576364d98f6e141560075760005460005260206000f35b3415600757600160005500`

From here we need to translate the hex representation to `opcodes` representation to better understand the contract's logic. Of course, we won't do that manually, we can use [EVM playground](https://www.evm.codes/playground) to do that. We're interested in the `runtime` bytecode as the creation bytecode is just returning the `runtime`, no initialization is made.<br>
**runtime opcodes**:
```asm
[00]	PUSH1	03
[02]	CALLDATASIZE	
[03]	GT	
[04]	PUSH1	0c
[06]	JUMPI	
[07]	JUMPDEST	
[08]	PUSH1	00
[0a]	DUP1	
[0b]	REVERT	
[0c]	JUMPDEST	
[0d]	PUSH4	ffffffff
[12]	PUSH29	0100000000000000000000000000000000000000000000000000000000
[30]	PUSH1	00
[32]	CALLDATALOAD	
[33]	DIV	
[34]	AND	
[35]	PUSH4	c2865037
[3a]	DUP2	
[3b]	EQ	
[3c]	PUSH1	54
[3e]	JUMPI	
[3f]	PUSH4	64d98f6e
[44]	EQ	
[45]	ISZERO	
[46]	PUSH1	07
[48]	JUMPI	
[49]	PUSH1	00
[4b]	SLOAD	
[4c]	PUSH1	00
[4e]	MSTORE	
[4f]	PUSH1	20
[51]	PUSH1	00
[53]	RETURN	
[54]	JUMPDEST	
[55]	CALLVALUE	
[56]	ISZERO	
[57]	PUSH1	07
[59]	JUMPI	
[5a]	PUSH1	01
[5c]	PUSH1	00
[5e]	SSTORE	
[5f]	
STOP
```
We won't go through opcode one by one. To summarize: 
- The `calldata` sent to the contract must be greater than 3 bytes.
- There're two function selectors accepted: `0xc2865037`, `0x64d98f6e` which correspond to [dumpBump()](https://www.4byte.directory/signatures/?bytes4_signature=0xc2865037) and [0x64d98f6e](https://www.4byte.directory/signatures/?bytes4_signature=0x64d98f6e) functions signatures accordingly.
- The function `isSolved` returns the value stored at `slot 0`
- The function `dumpBump()` sets the value of the first slot to `1`, and when it is called, 1 ether must be sent along.

The `Setup` contract's `isSolved` function returns the value returned by `isSolved` of `target`. So, to return `1`(which is casted to `true`), we need to set the value of the first slot to 1. To do that, we need to call first the `dumpBump()` function sending 1 ether along.

#### Solve script
```bash
TARGET=$(cast call "$SETUP" "TARGET()(address)" --rpc-url "$RPC") 
cast send "$TARGET" "dumpBump()" --value 1ether --rpc-url "$RPC" --private-key "$PrivateKey"

isSolved=$(cast call "$SETUP" "isSolved()(bool)" --rpc-url "$RPC")
echo "$isSolved"
# true
```
## Flag

`shellmates{y0u_S33_evm_0PC0d3s_4r3_L1KE_4S$EmBly}`
