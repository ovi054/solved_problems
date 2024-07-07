class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = numBottles
        existBottles = numBottles
        while(existBottles>=numExchange):
            output = output + existBottles//numExchange
            existBottles = existBottles//numExchange + existBottles%numExchange
        return output