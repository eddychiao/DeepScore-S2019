from midiutil import MIDIFile
from EasyMIDI import EasyMIDI,Track,Note,Chord,RomanChord
from random import choice
import sys


# RESOURCE
# https://easymidi.readthedocs.io/en/latest/_autosummary/EasyMIDI.Chord.html



# degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
# track    = 0
# channel  = 0
# time     = 0    # In beats
# duration = 1    # In beats
# tempo    = 60   # In BPM
# volume   = 100  # 0-127, as per the MIDI standard

# MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
#                       # automatically)
# MyMIDI.addTempo(track, time, tempo)

# for i, pitch in enumerate(degrees):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

# with open("major-scale.mid", "wb") as output_file:
#     MyMIDI.writeFile(output_file)

########################################################################


# easyMIDI = EasyMIDI()
# track1 = Track("acoustic grand piano")  # oops

# c = Note('C', octave = 4, duration = 1/4, volume = 100)
# e = Note('Eb', 4)
# g = Note('G', 4)

# chord = Chord([Note('C', octave = 4, duration = 1/4, volume = 100),Note('Eb', 4),Note('G', 4)])  # a chord of notes C, E and G
# track1.addNote(chord)
# track1.addNotes([c, e, g, chord])
# track1.addNotes([c, e, g, chord])

# # roman numeral chord, first inversion (defaults to key of C)
# track1.addNotes(RomanChord('I*', octave = 4, duration = 1))

# easyMIDI.addTrack(track1)
# easyMIDI.writeMIDI("output.mid")


########################################################################

def transcribe(file):
	easyMIDI = EasyMIDI()
	track1 = Track("acoustic grand piano")

	num = file[:-4]
	file = file[:-4] + "_to_chords.txt"
	f = open(file, "r")
	lines = f.readlines() #formatted like 'Cdim:\tC\tD#\tF#\tA\t\n'
	
	for chord in lines:
		aList = []
		appeared = []
		chord = chord.split("\t")[1:-1]
		for note in chord:
			if note not in appeared:
				temp = Note(note, 4, 1/4, 100)
				appeared.append(note)
			else:
				temp = Note(note, 5, 1/4, 100)
			aList.append(temp)
		chord = Chord(aList)
		track1.addNote(chord)

	easyMIDI.addTrack(track1)
	easyMIDI.writeMIDI("output" + "_" + num + ".mid")
	file = "output" + "_" + num + ".mid"

	f.close()
	return file
















