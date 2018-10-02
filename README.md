# Clicky2
Clicky is a local web based SWF player.
Clicky was created by Troy Krupinski - 2018 October @ UT Aus
Since JavaScript cannot access local files, I use python to add them.

*-------HOW TO SETUP CLICKY-------*
1. Put all clicky files in the folder you wish to play files from.
2. If you want to be able to play multiple (up to 3) different directories, open "Click(folder setup).py", if not open "click.py".
3. Open "Clicky2.html"
4 Done!

*-------HOW TO USE CLICKY-------*
How to use the multiple buttons:
The buttons clicky, clicky2, clicky3 and clicky 4 correspond to the arrays ar[], ar2[], ar3[] and ar4[] respectfully.
Once the buttons are clicked, a random file will be selected from the array (your folder).
The Back and Forward buttons are to scrub through the files you've already played (which is stored into a cache).
The Repeat button makes it so that no files repeat in every singular array. You can toggle this button - the default setting is  set to repeating.
The Clear button clears both the Repeat cache and the regular cache.
The Replay button replays the current SWF.
The Reset button resets the player back to the starting image.

REF: 
http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0
http://www.macromedia.com/go/getflashplayer
