#!/usr/bin/env python3

from gw_lan import lan
import dso1kb

#Connecting to a DSO.
#dso=dso1kb.Dso("10.10.0.77:3001") 
dso=dso1kb.Dso("127.0.0.1:3001")

dso.getRawData(True, 1)
dso.getRawData(True, 2)

fwave1 = dso.convertWaveform(1,1)
fwave2 = dso.convertWaveform(2,1)

