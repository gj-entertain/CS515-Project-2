# Text Adventure Game

## Team Members

- [Jia Gao] - Stevens Login: [jgao32@stevens.edu]

## Repository URL

[https://github.com/gj-entertain/CS515-Project-2]

## Time Spent on Project

Approximately 30 hours

## Code Testing

My code was tested iteratively during development. I utilized manual testing by running the game and interacting with it to ensure each function behaved as expected. This process helped identify and fix bugs in real-time.
I write a test.py to test all the cases:
```python
import subprocess

def run_test(map_file, input_file, expected_output_file):
    # Run adventure.py with the map file
    process = subprocess.Popen(['python3', '../CS515Project2/adventure.py', map_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Read input commands from the input file
    with open(input_file, 'r') as file:
        input_commands = file.read()
    
    # Send input commands to the adventure.py process
    output, errors = process.communicate(input_commands)

    # Split the output into lines
    output_lines = output.strip().split('\n')

    # Read and split the expected output into lines
    with open(expected_output_file, 'r') as file:
        expected_output_lines = file.read().strip().split('\n')

    # Compare the output and expected output line by line
    passed = True
    for i, (actual_line, expected_line) in enumerate(zip(output_lines, expected_output_lines)):
        if actual_line != expected_line:
            print(f"Test with {input_file} failed at line {i + 1}.")
            print(f"Expected: '{expected_line}'")
            print(f"Got: '{actual_line}'")
            passed = False
            break  # Stop at first failure

    # If all lines match
    if passed:
        print(f"Test with {input_file} passed.")

# List of test cases
test_cases = [
    ("test.map", "test.01.in", "test.01.out"),
    # Add more test cases as needed
]

# Run all test cases
for map_file, input_file, expected_output_file in test_cases:
    run_test(map_file, input_file, expected_output_file)

```

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
   - Players start with a maximum HP of 1000.
   - The objective is to find a specific item, termed as "magic wind". 
   - Winning Condition: The player wins if they find the "magic wind" before their HP runs out.
   - Losing Condition: If the player's HP reaches 0 before finding the "magic wind", they lose the game.

## How to Play

- Start the game by executing the script with a specified map file.
- Use commands like `go`, `get`, `drop`, `look`, `inventory`, `help`, and `quit` to interact with the game world.
- Navigate through different rooms, pick up items, and find the "magic wind" before your HP runs out.
