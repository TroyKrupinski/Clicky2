# Clicky2
Clicky is a local web based SWF player.
Clicky was created by Troy Krupinski - 2018 October @ UT Aus
Since JavaScript cannot access local files, you have to add your files manually

*-------HOW TO SETUP CLICKY-------*
1. Put all clicky files in the folder you wish to play files from.
2. Open "GetFiles.py" and follow the directions.
3. Open "filenames.txt" and copy the entire document.
4. EDIT "clicky2.html" with any text editor.
5. Go to line 80 and paste what was in "filenames.txt" inside -->> ar[*here*]
6. To get file names from a folder in the same directory, open "GetFilesF.py" and follow the instructions
7. Open "filenames.txt" and copy the entire document again.
8. Go to line 80 and paste what was in "filenames.txt" inside -->> ar2[*here*]
9. Repeat steps 6 through 8 for ar3[] and ar4[] if needed


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
