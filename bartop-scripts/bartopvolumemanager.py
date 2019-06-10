#!/usr/bin/env python

import struct
import os

#os.system("amixer -M sget PCM")

infile_path = "/dev/input/js0"
file = open(infile_path, "rb")
eventFormat = "LhBB"
EVENT_SIZE = struct.calcsize(eventFormat)
event = file.read(EVENT_SIZE)
hotkeyValue = 0
hotkeyButtonId = 0
volPlusButtonId = 6
volMinusButtonId = 1

while event:
    print(struct.unpack(eventFormat, event))
    (tv_msec, value, type, id) = struct.unpack(eventFormat, event)
    
    if id == hotkeyButtonId:
        hotkeyValue = value
    elif id == volPlusButtonId and value == 1 and hotkeyValue == 1:
        os.system("amixer -M sset PCM 5%+")
    elif id == volMinusButtonId and value == 1 and hotkeyValue == 1:
        os.system("amixer -M sset PCM 5%-")

    event = file.read(EVENT_SIZE)