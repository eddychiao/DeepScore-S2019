"""
Edward Chiao
VIP - Robotic Musicianship
"""

"""
Directory for MIDI conversion, unique code for each node
"""
note_to_num = {
    "B#": 60,
    "C": 60,
    "C#": 61,
    "Db": 61,
    "D": 62,
    "D#": 63,
    "Eb": 63,
    "E": 64,
    "F": 65,
    "F#": 66,
    "Gb": 66,
    "G": 67,
    "G#": 68,
    "Ab": 68,
    "A": 69,
    "A#": 70,
    "Bb": 70,
    "B": 71
}

num_to_note = {
    60: "C",
    61: "C#",
    62: "D",
    63: "D#",
    64: "E",
    65: "F",
    66: "F#",
    67: "G",
    68: "G#",
    69: "A",
    70: "A#",
    71: "B",
    72: "C",
    73: "C#",
    74: "D",
    75: "D#",
    76: "E",
    77: "F",
    78: "F#",
    79: "G",
    80: "G#",
    81: "A",
    82: "A#",
    83: "B",
    84: "C",
    85: "C#",
    86: "D"
}

major_rules = {
    "maj": [0, 4, 7, 12],
    "maj6": [0, 4, 7, 9],
    "maj7": [0, 4, 7, 11],
    "maj9": [0, 4, 7, 11, 14],
    "6": [0, 4, 7, 9],
    "7": [0, 4, 7, 10],
    "9": [0, 4, 7, 14],
    "sus4": [0, 5, 7, 12]
}

minor_rules = {
    "min": [0, 3, 7, 12],
    "min6": [0, 3, 7, 9],
    "min7": [0, 3, 7, 10],
    "min9": [0, 3, 7, 10, 13]
}

dim_rules = {
    "dim": [0, 3, 6, 9],
    "hdim": [0, 3, 6, 10]
}

aug_rules = {
    "aug": [0, 4, 8, 12]
}

"""
Function that takes in a text file of different chords and returns a list of chords as strings
param: file = string of file passed in

"""
def inList(file):
    if file[-4:].lower() != ".txt":
        raise Exception("File must be .txt")
        return
    try:
        reader = open(file, "r")
    except:
        raise Exception("Filename not found or is invalid")
        return
    allText = reader.read()
    aList = allText.split()
    for item in aList:
        item = item.strip()
    reader.close()
    return aList


"""
Breaks a chords into a tuple and returns it
Format of tuple is as follows:
    (ROOT, add-ons)

Param: aStr = basic chord passed in

* disregards "_END_" and "_START_"
"""
def baseNote(aStr):
    if aStr not in ["_END_", "_START_"]:
        split = aStr.split(":")
        return [split[0], split[1].lower()]


"""
Splits the chord into base note and alternation as tuple
    Format: 
        [(BASE, add), (BASE, add), (BASE, add), ...]
"""
def separate(file):
    aList = inList(file)
    for i in range(len(aList)):
        aList[i] = baseNote(aList[i])
    return aList


"""
Returns:
    True: chord passed in is major
    False otherwise
"""
def isMajor(aStr):
    if aStr[0].isdigit() or "maj" in aStr or "sus" in aStr:
        return True
    return False

"""
Returns:
    True: chord passed in is minor
    False otherwise
"""
def isMinor(aStr):
    return "min" in aStr


"""
Returns:
    True: chord passed in is diminished
    False otherwise
"""
def isDiminished(aStr):
    return "dim" in aStr

"""
Returns:
    True: chord passed in is augmented
    False otherwise
"""
def isAugmented(aStr):
    return "aug" in aStr

"""
Classifies the type of chord passed in
"""
def classifyChord(tup):
    if tup == None:
        return "Null"
    if isMajor(tup[1]):
        return "major"
    elif isMinor(tup[1]):
        return "minor"
    elif isDiminished(tup[1]):
        return "diminished"
    elif isAugmented(tup[1]):
        return "augmented"
    else:
        return "unidentified"

"""
Adds in an index classifying the type of chord passed in
"""
def classify(file):
    a = separate(file)
    aList = []
    for tup in a:
        if tup != None:
            tup.append(classifyChord(tup))
            aList.append(tup)
    return aList

"""
Returns the MIDI # representation of the note
"""
def getMIDINumber(char):
    return note_to_num[char]


"""
Passes in the list element with its identification, then returns the chord notes
    Input: [root note, chord, identification]
    Output: "CHORD: note1  note2  note3 ...."
    * for now, doesn't take into account stuff in parentheses (ex: G#:7(s5, *5))
"""
def chordify(aList):
    base, chord, ident = aList
    aStr = base + chord + ":\t"
    base_num = getMIDINumber(base)
    if ident == "major":
        for i in major_rules[chord]:
            aStr += num_to_note[base_num + i] + "\t"
    elif ident == "minor":
        for i in minor_rules[chord]:
            aStr += num_to_note[base_num + i] + "\t"
    elif ident == "diminished":
        for i in dim_rules[chord]:
            aStr += num_to_note[base_num + i] + "\t"
    elif ident == "augmented":
        for i in aug_rules[chord]:
            aStr += num_to_note[base_num + i] + "\t"
    else:
        raise Exception("Invalid Input")
    return aStr


"""
Runs the script on a file
"""
def test(file):
    newname = file[:-4] + "_to_chords.txt"
    f = open(newname, "w")
    val = classify(file)
    for i in val:
        f.write(chordify(i))
        f.write("\n")
    f.close()




