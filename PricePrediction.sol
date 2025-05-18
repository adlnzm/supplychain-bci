// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PricePrediction {
    event PredictionLogged(address predictor, uint timestamp, string coin, uint256 predictedPrice);

    struct Prediction {
        address predictor;
        string coin;
        uint256 predictedPrice;
        uint timestamp;
    }

    Prediction[] public predictions;

    function storePrediction(string memory coin, uint256 predictedPrice) public {
        predictions.push(Prediction(msg.sender, coin, predictedPrice, block.timestamp));
        emit PredictionLogged(msg.sender, block.timestamp, coin, predictedPrice);
    }

    function getTotalPredictions() public view returns (uint) {
        return predictions.length;
    }
}
