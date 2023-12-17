# Welcome To Blockchain

## Write-up

The description of the challenges gives us everything we need to solve the challenge, it highlights that:
- We're using **Ethereum**
- We're not working with mainnet, instead we are using **Sepolia test network**
- There's an interesting tx we need to give it a look: **0xa7d1c8bf96e30371a1049c6332b077eac6877b8b0c6191e362cc1702c5de4c7a**

After we check the transaction in [Sepolia Etherscan](https://sepolia.etherscan.io/tx/0xa7d1c8bf96e30371a1049c6332b077eac6877b8b0c6191e362cc1702c5de4c7a), we find the flag inside the encoded input data

## Flag

`shellmates{W3lcOME_tO_3tH3r3um_h4ve_fun}`
