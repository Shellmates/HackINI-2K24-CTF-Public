// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import {SpaceShip} from "./SpaceShip.sol";

contract Setup {
    SpaceShip public immutable TARGET;

    constructor() payable {
        TARGET = new SpaceShip();
    }


    function isSolved() public view returns (bool) {
        return TARGET.getDistanceTraveled() == 0;
    }
}