#data: window 256x240px, 17x16 tiles (fill screen + 1 row and column)
import json
import math
import render
#setup enviroment
RUN = True
File = open('game/data.json')
Data = json.loads(File.read())
Tiles = Data["tiles"]
Maps = Data["maps"]
GridData = Maps[0]["tiles"]
GridW = Maps[0]["width"]
GridH = math.floor(len(GridData)/GridW)
CamX = 0
CamY = 0

class FrameTile:
    Ox = 0
    Oy = 0
    InFrame = []
FrameT = FrameTile()

def GetTile(x, y):
    Tx = math.floor(x/16)
    Ty = math.floor(y/16)
    idx = Ty*GridW + Tx
    return idx

def GetBlocksInFrame():
	OffsetX = CamX % 16
	OffsetY = CamY % 16
	FrameT["Ox"] = OffsetX
	FrameT["Oy"] = OffsetY
	FrameT["InFrame"] = []
	for y in range(0,16):
		for x in range(0,17):
			idx = GetTile((x*16 - OffsetX),(y*16 - OffsetY))
			FrameT["InFrame"].append(idx)

def MainLoop():
    RUN = True
    while RUN:
        GetBlocksInFrame()
        render.DrawFrame(FrameT)
