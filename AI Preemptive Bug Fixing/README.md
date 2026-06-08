# AI: Preemptive Bug Fixing

## Objective
Use AI as a Senior C Developer to review vulnerable C code, identify logical and memory safety flaws, and generate a corrected solution.

## Files
- initial_code.c : Original vulnerable implementation
- corrected_code.c : Refactored and corrected implementation

## AI Tool Used
ChatGPT

## Issues Found
1. Missing NULL check after malloc()
2. Incorrect list traversal
3. Failure to link the new node
4. Potential memory leak

## Fixes Applied
- Added malloc() error handling
- Traversed to the last node correctly
- Linked the new node using current->next
- Properly initialized the new node

## Outcome
The corrected function safely appends a node to the end of a singly linked list while handling allocation failures correctly.
