import ops
import sys
import convert_to_midi
import os


if __name__ == "__main__":
	ops.test(sys.argv[1])
	a = convert_to_midi.transcribe(sys.argv[1])
	command = "open /Applications/MuseScore\ 3.app " + a
	os.system(command)