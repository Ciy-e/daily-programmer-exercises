
/*
* Dice roller, rolls n dices of s sides.
* Expected argument 2d20 -> a randomly generated int between 2 and 40.
*/

import Foundation

func diceRoller(diceRolled: String) -> Int {
    let numDiceAndDiceSize = diceRolled.components(separatedBy: "d")
    let numDice = Int(numDiceAndDiceSize[0])
    let diceSize = Int(numDiceAndDiceSize[1])

    var total = 0
    if let numDice = numDice {
        for _ in 0..<numDice {
            if let diceSize = diceSize {
                total += Int.random(in: 1 ..< diceSize+1)
            }
        }

    }
    return total
}


print(diceRoller(diceRolled: "2d20"))
print(diceRoller(diceRolled: "1d10"))
print(diceRoller(diceRolled: "6d7"))
