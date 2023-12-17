# Contact Me Writeup

## TL;DR
This is a warmup challenge intended to teach the player how to interact with smart contracts and how to call solidity functions.

## Interacting with the Blockchain
There are a lot of tools that you can use to interact with smart contracts, but we chose Foundry since it's simple to use and doesn't require any prior knowledge of other programming languages.
## Installing Foundry Tools
Foundry-rs is a smart contract development toolchain which we'll be using to interact with smart contracts in these series of challenges. You can install Foundry using the following commands:

#### 1 : 
```bash
curl -L https://foundry.paradigm.xyz | bash
```
#### 2:
```
foundryup
```
Now you have foundry tools installed.

## Solving the challenge
- Make a secure ticket and save it.
- Launch your instance.
- You'll get your connection infos.

Now, if we check the value of the `solved` attribute we'll see that it's 0 (false):
```
$cast call --rpc-url $YOUR_RPC_URL_GOES_HERE $SETUP_CONTRACT_ADDRESS "solved()"
0x0000000000000000000000000000000000000000000000000000000000000000
```
What we need to do, is to call the function makeACall with the argument 7 so we can set the `solved` value to true:
```
$cast send --rpc-url $YOUR_RPC_URL_GOES_HERE $SETUP_CONTRACT_ADDRESS "makeACall(uint8)" 7 --private-key $YOUR_PRIVATE_KEY
```
If we check the `solved` variable again we'll find that it's now true:
```
$cast call --rpc-url $YOUR_RPC_URL_GOES_HERE $SETUP_CONTRACT_ADDRESS "solved()"
0x0000000000000000000000000000000000000000000000000000000000000001
```
Now you can get the flag.

## Flag

`shellmates{U_c0ntRACteD_m3_$ucce$sFullY_0x007}`
