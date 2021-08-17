# Bombparty bot (WIP)
Ruin your friend's day!

This bot only works for the jklm.fun version of bomb party

# How to use
Asuming many things (1080p monitor, regular zoom level, opera browser (yes I use opera), etc.), this bot should work straight out of the box. 

If you wish to only use the longest word the bot finds, go inside the file bombparty-bot.py and edit line 14 to be True

When its your turn simply press "F8" and the bot will do its thing

# Some extra steps if it does not work
1. Not everyone has a 1080p monitor so you may need to direct the bot at the correct spot to select the text. Simply replace line 27 with the position of the letters, use the top left of your screen as 0,0.

I have provided a compiled AHK script to help you find the correct X and Y positions.

To use XY.exe simply run it and move your mouse over the middle of the letters like so:

![89233905168979260476](https://user-images.githubusercontent.com/68296986/129646899-4f28573f-f5c2-42e8-9134-e78da5f72604.png)

Press "F6" and a small window should show up with the correct X and Y positions

To close the program once you are done simply press the "backtick" key which looks like ``` ` ``` It should be to the left of your ```1``` key

2. Make sure that the wordlist.txt is in the same folder as the bombparty-bot.py file
