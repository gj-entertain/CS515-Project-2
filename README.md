# Text Adventure Game

## Team Members

- [Jia Gao] - Stevens Login: [jgao32@stevens.edu]

## Repository URL

[https://github.com/your-repo-url]

## Time Spent on Project

Approximately 30 hours

## Code Testing

My code was tested iteratively during development. I utilized manual testing by running the game and interacting with it to ensure each function behaved as expected. This process helped identify and fix bugs in real-time.

## Known Bugs and Issues

- Some minor synchronization issues with item states when rapidly executing commands.
- Occasionally, room descriptions may not update instantly after certain actions.

## Resolved Challenges

One challenging aspect was designing the `drop` and `get` functions to accurately update the item count in the game map. For instance, when a player picks up a rose, the item count in that room's map should decrease by one. Conversely, dropping an item should increase the count. This required careful manipulation of the game's state and item inventory to ensure consistency across the game.

## Implemented Extensions

1. **Help Command (`help`):** Provides players with a list of available commands and their usage, enhancing the game's usability.

2. **Drop Command (`drop`):** Allows players to remove items from their inventory and leave them in the current room, affecting the room's state and item availability for future interactions.

3. **Winning and Losing Conditions:** 
   - The game features a health point (HP) system. Each movement (using `go`) reduces HP by 1.
   - Players start with a maximum HP of 10.
   - The objective is to find a specific item, termed as "magic wind". 
   - Winning Condition: The player wins if they find the "magic wind" before their HP runs out.
   - Losing Condition: If the player's HP reaches 0 before finding the "magic wind", they lose the game.

## How to Play

- Start the game by executing the script with a specified map file.
- Use commands like `go`, `get`, `drop`, `look`, `inventory`, `help`, and `quit` to interact with the game world.
- Navigate through different rooms, pick up items, and find the "magic wind" before your HP runs out.
