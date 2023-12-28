# Battleship Game

## Project Overview

This project involves the implementation of a Battleship game against the computer. The game is played on a 10x10 grid, where columns are represented by numbers, and rows are represented by letters (e.g., A1, B2, C3). The objective is to strategically position ships on the board and take turns guessing the opponent's ship locations to sink them.

## Game Components

### Game Board

The game board is a 10x10 grid represented by the combination of letters (rows) and numbers (columns). Users and the computer will place their ships on this board.

### Ships

The game includes the following ships:

1. **Aircraft Carrier (Portaviones):** Occupies five consecutive cells (e.g., A1, B1, C1, D1, E1).
2. **Battleship (Acorazado):** Occupies four consecutive cells (e.g., F4, F5, F6).
3. **Big Battleship (Crucero de Batalla):** Occupies three consecutive cells (e.g., C5, D5, E5).
4. **Submarine (Submarino):** Occupies two consecutive cells (e.g., C4, D4).
5. **Boat (Lancha):** Occupies a single cell (e.g., G3).

### Ship Placement

Users have the opportunity to strategically place their ships on the board by specifying the cells of each ship (A1,B1,C1, D1,E1). Computer-generated boards, stored in TXT files, provide the initial ship positions for the computer.

### Gameplay

1. **User Turn:**
   - Users take turns selecting a cell on the opponent's board to hit.
   - The result of the hit (hit or miss) is displayed.

2. **Computer Turn:**
   - The computer randomly selects a cell on the user's board to hit.
   - The result of the hit is displayed.

3. **Winning Condition:**
   - The game continues until one player sinks all the opponent's ships.

## Project Files

The project includes the following files and directories:

1. **main.py:** Python script containing the main logic of the Battleship game.
2. **Tablero1.txt, Tablero2.txt, Tablero3.txt, Tablero4.txt:** TXT files storing computer-generated ship positions for different game scenarios.
3. **README.md:** Project documentation providing an overview of the game, its components, and instructions for playing.

## How to Play

1. Install pygame with pip ```pip3 install pygame```
2. Run the `main.py` script to initiate the Battleship game.
3. Follow on-screen prompts to strategically place your ships.
4. Take turns with the computer to hit cells on the opponent's board.
5. Continue playing until one player sinks all the opponent's ships.

Enjoy the strategic thrill of the classic Battleship game against the computer!
