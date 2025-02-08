# Big Two (Early Version)

## Overview

Big Two is a popular card game played in many East Asian countries. This Python implementation is an early version of the game, featuring:

- 4-player gameplay
- Automated dealing and turns
- Basic validation for single card plays
- Turn-based mechanics with passing support
- Determination of the winner

## Game Rules (Simplified)

- The game uses a standard 52-card deck.
- Cards are ranked from 3 (lowest) to 2 (highest): 3 4 5 6 7 8 9 10 J Q K A 2.
- Suits are ranked from Clubs (lowest) to Spades (highest): C D H S.
- Player with 3C (3 of Clubs) starts the first round.
- Players take turns playing a higher card than the last played card.
- If a player cannot play a valid card, they must pass.
- If all three other players pass, the round resets, and any card can be played.
- The first player to play all their cards wins the game.