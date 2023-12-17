    // SPDX-License-Identifier: UNLICENSED
    pragma solidity ^0.7.0;

    contract SpaceShip {
        uint32 public distanceFromTheBlackHole;
        uint32 private distanceTraveled;

        constructor() {
            distanceTraveled = 1337;
            distanceFromTheBlackHole = 4294967295;
        }

        function galacticBoost(uint32 advanceWithDistance) public {
            // Avoid the space ship from falling into the black hole
            require(distanceTraveled + advanceWithDistance < distanceFromTheBlackHole);
            distanceTraveled += advanceWithDistance;
        }

        
        function getDistanceTraveled() public view returns (uint256) {
            return distanceTraveled;
        }

    }

