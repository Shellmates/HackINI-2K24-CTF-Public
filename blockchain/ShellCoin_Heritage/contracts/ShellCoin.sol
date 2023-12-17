// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {ERC20} from "./ERC20.sol";

contract ShellCoin is ERC20 {


    address public willExecutor;
    uint public grandpaPassingTime;
    bool public executorSet;
    uint256 INITIAL_SUPPLY;

    constructor() ERC20('shellCoin', 'SHC') {
        grandpaPassingTime = block.timestamp;
        INITIAL_SUPPLY = 133713371333337;
    }

    function hireExecutor() external {
        require(willExecutor == address(0));
        require(!executorSet);
        _mint(msg.sender, INITIAL_SUPPLY);
        willExecutor = msg.sender;
        executorSet = true;
    }

    function transfer(address _to, uint256 _amount) override public onlyExecutor itsTherightTime returns (bool) {
        return super.transfer(_to, _amount);
    }


    function _checkExecutor() internal view {
        require(willExecutor == msg.sender, "You're not the will executor you thief !");
    }


    function _checkTime() internal view {
        require(block.timestamp > grandpaPassingTime + 30 * 365 days, "It's not the right time yet grandson.");
    }




    modifier onlyExecutor() {
        _checkExecutor();
        _;
    }

    modifier itsTherightTime() {
        _checkTime();
        _;
    }
}
