## TLDR:
This is a project I made to automate farming Memory Match boards efficiently in BSS using Python. Currently, the code was designed with my iMac's specifications in mind, but it could be adapted to work on other Mac devices.
## Motivation:
It was initially made when a rare reward was added to be given for the players with highest number of matches daily. Several macros were already being used in BSS for varying goals, but none had the ability to automate Memory Match games. Additionally, macros for Mac devices had been largely lacking compared to on devices running Windows. Due to these reasons, I saw an opportunity to become the only player on a game with 100k+ players peak players with the ability to farm Memory Matches to hit the top rankings on the leaderboards consistently for the rewards.
## What can the macro do?
* Navigate to each Memory Match board type.
* Perfectly play out each game to maximize the number of matches.
* Rejoin in the case of disconnecting and seamlessly continue functionality consistently.
* Detect nighttime by checking the color of the sky in order to play the Night MM board, although the navigation to the board is inconsistent due to the moon jumps.
* Log each game board after playing, as well as how logging how each board was played. This features proved helpful in debugging several times.
* Match all rewards gained to a RGB database of all known items so far. Any unknown/new items are stored by their RGB values rather than their name.
* Provide a post-session summary of games played, broken down by board type, and a list of all items obtained during the session.
