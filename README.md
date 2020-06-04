# SimpleTwitchPlays
A very simple python script allowing anyone to easily make a TwitchPlays setup

### Instructions
1) Download and extract the SimpleTwitchPlays folder
2) Ensure you have Python 3+ installed on your computer
3) Open MouseAndKeyboardControl.py and set any toggles (inputToggles and keyboardToggles) to False to disable them
4) Open _Twitch_Channel_Details.py and set the values according to the commented instructions within
5) Run _PROGRAM.py
6) In your channel's Twitch chat, use the keywords to trigger input (only the first command detected is run)

### Keywords
- "move_mouse 100 200" (replace 100 and 200 with whatever X and Y value to move relative to current position)
- "click"
- "double_click"
- "drag 100 200" (replace 100 and 200 with whatever X and Y value to move relative to current position while dragging)
- "space"
- "up"
- "down"
- "left"
- "right"
- "w"
- "a"
- "s"
- "d"
- "f"
- "g"
- "enter"

### Caveats
1) There are a number of games which isolate mouse control at the OS level and therefore this script will not be able to override them. Keyboard control seems to work in every game I've tested, but I haven't tested all of them. An interesting thing to note is that some games, for example Stardew Valley, restrict click and double_click but not drag... so you can simulate a click in that game by dragging a single pixel and you can simulate a double click by dragging a single pixel twice with a short delay in between.
2) The current setup of the script is to detect the keyword and pass on the command. If you want to restrict who can use the commands, or use "!w" instead of "w" as the command phrase, or detect if the ONLY thing said is a command so that it can't pick up a command in the middle of a string, you'll have to add that functionality yourself for now. I might add in simple overrides for that sort of thing in the future.
