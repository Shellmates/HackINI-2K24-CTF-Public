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