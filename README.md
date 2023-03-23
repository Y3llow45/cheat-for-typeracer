Cheat for https://play.typeracer.com/
 
## How to use in practice mode
Open https://play.typeracer.com/, click on practice, run practice.py and press "v" when you want to start cheating (i mean typing).

## Notes

If you want to increase typing speed decrease the interval
0.09 ~ 100wpm

Don't go over 100wpm cuz there is anti-cheat system.

## What to do if it doesn't work

Use firefox and scroll down a little bit.

OR

This script takes a screenshot and type all the text it extracted. If it doesn't work for you need to change line 10 with the right width and height values. It is x and y for two dots which are the edges of the screenshot. Import pyautogui and run "pyautogui.position()" in while True: loop to get cordinates of you mouse. Start practise and move your mouse to the top left corner of the text and save the cordinates. Do the same but for the bottom right corner(go as down as you can because you can get longer text and the script may cut it). Change line 10 with the new values you got. Run the script and test it.
