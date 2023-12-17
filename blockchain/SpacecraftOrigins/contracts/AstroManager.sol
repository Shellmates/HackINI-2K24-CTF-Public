// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract AstroManager {
    bool public resourcesAllocated;

    constructor() {
        resourcesAllocated = false;
    }

    function allocateResources() public {
        require(tx.origin != msg.sender, "Only spacecrafts can allocate resources.");
        resourcesAllocated = true;

    }
}

