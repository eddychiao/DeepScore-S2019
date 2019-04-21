# DeepScore-S2019
Compilation of what I worked on for S19

ops.py 
	- contains all the functions that I made in order to generate chord notes
	- I made a ton of smaller functions so that each operation would be easier to trace
main.py
	- runs the important stuff, imports ops.py and other files
convert_to_midi.py
	- contains code in writing .txt content into MIDI input, running it with MuseScore will automatically convert it


1.txt, 2.txt, 3.txt, etc.
	- sample chord progressions generated from the chord generation RNN

To Run:

	cd to directory that this is in

	python3 main.py 1.txt
	OR
	python3 main.py 2.txt

	...
	...
	etc.

	- This will automatically launch MuseScore and open the sheet music that was transcribed from the .txt input
	- To play the music, just press SPACE
