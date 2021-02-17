#!/usr/bin/env python

import sys
import argparse
import pickle

parser = argparse.ArgumentParser(description='Build label list')
parser.add_argument('species',type=open,help='The species header (include/constants/species.h)')
parser.add_argument('items',type=open,help='The items header (include/constants/items.h)')
parser.add_argument('reference',type=argparse.FileType('wb'),help='The output reference file')
parser.add_argument('output',type=argparse.FileType('wb'),help='The output label file')

args = parser.parse_args()

species = {}

lines = args.species.readlines()

forms_start = None

for line in lines:
	elements = line.split()
	if len(elements) < 3:
		continue
	if elements[0] != '#define':
		continue
	if not elements[1].startswith('SPECIES_'):
		if elements[1] == 'FORMS_START':
			if elements[2] in species:
				forms_start = species[elements[2]]
			else:
				print('WARN unrecognized forms_start %s'%elements[2])
		continue
	if elements[2] == 'FORMS_START':
		try:
			value = int(elements[4])
			if elements[1] in species:
				print('WARN %s %d %s'%(elements[1],species[elements[1]],line))
			if elements[3] == '+':
				species[elements[1]] = forms_start + value
			elif elements[3] == '-':
				species[elements[1]] = forms_start - value
		except ValueError:
			print('WARN unrecognised format for relative forms offset %s'%line)
			pass
	else:
		try:
			value = int(elements[2])
			if elements[1] in species:
				print('WARN %s %d %d'%(elements[1],species[elements[1]],value))
			species[elements[1]] = value
		except ValueError:
			pass

items = {}

lines = args.items.readlines()

for line in lines:
	elements = line.split()
	if len(elements) < 3:
		continue
	if elements[0] != '#define':
		continue
	if not elements[1].startswith('ITEM_'):
		continue
	if elements[1].startswith('ITEM_USE_') or elements[1].startswith('ITEM_B_USE_') :
		continue
	try:
		value = int(elements[2])
		if elements[1] in items:
			print('WARN %s %d %d'%(elements[1],items[elements[1]],value))
		items[elements[1]] = value
	except:
		pass

pickle.dump((species,items),args.reference)
args.reference.close()
args.species.close()
args.items.close()

#print(species)
#print(items)
#sys.exit()


mon_labels = {}

# Wild Tables:

mon_labels['gMirageTower_2F_LandMons'] = (['LandMons'],None)
mon_labels['gRoute116_LandMons'] = (['LandMons'],None)
mon_labels['gVictoryRoad_B2F_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave7_LandMons'] = (['LandMons'],None)
mon_labels['gRoute123_LandMons'] = (['LandMons'],None)
mon_labels['gRoute117_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_2_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_3F_2R_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave1_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_2F_3R_LandMons'] = (['LandMons'],None)
mon_labels['gRoute104_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePike_3_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_Exterior_LandMons'] = (['LandMons'],None)
mon_labels['gShoalCave_LowTideIceRoom_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_4F_LandMons'] = (['LandMons'],None)
mon_labels['gArtisanCave_1F_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave4_LandMons'] = (['LandMons'],None)
mon_labels['gRoute101_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_3F_1R_LandMons'] = (['LandMons'],None)
mon_labels['gNewMauville_Entrance_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_5_LandMons'] = (['LandMons'],None)
mon_labels['gFieryPath_LandMons'] = (['LandMons'],None)
mon_labels['gMeteorFalls_1F_2R_LandMons'] = (['LandMons'],None)
mon_labels['gRoute113_LandMons'] = (['LandMons'],None)
mon_labels['gRusturfTunnel_LandMons'] = (['LandMons'],None)
mon_labels['gGraniteCave_StevensRoom_LandMons'] = (['LandMons'],None)
mon_labels['gMeteorFalls_1F_1R_LandMons'] = (['LandMons'],None)
mon_labels['gCaveOfOrigin_1F_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_Summit_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_4F_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room2_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave5_LandMons'] = (['LandMons'],None)
mon_labels['gSkyPillar_1F_LandMons'] = (['LandMons'],None)
mon_labels['gRoute121_LandMons'] = (['LandMons'],None)
mon_labels['gCaveOfOrigin_UnusedRubySapphireMap1_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_1F_LandMons'] = (['LandMons'],None)
mon_labels['gShoalCave_LowTideStairsRoom_LandMons'] = (['LandMons'],None)
mon_labels['gRoute118_LandMons'] = (['LandMons'],None)
mon_labels['gRoute114_LandMons'] = (['LandMons'],None)
mon_labels['gSafariZone_North_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave8_LandMons'] = (['LandMons'],None)
mon_labels['gSafariZone_Southeast_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room3_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_5F_LandMons'] = (['LandMons'],None)
mon_labels['gJaggedPass_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePike_4_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_7_LandMons'] = (['LandMons'],None)
mon_labels['gGraniteCave_B2F_LandMons'] = (['LandMons'],None)
mon_labels['gSafariZone_Southwest_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePike_2_LandMons'] = (['LandMons'],None)
mon_labels['gSafariZone_Northwest_LandMons'] = (['LandMons'],None)
mon_labels['gDesertUnderpass_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room6_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_3F_3R_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_2F_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_1F_LandMons'] = (['LandMons'],None)
mon_labels['gArtisanCave_B1F_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_3F_LandMons'] = (['LandMons'],None)
mon_labels['gNewMauville_Inside_LandMons'] = (['LandMons'],None)
mon_labels['gMirageTower_3F_LandMons'] = (['LandMons'],None)
mon_labels['gRoute120_LandMons'] = (['LandMons'],None)
mon_labels['gSkyPillar_3F_LandMons'] = (['LandMons'],None)
mon_labels['gShoalCave_LowTideInnerRoom_LandMons'] = (['LandMons'],None)
mon_labels['gCaveOfOrigin_UnusedRubySapphireMap2_LandMons'] = (['LandMons'],None)
mon_labels['gMirageTower_1F_LandMons'] = (['LandMons'],None)
mon_labels['gSafariZone_South_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave9_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave3_LandMons'] = (['LandMons'],None)
mon_labels['gMirageTower_4F_LandMons'] = (['LandMons'],None)
mon_labels['gMeteorFalls_StevensCave_LandMons'] = (['LandMons'],None)
mon_labels['gShoalCave_LowTideLowerRoom_LandMons'] = (['LandMons'],None)
mon_labels['gShoalCave_LowTideEntranceRoom_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room8_LandMons'] = (['LandMons'],None)
mon_labels['gPetalburgWoods_LandMons'] = (['LandMons'],None)
mon_labels['gSkyPillar_5F_LandMons'] = (['LandMons'],None)
mon_labels['gRoute130_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_2F_2R_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_1_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room5_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave6_LandMons'] = (['LandMons'],None)
mon_labels['gRoute115_LandMons'] = (['LandMons'],None)
mon_labels['gCaveOfOrigin_UnusedRubySapphireMap3_LandMons'] = (['LandMons'],None)
mon_labels['gRoute102_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room1_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room4_LandMons'] = (['LandMons'],None)
mon_labels['gMeteorFalls_B1F_1R_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_4_LandMons'] = (['LandMons'],None)
mon_labels['gMtPyre_6F_LandMons'] = (['LandMons'],None)
mon_labels['gSafariZone_Northeast_LandMons'] = (['LandMons'],None)
mon_labels['gRoute119_LandMons'] = (['LandMons'],None)
mon_labels['gRoute103_LandMons'] = (['LandMons'],None)
mon_labels['gRoute111_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePike_1_LandMons'] = (['LandMons'],None)
mon_labels['gVictoryRoad_B1F_LandMons'] = (['LandMons'],None)
mon_labels['gGraniteCave_B1F_LandMons'] = (['LandMons'],None)
mon_labels['gMeteorFalls_B1F_2R_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_3_LandMons'] = (['LandMons'],None)
mon_labels['gMagmaHideout_2F_1R_LandMons'] = (['LandMons'],None)
mon_labels['gAlteringCave2_LandMons'] = (['LandMons'],None)
mon_labels['gBattlePyramid_6_LandMons'] = (['LandMons'],None)
mon_labels['gRoute110_LandMons'] = (['LandMons'],None)
mon_labels['gRoute112_LandMons'] = (['LandMons'],None)
mon_labels['gGraniteCave_1F_LandMons'] = (['LandMons'],None)
mon_labels['gCaveOfOrigin_Entrance_LandMons'] = (['LandMons'],None)
mon_labels['gVictoryRoad_1F_LandMons'] = (['LandMons'],None)
mon_labels['gSeafloorCavern_Room7_LandMons'] = (['LandMons'],None)

mon_labels['gAbandonedShip_Rooms_B1F_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute126_WaterMons'] = (['WaterMons'],None)
mon_labels['gSeafloorCavern_Room6_WaterMons'] = (['WaterMons'],None)
mon_labels['gDewfordTown_WaterMons'] = (['WaterMons'],None)
mon_labels['gShoalCave_LowTideInnerRoom_WaterMons'] = (['WaterMons'],None)
mon_labels['gVictoryRoad_B2F_WaterMons'] = (['WaterMons'],None)
mon_labels['gEverGrandeCity_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute118_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute123_WaterMons'] = (['WaterMons'],None)
mon_labels['gSootopolisCity_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute110_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute108_WaterMons'] = (['WaterMons'],None)
mon_labels['gSafariZone_Northwest_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute103_WaterMons'] = (['WaterMons'],None)
mon_labels['gPetalburgCity_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute111_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute119_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute104_WaterMons'] = (['WaterMons'],None)
mon_labels['gMossdeepCity_WaterMons'] = (['WaterMons'],None)
mon_labels['gSeafloorCavern_Entrance_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute131_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute120_WaterMons'] = (['WaterMons'],None)
mon_labels['gMeteorFalls_B1F_1R_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute125_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute115_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute133_WaterMons'] = (['WaterMons'],None)
mon_labels['gUnderwater_Route126_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute106_WaterMons'] = (['WaterMons'],None)
mon_labels['gPacifidlogTown_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute121_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute127_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute107_WaterMons'] = (['WaterMons'],None)
mon_labels['gMeteorFalls_1F_1R_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute132_WaterMons'] = (['WaterMons'],None)
mon_labels['gAbandonedShip_HiddenFloorCorridors_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute114_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute128_WaterMons'] = (['WaterMons'],None)
mon_labels['gUnderwater_Route124_WaterMons'] = (['WaterMons'],None)
mon_labels['gLilycoveCity_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute129_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute134_WaterMons'] = (['WaterMons'],None)
mon_labels['gMeteorFalls_1F_2R_WaterMons'] = (['WaterMons'],None)
mon_labels['gShoalCave_LowTideEntranceRoom_WaterMons'] = (['WaterMons'],None)
mon_labels['gMeteorFalls_B1F_2R_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute105_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute109_WaterMons'] = (['WaterMons'],None)
mon_labels['gSeafloorCavern_Room7_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute102_WaterMons'] = (['WaterMons'],None)
mon_labels['gSafariZone_Southwest_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute122_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute117_WaterMons'] = (['WaterMons'],None)
mon_labels['gSlateportCity_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute130_WaterMons'] = (['WaterMons'],None)
mon_labels['gRoute124_WaterMons'] = (['WaterMons'],None)
mon_labels['gSafariZone_Southeast_WaterMons'] = (['WaterMons'],None)

mon_labels['gVictoryRoad_B2F_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute122_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute132_FishingMons'] = (['FishingMons'],None)
mon_labels['gSafariZone_Northwest_FishingMons'] = (['FishingMons'],None)
mon_labels['gDewfordTown_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute114_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute107_FishingMons'] = (['FishingMons'],None)
mon_labels['gMeteorFalls_B1F_1R_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute103_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute108_FishingMons'] = (['FishingMons'],None)
mon_labels['gShoalCave_LowTideInnerRoom_FishingMons'] = (['FishingMons'],None)
mon_labels['gSafariZone_Southwest_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute102_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute134_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute126_FishingMons'] = (['FishingMons'],None)
mon_labels['gPacifidlogTown_FishingMons'] = (['FishingMons'],None)
mon_labels['gMeteorFalls_1F_2R_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute124_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute121_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute110_FishingMons'] = (['FishingMons'],None)
mon_labels['gSeafloorCavern_Room7_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute118_FishingMons'] = (['FishingMons'],None)
mon_labels['gMossdeepCity_FishingMons'] = (['FishingMons'],None)
mon_labels['gMeteorFalls_B1F_2R_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute131_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute111_FishingMons'] = (['FishingMons'],None)
mon_labels['gShoalCave_LowTideEntranceRoom_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute127_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute105_FishingMons'] = (['FishingMons'],None)
mon_labels['gAbandonedShip_Rooms_B1F_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute129_FishingMons'] = (['FishingMons'],None)
mon_labels['gSootopolisCity_FishingMons'] = (['FishingMons'],None)
mon_labels['gPetalburgCity_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute123_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute125_FishingMons'] = (['FishingMons'],None)
mon_labels['gLilycoveCity_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute117_FishingMons'] = (['FishingMons'],None)
mon_labels['gSafariZone_Southeast_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute130_FishingMons'] = (['FishingMons'],None)
mon_labels['gMeteorFalls_1F_1R_FishingMons'] = (['FishingMons'],None)
mon_labels['gSeafloorCavern_Entrance_FishingMons'] = (['FishingMons'],None)
mon_labels['gSeafloorCavern_Room6_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute128_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute133_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute109_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute104_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute115_FishingMons'] = (['FishingMons'],None)
mon_labels['gEverGrandeCity_FishingMons'] = (['FishingMons'],None)
mon_labels['gAbandonedShip_HiddenFloorCorridors_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute119_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute106_FishingMons'] = (['FishingMons'],None)
mon_labels['gRoute120_FishingMons'] = (['FishingMons'],None)
mon_labels['gSlateportCity_FishingMons'] = (['FishingMons'],None)

mon_labels['gGraniteCave_B2F_RockSmashMons'] = (['RockSmashMons'],None)
mon_labels['gSafariZone_North_RockSmashMons'] = (['RockSmashMons'],None)
mon_labels['gVictoryRoad_B1F_RockSmashMons'] = (['RockSmashMons'],None)
mon_labels['gRoute111_RockSmashMons'] = (['RockSmashMons'],None)
mon_labels['gSafariZone_Northeast_RockSmashMons'] = (['RockSmashMons'],None)
mon_labels['gRoute114_RockSmashMons'] = (['RockSmashMons'],None)

# Gift Mons:

mon_labels['sStarterMon'] = (['Starters'],None)

## In scripts, need offset:

encounter_id = 0
pokemon = None
item = None

### Cyndaquil 0x9b00
pokemon = species['SPECIES_CYNDAQUIL']
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_Cyndaquil'] = (['showmonpic'],(encounter_id,(pokemon,item)))
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_GiveCyndaquil'] = (['bufferspeciesname','setvar','givemon'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Chikorita 0x9800
pokemon = species['SPECIES_CHIKORITA']
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_Chikorita'] = (['showmonpic'],(encounter_id,(pokemon,item)))
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_GiveChikorita'] = (['bufferspeciesname','setvar','givemon'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Totodile 0x9e00
pokemon = species['SPECIES_TOTODILE']
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_Totodile'] = (['showmonpic'],(encounter_id,(pokemon,item)))
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_GiveTotodile'] = (['bufferspeciesname','setvar','givemon'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Beldum 0x7601
pokemon = species['SPECIES_BELDUM']
mon_labels['MossdeepCity_StevensHouse_EventScript_GiveBeldum'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['MossdeepCity_StevensHouse_EventScript_ReceivedBeldumFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Castform 0x5f01 (HOLDING MYSTIC WATER 0xf800)
pokemon = species['SPECIES_CASTFORM']
item = items['ITEM_MYSTIC_WATER']
mon_labels['Route119_WeatherInstitute_2F_EventScript_ReceiveCastform'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['Route119_WeatherInstitute_2F_EventScript_ReceivedCastformFanfare'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

item = None

### Wynaut Egg 0x6801
pokemon = species['SPECIES_WYNAUT']
mon_labels['LavaridgeTown_EventScript_EggWoman'] = (['giveegg'],(encounter_id,(pokemon,item)))
encounter_id+=1

# Static encounters:

## Rayquaza 0x8001
pokemon = species['SPECIES_RAYQUAZA']
mon_labels['SootopolisCity_EventScript_RayquazaSceneFromPokeCenter'] = (['playmoncry','playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['SootopolisCity_EventScript_RayquazaSceneFromDive'] = (['playmoncry','playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['SkyPillar_Top_EventScript_Rayquaza'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
mon_labels['SkyPillar_Top_EventScript_AwakenRayquaza'] = (['playmoncry','playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['SkyPillar_Top_EventScript_RanFromRayquaza'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Groudon 0x7f01
pokemon = species['SPECIES_GROUDON']
mon_labels['SootopolisCity_EventScript_LegendariesSceneFromPokeCenter'] = (['playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['SootopolisCity_EventScript_LegendariesSceneFromDive'] = (['playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['TerraCave_End_EventScript_Groudon'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
mon_labels['TerraCave_End_EventScript_RanFromGroudon'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Kyogre 0x7e01
pokemon = species['SPECIES_KYOGRE']
mon_labels['SootopolisCity_EventScript_LegendariesSceneFromPokeCenter'] = (['playmoncry','playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['SootopolisCity_EventScript_LegendariesSceneFromDive'] = (['playmoncry','playmoncry'],(encounter_id,(pokemon,item)))
mon_labels['MarineCave_End_EventScript_Kyogre'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
mon_labels['MarineCave_End_EventScript_RanFromKyogre'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Sudowoodo 0xb900
pokemon = species['SPECIES_SUDOWOODO']
mon_labels['BattleFrontier_OutsideEast_EventScript_WaterSudowoodo'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Mew 0x9700
pokemon = species['SPECIES_MEW']
mon_labels['FarawayIsland_Interior_EventScript_Mew'] = (['playmoncry','setvar'],(encounter_id,(pokemon,item)))
mon_labels['FarawayIsland_Interior_EventScript_MewDefeated'] = (['setvar'],(encounter_id,(pokemon,item)))
mon_labels['FarawayIsland_Interior_EventScript_PlayerOrMewRan'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Ho-oh 0xfa00
pokemon = species['SPECIES_HO_OH']
mon_labels['NavelRock_Top_EventScript_HoOh'] = (['playmoncry','setvar'],(encounter_id,(pokemon,item)))
mon_labels['NavelRock_Top_EventScript_DefeatedHoOh'] = (['setvar'],(encounter_id,(pokemon,item)))
mon_labels['NavelRock_Top_EventScript_RanFromHoOh'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Lugia 0xf900
pokemon = species['SPECIES_LUGIA']
mon_labels['NavelRock_Bottom_EventScript_Lugia'] = (['playmoncry','setvar'],(encounter_id,(pokemon,item)))
mon_labels['NavelRock_Bottom_EventScript_DefeatedLugia'] = (['setvar'],(encounter_id,(pokemon,item)))
mon_labels['NavelRock_Bottom_EventScript_RanFromLugia'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Deoxys 0x8201
pokemon = species['SPECIES_DEOXYS']
mon_labels['BirthIsland_Exterior_EventScript_Deoxys'] = (['playmoncry','setvar'],(encounter_id,(pokemon,item)))
mon_labels['BirthIsland_Exterior_EventScript_DefeatedDeoxys'] = (['setvar'],(encounter_id,(pokemon,item)))
mon_labels['BirthIsland_Exterior_EventScript_RanFromDeoxys'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Latios 0x7d01
pokemon = species['SPECIES_LATIOS']
mon_labels['sRoamerMons'] = (['hard'],(encounter_id,(pokemon,item)))
mon_labels['SouthernIsland_Interior_EventScript_SetUpLatios'] = (['setvar'],(encounter_id,(pokemon,item)))
mon_labels['SouthernIsland_Interior_EventScript_SetLatiosBattleVars'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Latias 0x7c01
pokemon = species['SPECIES_LATIAS']
#mon_labels['sRoamerMons'] = (['hard'],(encounter_id,(pokemon,item))) WOULD BE OVERWRITING
mon_labels['SouthernIsland_Interior_EventScript_SetUpLatias'] = (['setvar'],(encounter_id,(pokemon,item)))
mon_labels['SouthernIsland_Interior_EventScript_SetLatiasBattleVars'] = (['setvar'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Regirock 0x7901
pokemon = species['SPECIES_REGIROCK']
mon_labels['DesertRuins_EventScript_Regirock'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Regice 0x7a01
pokemon = species['SPECIES_REGICE']
mon_labels['IslandCave_EventScript_Regice'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Registeel 0x7b01
pokemon = species['SPECIES_REGISTEEL']
mon_labels['AncientTomb_EventScript_Registeel'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
encounter_id+=1

## New Mauville Voltorbs 0x6400
pokemon = species['SPECIES_VOLTORB']
mon_labels['NewMauville_Inside_EventScript_Voltorb1'] = (['setwildbattle','playmoncry'],(encounter_id,(pokemon,item)))
encounter_id+=1
mon_labels['NewMauville_Inside_EventScript_Voltorb2'] = (['setwildbattle','playmoncry'],(encounter_id,(pokemon,item)))
encounter_id+=1
mon_labels['NewMauville_Inside_EventScript_Voltorb3'] = (['setwildbattle','playmoncry'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Aqua Hideout Electrodes 0x6500
pokemon = species['SPECIES_ELECTRODE']
mon_labels['AquaHideout_B1F_EventScript_Electrode1'] = (['setwildbattle','playmoncry'],(encounter_id,(pokemon,item)))
encounter_id+=1
mon_labels['AquaHideout_B1F_EventScript_Electrode2'] = (['setwildbattle','playmoncry'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Kecleons (1 + 7) 0x6001
pokemon = species['SPECIES_KECLEON']
mon_labels['Route120_EventScript_StevenBattleKecleon'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
encounter_id+=1

mon_labels['EventScript_BattleKecleon'] = (['playmoncry','setwildbattle'],(encounter_id,(pokemon,item)))
encounter_id+=1

## Fossils
pokemon = species['SPECIES_AERODACTYL']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_AerodactylReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveAerodactyl'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedAerodactylFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_KABUTO']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_KabutoReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveKabuto'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedKabutoFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_OMANYTE']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_OmanyteReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveOmanyte'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedOmanyteFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_ANORITH']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_AnorithReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveAnorith'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedAnorithFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_LILEEP']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_LileepReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveLileep'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedLileepFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_CRANIDOS']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_CranidosReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveCranidos'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedCranidosFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_SHIELDON']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ShieldonReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveShieldon'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedShieldonFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_TIRTOUGA']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_TirtougaReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveTirtouga'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedTirtougaFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_ARCHEN']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ArchenReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveArchen'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedArchenFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_TYRUNT']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_TyruntReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveTyrunt'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedTyruntFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

pokemon = species['SPECIES_AMAURA']
mon_labels['RustboroCity_DevonCorp_2F_EventScript_AmauraReady'] = (['bufferspeciesname'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceiveAmaura'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['RustboroCity_DevonCorp_2F_EventScript_ReceivedAmauraFanfare'] = (['bufferspeciesname','bufferspeciesname'],(encounter_id,(pokemon,item)))
encounter_id+=1

# Trades
trade_labels = {}

trade_labels['sIngameTrades'] = [
		(species['SPECIES_SEEDOT'],items['ITEM_CHESTO_BERRY'],species['SPECIES_RALTS']), # Seedot, Chesto berry, Ralts
		(species['SPECIES_PLUSLE'],items['ITEM_WOOD_MAIL'],species['SPECIES_VOLBEAT']), # Plusle, Wood Mail, Volbeat
		(species['SPECIES_HORSEA'],items['ITEM_WAVE_MAIL'],species['SPECIES_BAGON']), # Horsea, Wave Mail, Bagon
		(species['SPECIES_MEOWTH'],items['ITEM_RETRO_MAIL'],species['SPECIES_SKITTY']), # Meowth, Retro Mail, Skitty
		]

# Foes
foe_item_labels = {}
foe_item_labels['sParty_Alexia'] = [(species['SPECIES_WIGGLYTUFF'],items['ITEM_NONE'])]
foe_item_labels['sParty_Angelo'] = [(species['SPECIES_ILLUMISE'],items['ITEM_NONE']),(species['SPECIES_VOLBEAT'],items['ITEM_NONE'])]
foe_item_labels['sParty_Annika'] = [(species['SPECIES_FEEBAS'],items['ITEM_ORAN_BERRY']),(species['SPECIES_FEEBAS'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Athena'] = [(species['SPECIES_MANECTRIC'],items['ITEM_NONE']),(species['SPECIES_LINOONE'],items['ITEM_NONE'])]
foe_item_labels['sParty_Berke'] = [(species['SPECIES_VIGOROTH'],items['ITEM_NONE'])]
foe_item_labels['sParty_Bethany'] = [(species['SPECIES_AZURILL'],items['ITEM_ORAN_BERRY']),(species['SPECIES_MARILL'],items['ITEM_ORAN_BERRY']),(species['SPECIES_AZUMARILL'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Brawly1'] = [(species['SPECIES_MACHOP'],items['ITEM_NONE']),(species['SPECIES_MEDITITE'],items['ITEM_NONE']),(species['SPECIES_MAKUHITA'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Brawly2'] = [(species['SPECIES_MACHAMP'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MEDITITE'],items['ITEM_NONE']),(species['SPECIES_HITMONTOP'],items['ITEM_NONE']),(species['SPECIES_HARIYAMA'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Brawly3'] = [(species['SPECIES_MACHAMP'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MEDICHAM'],items['ITEM_NONE']),(species['SPECIES_HITMONTOP'],items['ITEM_NONE']),(species['SPECIES_HARIYAMA'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Brawly4'] = [(species['SPECIES_HITMONCHAN'],items['ITEM_NONE']),(species['SPECIES_MACHAMP'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MEDICHAM'],items['ITEM_NONE']),(species['SPECIES_HITMONTOP'],items['ITEM_NONE']),(species['SPECIES_HARIYAMA'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Brawly5'] = [(species['SPECIES_HITMONLEE'],items['ITEM_NONE']),(species['SPECIES_HITMONCHAN'],items['ITEM_NONE']),(species['SPECIES_MACHAMP'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MEDICHAM'],items['ITEM_NONE']),(species['SPECIES_HITMONTOP'],items['ITEM_NONE']),(species['SPECIES_HARIYAMA'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Brianna'] = [(species['SPECIES_SEAKING'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Cindy1'] = [(species['SPECIES_ZIGZAGOON'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Cindy2'] = [(species['SPECIES_ZIGZAGOON'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Cindy3'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Cindy4'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Cindy5'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Cindy6'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Colton'] = [(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY']),(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY']),(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY']),(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY']),(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY']),(species['SPECIES_DELCATTY'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Daphne'] = [(species['SPECIES_LUVDISC'],items['ITEM_NUGGET']),(species['SPECIES_LUVDISC'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Dawson'] = [(species['SPECIES_ZIGZAGOON'],items['ITEM_NUGGET']),(species['SPECIES_POOCHYENA'],items['ITEM_NONE'])]
foe_item_labels['sParty_Dianne'] = [(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_LANTURN'],items['ITEM_NONE'])]
foe_item_labels['sParty_Drake'] = [(species['SPECIES_SHELGON'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_NONE']),(species['SPECIES_KINGDRA'],items['ITEM_NONE']),(species['SPECIES_FLYGON'],items['ITEM_NONE']),(species['SPECIES_SALAMENCE'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Flannery1'] = [(species['SPECIES_NUMEL'],items['ITEM_NONE']),(species['SPECIES_SLUGMA'],items['ITEM_NONE']),(species['SPECIES_CAMERUPT'],items['ITEM_NONE']),(species['SPECIES_TORKOAL'],items['ITEM_WHITE_HERB'])]
foe_item_labels['sParty_Flannery2'] = [(species['SPECIES_MAGCARGO'],items['ITEM_WHITE_HERB']),(species['SPECIES_PONYTA'],items['ITEM_NONE']),(species['SPECIES_CAMERUPT'],items['ITEM_WHITE_HERB']),(species['SPECIES_TORKOAL'],items['ITEM_WHITE_HERB'])]
foe_item_labels['sParty_Flannery3'] = [(species['SPECIES_GROWLITHE'],items['ITEM_NONE']),(species['SPECIES_MAGCARGO'],items['ITEM_WHITE_HERB']),(species['SPECIES_PONYTA'],items['ITEM_NONE']),(species['SPECIES_CAMERUPT'],items['ITEM_WHITE_HERB']),(species['SPECIES_TORKOAL'],items['ITEM_WHITE_HERB'])]
foe_item_labels['sParty_Flannery4'] = [(species['SPECIES_HOUNDOUR'],items['ITEM_NONE']),(species['SPECIES_GROWLITHE'],items['ITEM_NONE']),(species['SPECIES_MAGCARGO'],items['ITEM_WHITE_HERB']),(species['SPECIES_RAPIDASH'],items['ITEM_NONE']),(species['SPECIES_CAMERUPT'],items['ITEM_WHITE_HERB']),(species['SPECIES_TORKOAL'],items['ITEM_WHITE_HERB'])]
foe_item_labels['sParty_Flannery5'] = [(species['SPECIES_ARCANINE'],items['ITEM_NONE']),(species['SPECIES_MAGCARGO'],items['ITEM_WHITE_HERB']),(species['SPECIES_HOUNDOOM'],items['ITEM_NONE']),(species['SPECIES_RAPIDASH'],items['ITEM_NONE']),(species['SPECIES_CAMERUPT'],items['ITEM_WHITE_HERB']),(species['SPECIES_TORKOAL'],items['ITEM_WHITE_HERB'])]
foe_item_labels['sParty_Garret'] = [(species['SPECIES_AZUMARILL'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_George'] = [(species['SPECIES_SLAKOTH'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Glacia'] = [(species['SPECIES_SEALEO'],items['ITEM_NONE']),(species['SPECIES_GLALIE'],items['ITEM_NONE']),(species['SPECIES_SEALEO'],items['ITEM_NONE']),(species['SPECIES_GLALIE'],items['ITEM_NONE']),(species['SPECIES_WALREIN'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Isabel1'] = [(species['SPECIES_PLUSLE'],items['ITEM_ORAN_BERRY']),(species['SPECIES_MINUN'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Isabel2'] = [(species['SPECIES_PLUSLE'],items['ITEM_ORAN_BERRY']),(species['SPECIES_MINUN'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Isabel3'] = [(species['SPECIES_PLUSLE'],items['ITEM_ORAN_BERRY']),(species['SPECIES_MINUN'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Isabel4'] = [(species['SPECIES_PLUSLE'],items['ITEM_ORAN_BERRY']),(species['SPECIES_MINUN'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Isabel5'] = [(species['SPECIES_PLUSLE'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MINUN'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Jeffrey5'] = [(species['SPECIES_SURSKIT'],items['ITEM_NONE']),(species['SPECIES_DUSTOX'],items['ITEM_NONE']),(species['SPECIES_SURSKIT'],items['ITEM_NONE']),(species['SPECIES_MASQUERAIN'],items['ITEM_SILVER_POWDER']),(species['SPECIES_BEAUTIFLY'],items['ITEM_NONE'])]
foe_item_labels['sParty_Jody'] = [(species['SPECIES_ZANGOOSE'],items['ITEM_NONE'])]
foe_item_labels['sParty_Juan1'] = [(species['SPECIES_LUVDISC'],items['ITEM_NONE']),(species['SPECIES_WHISCASH'],items['ITEM_NONE']),(species['SPECIES_SEALEO'],items['ITEM_NONE']),(species['SPECIES_CRAWDAUNT'],items['ITEM_NONE']),(species['SPECIES_KINGDRA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Juan2'] = [(species['SPECIES_POLIWAG'],items['ITEM_NONE']),(species['SPECIES_WHISCASH'],items['ITEM_NONE']),(species['SPECIES_WALREIN'],items['ITEM_NONE']),(species['SPECIES_CRAWDAUNT'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_KINGDRA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Juan3'] = [(species['SPECIES_POLIWHIRL'],items['ITEM_NONE']),(species['SPECIES_WHISCASH'],items['ITEM_NONE']),(species['SPECIES_WALREIN'],items['ITEM_NONE']),(species['SPECIES_CRAWDAUNT'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_KINGDRA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Juan4'] = [(species['SPECIES_LAPRAS'],items['ITEM_NONE']),(species['SPECIES_WHISCASH'],items['ITEM_NONE']),(species['SPECIES_POLIWHIRL'],items['ITEM_NONE']),(species['SPECIES_WALREIN'],items['ITEM_NONE']),(species['SPECIES_CRAWDAUNT'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_KINGDRA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Juan5'] = [(species['SPECIES_LAPRAS'],items['ITEM_NONE']),(species['SPECIES_WHISCASH'],items['ITEM_NONE']),(species['SPECIES_POLITOED'],items['ITEM_NONE']),(species['SPECIES_WALREIN'],items['ITEM_NONE']),(species['SPECIES_CRAWDAUNT'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_KINGDRA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Kaleb'] = [(species['SPECIES_MINUN'],items['ITEM_ORAN_BERRY']),(species['SPECIES_PLUSLE'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Lao5'] = [(species['SPECIES_KOFFING'],items['ITEM_NONE']),(species['SPECIES_KOFFING'],items['ITEM_NONE']),(species['SPECIES_KOFFING'],items['ITEM_NONE']),(species['SPECIES_WEEZING'],items['ITEM_SMOKE_BALL'])]
foe_item_labels['sParty_Marley'] = [(species['SPECIES_MANECTRIC'],items['ITEM_NONE'])]
foe_item_labels['sParty_Mary'] = [(species['SPECIES_DELCATTY'],items['ITEM_NONE'])]
foe_item_labels['sParty_Miguel1'] = [(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Miguel2'] = [(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Miguel3'] = [(species['SPECIES_SKITTY'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Miguel4'] = [(species['SPECIES_DELCATTY'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Miguel5'] = [(species['SPECIES_DELCATTY'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Naomi'] = [(species['SPECIES_ROSELIA'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Nicolas5'] = [(species['SPECIES_ALTARIA'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_NONE']),(species['SPECIES_SHELGON'],items['ITEM_DRAGON_FANG'])]
foe_item_labels['sParty_Nob5'] = [(species['SPECIES_MACHOP'],items['ITEM_NONE']),(species['SPECIES_MACHOKE'],items['ITEM_NONE']),(species['SPECIES_MACHOKE'],items['ITEM_NONE']),(species['SPECIES_MACHAMP'],items['ITEM_BLACK_BELT'])]
foe_item_labels['sParty_Norman1'] = [(species['SPECIES_SPINDA'],items['ITEM_NONE']),(species['SPECIES_VIGOROTH'],items['ITEM_NONE']),(species['SPECIES_LINOONE'],items['ITEM_NONE']),(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Norman2'] = [(species['SPECIES_CHANSEY'],items['ITEM_NONE']),(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_SPINDA'],items['ITEM_NONE']),(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Norman3'] = [(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_CHANSEY'],items['ITEM_NONE']),(species['SPECIES_KANGASKHAN'],items['ITEM_NONE']),(species['SPECIES_SPINDA'],items['ITEM_NONE']),(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Norman4'] = [(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_BLISSEY'],items['ITEM_NONE']),(species['SPECIES_KANGASKHAN'],items['ITEM_NONE']),(species['SPECIES_SPINDA'],items['ITEM_NONE']),(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Norman5'] = [(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_BLISSEY'],items['ITEM_NONE']),(species['SPECIES_KANGASKHAN'],items['ITEM_NONE']),(species['SPECIES_TAUROS'],items['ITEM_NONE']),(species['SPECIES_SPINDA'],items['ITEM_NONE']),(species['SPECIES_SLAKING'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Parker'] = [(species['SPECIES_SPINDA'],items['ITEM_NONE'])]
foe_item_labels['sParty_Phoebe'] = [(species['SPECIES_DUSCLOPS'],items['ITEM_NONE']),(species['SPECIES_BANETTE'],items['ITEM_NONE']),(species['SPECIES_SABLEYE'],items['ITEM_NONE']),(species['SPECIES_BANETTE'],items['ITEM_NONE']),(species['SPECIES_DUSCLOPS'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Randall'] = [(species['SPECIES_SWELLOW'],items['ITEM_NONE'])]
foe_item_labels['sParty_Roxanne1'] = [(species['SPECIES_GEODUDE'],items['ITEM_NONE']),(species['SPECIES_GEODUDE'],items['ITEM_NONE']),(species['SPECIES_NOSEPASS'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Roxanne2'] = [(species['SPECIES_GOLEM'],items['ITEM_NONE']),(species['SPECIES_KABUTO'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_ONIX'],items['ITEM_NONE']),(species['SPECIES_NOSEPASS'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Roxanne3'] = [(species['SPECIES_OMANYTE'],items['ITEM_NONE']),(species['SPECIES_GOLEM'],items['ITEM_NONE']),(species['SPECIES_KABUTOPS'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_ONIX'],items['ITEM_NONE']),(species['SPECIES_NOSEPASS'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Roxanne4'] = [(species['SPECIES_OMASTAR'],items['ITEM_NONE']),(species['SPECIES_GOLEM'],items['ITEM_NONE']),(species['SPECIES_KABUTOPS'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_ONIX'],items['ITEM_NONE']),(species['SPECIES_NOSEPASS'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Roxanne5'] = [(species['SPECIES_AERODACTYL'],items['ITEM_NONE']),(species['SPECIES_GOLEM'],items['ITEM_NONE']),(species['SPECIES_OMASTAR'],items['ITEM_NONE']),(species['SPECIES_KABUTOPS'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_STEELIX'],items['ITEM_NONE']),(species['SPECIES_NOSEPASS'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Sarah'] = [(species['SPECIES_LOTAD'],items['ITEM_NONE']),(species['SPECIES_ZIGZAGOON'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Sidney'] = [(species['SPECIES_MIGHTYENA'],items['ITEM_NONE']),(species['SPECIES_SHIFTRY'],items['ITEM_NONE']),(species['SPECIES_CACTURNE'],items['ITEM_NONE']),(species['SPECIES_CRAWDAUNT'],items['ITEM_NONE']),(species['SPECIES_ABSOL'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Steven'] = [(species['SPECIES_SKARMORY'],items['ITEM_NONE']),(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_AGGRON'],items['ITEM_NONE']),(species['SPECIES_CRADILY'],items['ITEM_NONE']),(species['SPECIES_ARMALDO'],items['ITEM_NONE']),(species['SPECIES_METAGROSS'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_TateAndLiza1'] = [(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_XATU'],items['ITEM_NONE']),(species['SPECIES_LUNATONE'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_SOLROCK'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_TateAndLiza2'] = [(species['SPECIES_SLOWPOKE'],items['ITEM_NONE']),(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_XATU'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_LUNATONE'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_SOLROCK'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_TateAndLiza3'] = [(species['SPECIES_DROWZEE'],items['ITEM_NONE']),(species['SPECIES_SLOWPOKE'],items['ITEM_NONE']),(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_XATU'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_LUNATONE'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_SOLROCK'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_TateAndLiza4'] = [(species['SPECIES_HYPNO'],items['ITEM_NONE']),(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_SLOWPOKE'],items['ITEM_NONE']),(species['SPECIES_XATU'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_LUNATONE'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_SOLROCK'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_TateAndLiza5'] = [(species['SPECIES_HYPNO'],items['ITEM_NONE']),(species['SPECIES_CLAYDOL'],items['ITEM_NONE']),(species['SPECIES_SLOWKING'],items['ITEM_NONE']),(species['SPECIES_XATU'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_LUNATONE'],items['ITEM_CHESTO_BERRY']),(species['SPECIES_SOLROCK'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Vanessa'] = [(species['SPECIES_PIKACHU'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Victor'] = [(species['SPECIES_TAILLOW'],items['ITEM_ORAN_BERRY']),(species['SPECIES_ZIGZAGOON'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Victoria'] = [(species['SPECIES_ROSELIA'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Wallace'] = [(species['SPECIES_WAILORD'],items['ITEM_NONE']),(species['SPECIES_TENTACRUEL'],items['ITEM_NONE']),(species['SPECIES_LUDICOLO'],items['ITEM_NONE']),(species['SPECIES_WHISCASH'],items['ITEM_NONE']),(species['SPECIES_GYARADOS'],items['ITEM_NONE']),(species['SPECIES_MILOTIC'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Wattson1'] = [(species['SPECIES_VOLTORB'],items['ITEM_NONE']),(species['SPECIES_ELECTRIKE'],items['ITEM_NONE']),(species['SPECIES_MAGNETON'],items['ITEM_NONE']),(species['SPECIES_MANECTRIC'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Wattson2'] = [(species['SPECIES_MAREEP'],items['ITEM_NONE']),(species['SPECIES_ELECTRODE'],items['ITEM_NONE']),(species['SPECIES_MAGNETON'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MANECTRIC'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Wattson3'] = [(species['SPECIES_PIKACHU'],items['ITEM_NONE']),(species['SPECIES_FLAAFFY'],items['ITEM_NONE']),(species['SPECIES_ELECTRODE'],items['ITEM_NONE']),(species['SPECIES_MAGNETON'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MANECTRIC'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Wattson4'] = [(species['SPECIES_RAICHU'],items['ITEM_NONE']),(species['SPECIES_AMPHAROS'],items['ITEM_NONE']),(species['SPECIES_ELECTRODE'],items['ITEM_NONE']),(species['SPECIES_MAGNETON'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MANECTRIC'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Wattson5'] = [(species['SPECIES_ELECTABUZZ'],items['ITEM_NONE']),(species['SPECIES_RAICHU'],items['ITEM_NONE']),(species['SPECIES_AMPHAROS'],items['ITEM_NONE']),(species['SPECIES_ELECTRODE'],items['ITEM_NONE']),(species['SPECIES_MAGNETON'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_MANECTRIC'],items['ITEM_SITRUS_BERRY'])]
foe_item_labels['sParty_Winona1'] = [(species['SPECIES_SWABLU'],items['ITEM_NONE']),(species['SPECIES_TROPIUS'],items['ITEM_NONE']),(species['SPECIES_PELIPPER'],items['ITEM_NONE']),(species['SPECIES_SKARMORY'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_ORAN_BERRY'])]
foe_item_labels['sParty_Winona2'] = [(species['SPECIES_DRATINI'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_TROPIUS'],items['ITEM_NONE']),(species['SPECIES_PELIPPER'],items['ITEM_NONE']),(species['SPECIES_SKARMORY'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Winona3'] = [(species['SPECIES_HOOTHOOT'],items['ITEM_NONE']),(species['SPECIES_TROPIUS'],items['ITEM_NONE']),(species['SPECIES_DRAGONAIR'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_PELIPPER'],items['ITEM_NONE']),(species['SPECIES_SKARMORY'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Winona4'] = [(species['SPECIES_NOCTOWL'],items['ITEM_NONE']),(species['SPECIES_TROPIUS'],items['ITEM_NONE']),(species['SPECIES_DRAGONAIR'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_PELIPPER'],items['ITEM_NONE']),(species['SPECIES_SKARMORY'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Winona5'] = [(species['SPECIES_NOCTOWL'],items['ITEM_NONE']),(species['SPECIES_TROPIUS'],items['ITEM_NONE']),(species['SPECIES_PELIPPER'],items['ITEM_NONE']),(species['SPECIES_DRAGONITE'],items['ITEM_SITRUS_BERRY']),(species['SPECIES_SKARMORY'],items['ITEM_NONE']),(species['SPECIES_ALTARIA'],items['ITEM_CHESTO_BERRY'])]
foe_item_labels['sParty_Winston1'] = [(species['SPECIES_ZIGZAGOON'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Winston2'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Winston3'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Winston4'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]
foe_item_labels['sParty_Winston5'] = [(species['SPECIES_LINOONE'],items['ITEM_NUGGET'])]

foe_labels = {}
foe_labels['sParty_Aaron'] = [species['SPECIES_BAGON']]
foe_labels['sParty_Abigail1'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Abigail2'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Abigail3'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Abigail4'] = [species['SPECIES_MAGNETON']]
foe_labels['sParty_Abigail5'] = [species['SPECIES_MAGNETON']]
foe_labels['sParty_Aidan'] = [species['SPECIES_SWELLOW'],species['SPECIES_SKARMORY']]
foe_labels['sParty_Aisha'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Alan'] = [species['SPECIES_GEODUDE'],species['SPECIES_NOSEPASS'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Albert'] = [species['SPECIES_MAGNETON'],species['SPECIES_MUK']]
foe_labels['sParty_Alberto'] = [species['SPECIES_PELIPPER'],species['SPECIES_XATU']]
foe_labels['sParty_Alex'] = [species['SPECIES_NATU'],species['SPECIES_SWELLOW']]
foe_labels['sParty_Alexa'] = [species['SPECIES_GLOOM'],species['SPECIES_AZUMARILL']]
foe_labels['sParty_Alexis'] = [species['SPECIES_KIRLIA'],species['SPECIES_XATU']]
foe_labels['sParty_Alice'] = [species['SPECIES_GOLDEEN'],species['SPECIES_WINGULL'],species['SPECIES_GOLDEEN']]
foe_labels['sParty_Alix'] = [species['SPECIES_KADABRA'],species['SPECIES_KIRLIA']]
foe_labels['sParty_Allen'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_TAILLOW']]
foe_labels['sParty_Allison'] = [species['SPECIES_WINGULL'],species['SPECIES_STARYU']]
foe_labels['sParty_Alvaro'] = [species['SPECIES_BANETTE'],species['SPECIES_KADABRA']]
foe_labels['sParty_Alyssa'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_AmyAndLiv1'] = [species['SPECIES_PLUSLE'],species['SPECIES_MINUN']]
foe_labels['sParty_AmyAndLiv2'] = [species['SPECIES_PLUSLE'],species['SPECIES_MINUN']]
foe_labels['sParty_AmyAndLiv3'] = [species['SPECIES_PLUSLE'],species['SPECIES_MINUN']]
foe_labels['sParty_AmyAndLiv4'] = [species['SPECIES_PLUSLE'],species['SPECIES_MINUN']]
foe_labels['sParty_AmyAndLiv5'] = [species['SPECIES_PLUSLE'],species['SPECIES_MINUN']]
foe_labels['sParty_AmyAndLiv6'] = [species['SPECIES_PLUSLE'],species['SPECIES_MINUN']]
foe_labels['sParty_Anabel'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_Andrea'] = [species['SPECIES_LUVDISC']]
foe_labels['sParty_Andres1'] = [species['SPECIES_SANDSHREW'],species['SPECIES_SANDSHREW']]
foe_labels['sParty_Andres2'] = [species['SPECIES_SANDSHREW'],species['SPECIES_SANDSHREW']]
foe_labels['sParty_Andres3'] = [species['SPECIES_NOSEPASS'],species['SPECIES_SANDSHREW'],species['SPECIES_SANDSHREW']]
foe_labels['sParty_Andres4'] = [species['SPECIES_NOSEPASS'],species['SPECIES_SANDSHREW'],species['SPECIES_SANDSHREW']]
foe_labels['sParty_Andres5'] = [species['SPECIES_NOSEPASS'],species['SPECIES_SANDSLASH'],species['SPECIES_SANDSLASH']]
foe_labels['sParty_Andrew'] = [species['SPECIES_MAGIKARP'],species['SPECIES_TENTACOOL'],species['SPECIES_MAGIKARP']]
foe_labels['sParty_Angelica'] = [species['SPECIES_CASTFORM']]
foe_labels['sParty_Angelina'] = [species['SPECIES_LOMBRE'],species['SPECIES_MARILL']]
foe_labels['sParty_AnnaAndMeg1'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_AnnaAndMeg2'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_AnnaAndMeg3'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_AnnaAndMeg4'] = [species['SPECIES_LINOONE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_AnnaAndMeg5'] = [species['SPECIES_LINOONE'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Anthony'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Archie'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_CROBAT'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_Ashley'] = [species['SPECIES_SWABLU'],species['SPECIES_SWABLU'],species['SPECIES_SWABLU']]
foe_labels['sParty_Atsushi'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Auron'] = [species['SPECIES_MANECTRIC'],species['SPECIES_MACHAMP']]
foe_labels['sParty_Austina'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Autumn'] = [species['SPECIES_SHROOMISH']]
foe_labels['sParty_Axle'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Barny'] = [species['SPECIES_TENTACOOL'],species['SPECIES_CARVANHA']]
foe_labels['sParty_Barry'] = [species['SPECIES_GYARADOS']]
foe_labels['sParty_Beau'] = [species['SPECIES_BALTOY'],species['SPECIES_SANDSHREW'],species['SPECIES_BALTOY']]
foe_labels['sParty_Beck'] = [species['SPECIES_TROPIUS']]
foe_labels['sParty_Becky'] = [species['SPECIES_SANDSHREW'],species['SPECIES_MARILL']]
foe_labels['sParty_Ben'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_GULPIN']]
foe_labels['sParty_Benjamin1'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Benjamin2'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Benjamin3'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Benjamin4'] = [species['SPECIES_MAGNETON']]
foe_labels['sParty_Benjamin5'] = [species['SPECIES_MAGNETON']]
foe_labels['sParty_Benny'] = [species['SPECIES_SWELLOW'],species['SPECIES_PELIPPER'],species['SPECIES_XATU']]
foe_labels['sParty_Bernie1'] = [species['SPECIES_SLUGMA'],species['SPECIES_WINGULL']]
foe_labels['sParty_Bernie2'] = [species['SPECIES_SLUGMA'],species['SPECIES_WINGULL']]
foe_labels['sParty_Bernie3'] = [species['SPECIES_SLUGMA'],species['SPECIES_PELIPPER']]
foe_labels['sParty_Bernie4'] = [species['SPECIES_SLUGMA'],species['SPECIES_PELIPPER']]
foe_labels['sParty_Bernie5'] = [species['SPECIES_MAGCARGO'],species['SPECIES_PELIPPER']]
foe_labels['sParty_Beth'] = [species['SPECIES_GOLDEEN']]
foe_labels['sParty_Beverly'] = [species['SPECIES_WINGULL'],species['SPECIES_WAILMER']]
foe_labels['sParty_Bianca'] = [species['SPECIES_SHROOMISH']]
foe_labels['sParty_Billy'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_SEEDOT']]
foe_labels['sParty_Blake'] = [species['SPECIES_GIRAFARIG']]
foe_labels['sParty_Branden'] = [species['SPECIES_TAILLOW'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Brandi'] = [species['SPECIES_RALTS']]
foe_labels['sParty_Brandon'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_Braxton'] = [species['SPECIES_SWELLOW'],species['SPECIES_TRAPINCH'],species['SPECIES_WAILMER'],species['SPECIES_MAGNETON'],species['SPECIES_SHIFTRY']]
foe_labels['sParty_Brenda'] = [species['SPECIES_GOLDEEN']]
foe_labels['sParty_BrendanLilycoveMudkip'] = [species['SPECIES_TROPIUS'],species['SPECIES_SLUGMA'],species['SPECIES_PELIPPER'],species['SPECIES_GROVYLE']]
foe_labels['sParty_BrendanLilycoveTorchic'] = [species['SPECIES_TROPIUS'],species['SPECIES_LUDICOLO'],species['SPECIES_SLUGMA'],species['SPECIES_MARSHTOMP']]
foe_labels['sParty_BrendanLilycoveTreecko'] = [species['SPECIES_TROPIUS'],species['SPECIES_PELIPPER'],species['SPECIES_LUDICOLO'],species['SPECIES_COMBUSKEN']]
foe_labels['sParty_BrendanLinkPlaceholder'] = [species['SPECIES_GROUDON']]
foe_labels['sParty_BrendanRoute103Mudkip'] = [species['SPECIES_TREECKO']]
foe_labels['sParty_BrendanRoute103Torchic'] = [species['SPECIES_MUDKIP']]
foe_labels['sParty_BrendanRoute103Treecko'] = [species['SPECIES_TORCHIC']]
foe_labels['sParty_BrendanRoute110Mudkip'] = [species['SPECIES_SLUGMA'],species['SPECIES_WINGULL'],species['SPECIES_GROVYLE']]
foe_labels['sParty_BrendanRoute110Torchic'] = [species['SPECIES_LOMBRE'],species['SPECIES_SLUGMA'],species['SPECIES_MARSHTOMP']]
foe_labels['sParty_BrendanRoute110Treecko'] = [species['SPECIES_WINGULL'],species['SPECIES_LOMBRE'],species['SPECIES_COMBUSKEN']]
foe_labels['sParty_BrendanRoute119Mudkip'] = [species['SPECIES_SLUGMA'],species['SPECIES_PELIPPER'],species['SPECIES_GROVYLE']]
foe_labels['sParty_BrendanRoute119Torchic'] = [species['SPECIES_LOMBRE'],species['SPECIES_SLUGMA'],species['SPECIES_MARSHTOMP']]
foe_labels['sParty_BrendanRoute119Treecko'] = [species['SPECIES_PELIPPER'],species['SPECIES_LOMBRE'],species['SPECIES_COMBUSKEN']]
foe_labels['sParty_BrendanRustboroMudkip'] = [species['SPECIES_WINGULL'],species['SPECIES_TREECKO']]
foe_labels['sParty_BrendanRustboroTorchic'] = [species['SPECIES_SLUGMA'],species['SPECIES_MUDKIP']]
foe_labels['sParty_BrendanRustboroTreecko'] = [species['SPECIES_LOTAD'],species['SPECIES_TORCHIC']]
foe_labels['sParty_Brenden'] = [species['SPECIES_MACHOP']]
foe_labels['sParty_Brent'] = [species['SPECIES_SURSKIT']]
foe_labels['sParty_Brice'] = [species['SPECIES_NUMEL'],species['SPECIES_MACHOP']]
foe_labels['sParty_Bridget'] = [species['SPECIES_AZUMARILL']]
foe_labels['sParty_Brooke1'] = [species['SPECIES_WINGULL'],species['SPECIES_NUMEL'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Brooke2'] = [species['SPECIES_WINGULL'],species['SPECIES_NUMEL'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Brooke3'] = [species['SPECIES_PELIPPER'],species['SPECIES_NUMEL'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Brooke4'] = [species['SPECIES_PELIPPER'],species['SPECIES_NUMEL'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Brooke5'] = [species['SPECIES_PELIPPER'],species['SPECIES_CAMERUPT'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Bryan'] = [species['SPECIES_SANDSHREW'],species['SPECIES_SANDSLASH']]
foe_labels['sParty_Bryant'] = [species['SPECIES_NUMEL'],species['SPECIES_SLUGMA']]
foe_labels['sParty_Cale'] = [species['SPECIES_DUSTOX'],species['SPECIES_BEAUTIFLY']]
foe_labels['sParty_Callie'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Calvin1'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_Calvin2'] = [species['SPECIES_MIGHTYENA']]
foe_labels['sParty_Calvin3'] = [species['SPECIES_SWELLOW'],species['SPECIES_MIGHTYENA']]
foe_labels['sParty_Calvin4'] = [species['SPECIES_SWELLOW'],species['SPECIES_LINOONE'],species['SPECIES_MIGHTYENA']]
foe_labels['sParty_Calvin5'] = [species['SPECIES_SWELLOW'],species['SPECIES_LINOONE'],species['SPECIES_MIGHTYENA']]
foe_labels['sParty_Camden'] = [species['SPECIES_STARYU'],species['SPECIES_STARYU']]
foe_labels['sParty_Cameron1'] = [species['SPECIES_SOLROCK']]
foe_labels['sParty_Cameron2'] = [species['SPECIES_KADABRA'],species['SPECIES_SOLROCK']]
foe_labels['sParty_Cameron3'] = [species['SPECIES_KADABRA'],species['SPECIES_SOLROCK']]
foe_labels['sParty_Cameron4'] = [species['SPECIES_KADABRA'],species['SPECIES_SOLROCK']]
foe_labels['sParty_Cameron5'] = [species['SPECIES_SOLROCK'],species['SPECIES_ALAKAZAM']]
foe_labels['sParty_Camron'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Carlee'] = [species['SPECIES_SEAKING']]
foe_labels['sParty_Carol'] = [species['SPECIES_TAILLOW'],species['SPECIES_LOMBRE']]
foe_labels['sParty_Carolina'] = [species['SPECIES_MANECTRIC'],species['SPECIES_SWELLOW'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Caroline'] = [species['SPECIES_SKARMORY'],species['SPECIES_SABLEYE']]
foe_labels['sParty_Carter'] = [species['SPECIES_WAILMER'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Catherine1'] = [species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Catherine2'] = [species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Catherine3'] = [species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Catherine4'] = [species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Catherine5'] = [species['SPECIES_BELLOSSOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Cedric'] = [species['SPECIES_WOBBUFFET']]
foe_labels['sParty_Celia'] = [species['SPECIES_MARILL'],species['SPECIES_LOMBRE']]
foe_labels['sParty_Celina'] = [species['SPECIES_ROSELIA']]
foe_labels['sParty_Chad'] = [species['SPECIES_TENTACOOL'],species['SPECIES_WAILMER']]
foe_labels['sParty_Chandler'] = [species['SPECIES_TENTACOOL'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Charlie'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Charlotte'] = [species['SPECIES_NUZLEAF']]
foe_labels['sParty_Chase'] = [species['SPECIES_WINGULL'],species['SPECIES_STARYU']]
foe_labels['sParty_Chester'] = [species['SPECIES_TAILLOW'],species['SPECIES_SWELLOW']]
foe_labels['sParty_Chip'] = [species['SPECIES_BALTOY'],species['SPECIES_SANDSHREW'],species['SPECIES_SANDSLASH']]
foe_labels['sParty_Chris'] = [species['SPECIES_MAGIKARP'],species['SPECIES_TENTACOOL'],species['SPECIES_FEEBAS'],species['SPECIES_CARVANHA']]
foe_labels['sParty_Clarence'] = [species['SPECIES_SHARPEDO']]
foe_labels['sParty_Clarissa'] = [species['SPECIES_ROSELIA'],species['SPECIES_WAILMER']]
foe_labels['sParty_Clark'] = [species['SPECIES_GEODUDE']]
foe_labels['sParty_Claude'] = [species['SPECIES_MAGIKARP'],species['SPECIES_GOLDEEN'],species['SPECIES_BARBOACH']]
foe_labels['sParty_Clifford'] = [species['SPECIES_GIRAFARIG']]
foe_labels['sParty_Coby'] = [species['SPECIES_SKARMORY'],species['SPECIES_SWELLOW']]
foe_labels['sParty_Cole'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Colin'] = [species['SPECIES_WINGULL'],species['SPECIES_NATU']]
foe_labels['sParty_Connie'] = [species['SPECIES_GOLDEEN']]
foe_labels['sParty_Conor'] = [species['SPECIES_CHINCHOU'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Cora'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Cory1'] = [species['SPECIES_WINGULL'],species['SPECIES_MACHOP'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Cory2'] = [species['SPECIES_WINGULL'],species['SPECIES_MACHOP'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Cory3'] = [species['SPECIES_PELIPPER'],species['SPECIES_MACHOP'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Cory4'] = [species['SPECIES_PELIPPER'],species['SPECIES_MACHOP'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Cory5'] = [species['SPECIES_PELIPPER'],species['SPECIES_MACHOKE'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Crissy'] = [species['SPECIES_GOLDEEN'],species['SPECIES_WAILMER']]
foe_labels['sParty_Cristian'] = [species['SPECIES_MAKUHITA']]
foe_labels['sParty_Cristin1'] = [species['SPECIES_LOUDRED'],species['SPECIES_VIGOROTH']]
foe_labels['sParty_Cristin2'] = [species['SPECIES_LOUDRED'],species['SPECIES_VIGOROTH']]
foe_labels['sParty_Cristin3'] = [species['SPECIES_SPINDA'],species['SPECIES_LOUDRED'],species['SPECIES_VIGOROTH']]
foe_labels['sParty_Cristin4'] = [species['SPECIES_SPINDA'],species['SPECIES_LOUDRED'],species['SPECIES_VIGOROTH']]
foe_labels['sParty_Cristin5'] = [species['SPECIES_SPINDA'],species['SPECIES_EXPLOUD'],species['SPECIES_SLAKING']]
foe_labels['sParty_Cyndy1'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Cyndy2'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Cyndy3'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Cyndy4'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Cyndy5'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Daisuke'] = [species['SPECIES_MACHOP']]
foe_labels['sParty_Daisy'] = [species['SPECIES_SHROOMISH'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Dale'] = [species['SPECIES_TENTACOOL'],species['SPECIES_WAILMER'],species['SPECIES_TENTACOOL'],species['SPECIES_WAILMER']]
foe_labels['sParty_Dalton1'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_WHISMUR']]
foe_labels['sParty_Dalton2'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_WHISMUR'],species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Dalton3'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_LOUDRED'],species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Dalton4'] = [species['SPECIES_MAGNETON'],species['SPECIES_LOUDRED'],species['SPECIES_MAGNETON']]
foe_labels['sParty_Dalton5'] = [species['SPECIES_MAGNETON'],species['SPECIES_EXPLOUD'],species['SPECIES_MAGNETON']]
foe_labels['sParty_Dana'] = [species['SPECIES_AZUMARILL']]
foe_labels['sParty_Danielle'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Darcy'] = [species['SPECIES_PELIPPER'],species['SPECIES_CAMERUPT']]
foe_labels['sParty_Darian'] = [species['SPECIES_MAGIKARP']]
foe_labels['sParty_Darius'] = [species['SPECIES_TROPIUS']]
foe_labels['sParty_Darrin'] = [species['SPECIES_TENTACOOL'],species['SPECIES_WINGULL'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_David'] = [species['SPECIES_TENTACOOL'],species['SPECIES_CARVANHA']]
foe_labels['sParty_Davis'] = [species['SPECIES_PINSIR']]
foe_labels['sParty_Dayton'] = [species['SPECIES_SLUGMA'],species['SPECIES_NUMEL']]
foe_labels['sParty_Dean'] = [species['SPECIES_CARVANHA'],species['SPECIES_WINGULL'],species['SPECIES_CARVANHA']]
foe_labels['sParty_Deandre'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_ARON'],species['SPECIES_ELECTRIKE']]
foe_labels['sParty_Debra'] = [species['SPECIES_SEAKING']]
foe_labels['sParty_Declan'] = [species['SPECIES_GYARADOS']]
foe_labels['sParty_Demetrius'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_ELECTRIKE']]
foe_labels['sParty_Denise'] = [species['SPECIES_WINGULL'],species['SPECIES_GOLDEEN']]
foe_labels['sParty_Derek'] = [species['SPECIES_DUSTOX'],species['SPECIES_BEAUTIFLY']]
foe_labels['sParty_Devan'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE']]
foe_labels['sParty_DezAndLuke'] = [species['SPECIES_DELCATTY'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Diana1'] = [species['SPECIES_SHROOMISH'],species['SPECIES_ODDISH'],species['SPECIES_SWABLU']]
foe_labels['sParty_Diana2'] = [species['SPECIES_SHROOMISH'],species['SPECIES_GLOOM'],species['SPECIES_SWABLU']]
foe_labels['sParty_Diana3'] = [species['SPECIES_BRELOOM'],species['SPECIES_GLOOM'],species['SPECIES_SWABLU']]
foe_labels['sParty_Diana4'] = [species['SPECIES_BRELOOM'],species['SPECIES_GLOOM'],species['SPECIES_SWABLU']]
foe_labels['sParty_Diana5'] = [species['SPECIES_BRELOOM'],species['SPECIES_VILEPLUME'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Dillon'] = [species['SPECIES_ARON']]
foe_labels['sParty_Dominik'] = [species['SPECIES_TENTACOOL']]
foe_labels['sParty_Donald'] = [species['SPECIES_WURMPLE'],species['SPECIES_SILCOON'],species['SPECIES_BEAUTIFLY']]
foe_labels['sParty_Donny'] = [species['SPECIES_WINGULL'],species['SPECIES_STARYU']]
foe_labels['sParty_Doug'] = [species['SPECIES_NINCADA'],species['SPECIES_NINJASK']]
foe_labels['sParty_Douglas'] = [species['SPECIES_TENTACOOL'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Drew'] = [species['SPECIES_SANDSHREW']]
foe_labels['sParty_Dudley'] = [species['SPECIES_TENTACOOL'],species['SPECIES_WINGULL'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Duncan'] = [species['SPECIES_SPHEAL'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Dusty1'] = [species['SPECIES_SANDSLASH']]
foe_labels['sParty_Dusty2'] = [species['SPECIES_SANDSLASH']]
foe_labels['sParty_Dusty3'] = [species['SPECIES_SANDSLASH']]
foe_labels['sParty_Dusty4'] = [species['SPECIES_SANDSLASH']]
foe_labels['sParty_Dusty5'] = [species['SPECIES_SANDSLASH']]
foe_labels['sParty_Dwayne'] = [species['SPECIES_WINGULL'],species['SPECIES_MACHOP'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Dylan1'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Dylan2'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Dylan3'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Dylan4'] = [species['SPECIES_DODRIO']]
foe_labels['sParty_Dylan5'] = [species['SPECIES_DODRIO']]
foe_labels['sParty_Ed'] = [species['SPECIES_ZANGOOSE'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Eddie'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_ZIGZAGOON']]
foe_labels['sParty_Edgar'] = [species['SPECIES_CACTURNE'],species['SPECIES_PELIPPER']]
foe_labels['sParty_Edmond'] = [species['SPECIES_WINGULL']]
foe_labels['sParty_Edward'] = [species['SPECIES_ABRA']]
foe_labels['sParty_Edwardo'] = [species['SPECIES_DODUO'],species['SPECIES_PELIPPER']]
foe_labels['sParty_Edwin1'] = [species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Edwin2'] = [species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Edwin3'] = [species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Edwin4'] = [species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Edwin5'] = [species['SPECIES_LUDICOLO'],species['SPECIES_SHIFTRY']]
foe_labels['sParty_Eli'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Elijah'] = [species['SPECIES_SKARMORY'],species['SPECIES_SKARMORY']]
foe_labels['sParty_Elliot1'] = [species['SPECIES_MAGIKARP'],species['SPECIES_TENTACOOL'],species['SPECIES_MAGIKARP']]
foe_labels['sParty_Elliot2'] = [species['SPECIES_TENTACOOL'],species['SPECIES_GYARADOS'],species['SPECIES_GYARADOS']]
foe_labels['sParty_Elliot3'] = [species['SPECIES_GYARADOS'],species['SPECIES_CARVANHA'],species['SPECIES_TENTACOOL'],species['SPECIES_GYARADOS']]
foe_labels['sParty_Elliot4'] = [species['SPECIES_GYARADOS'],species['SPECIES_CARVANHA'],species['SPECIES_TENTACRUEL'],species['SPECIES_GYARADOS']]
foe_labels['sParty_Elliot5'] = [species['SPECIES_GYARADOS'],species['SPECIES_SHARPEDO'],species['SPECIES_GYARADOS'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Eric'] = [species['SPECIES_GEODUDE'],species['SPECIES_BALTOY']]
foe_labels['sParty_Ernest1'] = [species['SPECIES_WINGULL'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Ernest2'] = [species['SPECIES_WINGULL'],species['SPECIES_TENTACOOL'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Ernest3'] = [species['SPECIES_PELIPPER'],species['SPECIES_TENTACOOL'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Ernest4'] = [species['SPECIES_PELIPPER'],species['SPECIES_TENTACOOL'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Ernest5'] = [species['SPECIES_PELIPPER'],species['SPECIES_MACHOKE'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Ethan1'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_TAILLOW']]
foe_labels['sParty_Ethan2'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_TAILLOW']]
foe_labels['sParty_Ethan3'] = [species['SPECIES_LINOONE'],species['SPECIES_SWELLOW']]
foe_labels['sParty_Ethan4'] = [species['SPECIES_SANDSHREW'],species['SPECIES_SWELLOW'],species['SPECIES_LINOONE']]
foe_labels['sParty_Ethan5'] = [species['SPECIES_SWELLOW'],species['SPECIES_SANDSLASH'],species['SPECIES_LINOONE']]
foe_labels['sParty_Everett'] = [species['SPECIES_WOBBUFFET']]
foe_labels['sParty_Fabian'] = [species['SPECIES_MANECTRIC']]
foe_labels['sParty_Felix'] = [species['SPECIES_MEDICHAM'],species['SPECIES_CLAYDOL']]
foe_labels['sParty_Fernando1'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Fernando2'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_ELECTRIKE'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Fernando3'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_MANECTRIC'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Fernando4'] = [species['SPECIES_MANECTRIC'],species['SPECIES_MANECTRIC'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Fernando5'] = [species['SPECIES_MANECTRIC'],species['SPECIES_MANECTRIC'],species['SPECIES_EXPLOUD']]
foe_labels['sParty_Flint'] = [species['SPECIES_SWELLOW'],species['SPECIES_XATU']]
foe_labels['sParty_Foster'] = [species['SPECIES_SANDSHREW'],species['SPECIES_SANDSLASH']]
foe_labels['sParty_Franklin'] = [species['SPECIES_SEALEO']]
foe_labels['sParty_Fredrick'] = [species['SPECIES_MAKUHITA'],species['SPECIES_MACHOKE']]
foe_labels['sParty_GabbyAndTy1'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_WHISMUR']]
foe_labels['sParty_GabbyAndTy2'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_LOUDRED']]
foe_labels['sParty_GabbyAndTy3'] = [species['SPECIES_MAGNETON'],species['SPECIES_LOUDRED']]
foe_labels['sParty_GabbyAndTy4'] = [species['SPECIES_MAGNETON'],species['SPECIES_LOUDRED']]
foe_labels['sParty_GabbyAndTy5'] = [species['SPECIES_MAGNETON'],species['SPECIES_LOUDRED']]
foe_labels['sParty_GabbyAndTy6'] = [species['SPECIES_MAGNETON'],species['SPECIES_EXPLOUD']]
foe_labels['sParty_Gabrielle1'] = [species['SPECIES_SKITTY'],species['SPECIES_POOCHYENA'],species['SPECIES_ZIGZAGOON'],species['SPECIES_LOTAD'],species['SPECIES_SEEDOT'],species['SPECIES_TAILLOW']]
foe_labels['sParty_Gabrielle2'] = [species['SPECIES_SKITTY'],species['SPECIES_MIGHTYENA'],species['SPECIES_ZIGZAGOON'],species['SPECIES_LOTAD'],species['SPECIES_SEEDOT'],species['SPECIES_TAILLOW']]
foe_labels['sParty_Gabrielle3'] = [species['SPECIES_SKITTY'],species['SPECIES_MIGHTYENA'],species['SPECIES_LINOONE'],species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF'],species['SPECIES_TAILLOW']]
foe_labels['sParty_Gabrielle4'] = [species['SPECIES_DELCATTY'],species['SPECIES_MIGHTYENA'],species['SPECIES_LINOONE'],species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF'],species['SPECIES_SWELLOW']]
foe_labels['sParty_Gabrielle5'] = [species['SPECIES_DELCATTY'],species['SPECIES_MIGHTYENA'],species['SPECIES_LINOONE'],species['SPECIES_LUDICOLO'],species['SPECIES_SHIFTRY'],species['SPECIES_SWELLOW']]
foe_labels['sParty_Garrison'] = [species['SPECIES_SANDSLASH']]
foe_labels['sParty_Georgia'] = [species['SPECIES_SHROOMISH'],species['SPECIES_BEAUTIFLY']]
foe_labels['sParty_Gerald'] = [species['SPECIES_KECLEON']]
foe_labels['sParty_Gilbert'] = [species['SPECIES_SHARPEDO']]
foe_labels['sParty_GinaAndMia1'] = [species['SPECIES_SEEDOT'],species['SPECIES_LOTAD']]
foe_labels['sParty_GinaAndMia2'] = [species['SPECIES_DUSKULL'],species['SPECIES_SHROOMISH']]
foe_labels['sParty_Grace'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Greg'] = [species['SPECIES_VOLBEAT'],species['SPECIES_ILLUMISE']]
foe_labels['sParty_Greta'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_GruntAquaHideout1'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntAquaHideout2'] = [species['SPECIES_ZUBAT'],species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntAquaHideout3'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntAquaHideout4'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntAquaHideout5'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntAquaHideout6'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntAquaHideout7'] = [species['SPECIES_POOCHYENA'],species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntAquaHideout8'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntJaggedPass'] = [species['SPECIES_POOCHYENA'],species['SPECIES_NUMEL']]
foe_labels['sParty_GruntMagmaHideout1'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMagmaHideout10'] = [species['SPECIES_MIGHTYENA']]
foe_labels['sParty_GruntMagmaHideout11'] = [species['SPECIES_BALTOY']]
foe_labels['sParty_GruntMagmaHideout12'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_GruntMagmaHideout13'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMagmaHideout14'] = [species['SPECIES_MIGHTYENA']]
foe_labels['sParty_GruntMagmaHideout15'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_GruntMagmaHideout16'] = [species['SPECIES_BALTOY']]
foe_labels['sParty_GruntMagmaHideout2'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntMagmaHideout3'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_GruntMagmaHideout4'] = [species['SPECIES_BALTOY'],species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMagmaHideout5'] = [species['SPECIES_BALTOY'],species['SPECIES_NUMEL']]
foe_labels['sParty_GruntMagmaHideout6'] = [species['SPECIES_MIGHTYENA']]
foe_labels['sParty_GruntMagmaHideout7'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMagmaHideout8'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntMagmaHideout9'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMtChimney1'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_GruntMtChimney2'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMtPyre1'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMtPyre2'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntMtPyre3'] = [species['SPECIES_POOCHYENA'],species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntMtPyre4'] = [species['SPECIES_WAILMER'],species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntMuseum1'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntMuseum2'] = [species['SPECIES_ZUBAT'],species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntPetalburgWoods'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntRusturfTunnel'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntSeafloorCavern1'] = [species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntSeafloorCavern2'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntSeafloorCavern3'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntSeafloorCavern4'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntSeafloorCavern5'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_GOLBAT']]
foe_labels['sParty_GruntSpaceCenter1'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_GruntSpaceCenter2'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_MIGHTYENA'],species['SPECIES_NUMEL']]
foe_labels['sParty_GruntSpaceCenter3'] = [species['SPECIES_ZUBAT'],species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntSpaceCenter4'] = [species['SPECIES_BALTOY']]
foe_labels['sParty_GruntSpaceCenter5'] = [species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntSpaceCenter6'] = [species['SPECIES_MIGHTYENA']]
foe_labels['sParty_GruntSpaceCenter7'] = [species['SPECIES_BALTOY']]
foe_labels['sParty_GruntUnused'] = [species['SPECIES_WAILMER'],species['SPECIES_ZUBAT']]
foe_labels['sParty_GruntWeatherInst1'] = [species['SPECIES_ZUBAT'],species['SPECIES_POOCHYENA']]
foe_labels['sParty_GruntWeatherInst2'] = [species['SPECIES_POOCHYENA'],species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntWeatherInst3'] = [species['SPECIES_POOCHYENA'],species['SPECIES_ZUBAT'],species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntWeatherInst4'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_GruntWeatherInst5'] = [species['SPECIES_ZUBAT'],species['SPECIES_POOCHYENA']]
foe_labels['sParty_Gwen'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Hailey'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Haley1'] = [species['SPECIES_LOTAD'],species['SPECIES_SHROOMISH']]
foe_labels['sParty_Haley2'] = [species['SPECIES_LOMBRE'],species['SPECIES_SHROOMISH']]
foe_labels['sParty_Haley3'] = [species['SPECIES_LOMBRE'],species['SPECIES_BRELOOM']]
foe_labels['sParty_Haley4'] = [species['SPECIES_LOMBRE'],species['SPECIES_BRELOOM']]
foe_labels['sParty_Haley5'] = [species['SPECIES_SWELLOW'],species['SPECIES_LOMBRE'],species['SPECIES_BRELOOM']]
foe_labels['sParty_Halle'] = [species['SPECIES_SABLEYE'],species['SPECIES_ABSOL']]
foe_labels['sParty_Hannah'] = [species['SPECIES_KIRLIA']]
foe_labels['sParty_Harrison'] = [species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Hayden'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Hector'] = [species['SPECIES_ZANGOOSE'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Heidi'] = [species['SPECIES_SANDSHREW'],species['SPECIES_BALTOY']]
foe_labels['sParty_Helene'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Henry'] = [species['SPECIES_CARVANHA'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Herman'] = [species['SPECIES_WINGULL'],species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Hideo'] = [species['SPECIES_KOFFING'],species['SPECIES_KOFFING']]
foe_labels['sParty_Hitoshi'] = [species['SPECIES_MACHOP'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Hope'] = [species['SPECIES_ROSELIA']]
foe_labels['sParty_Hudson'] = [species['SPECIES_WAILMER']]
foe_labels['sParty_Huey'] = [species['SPECIES_WINGULL'],species['SPECIES_MACHOP']]
foe_labels['sParty_Hugh'] = [species['SPECIES_WINGULL'],species['SPECIES_TROPIUS']]
foe_labels['sParty_Humberto'] = [species['SPECIES_SKARMORY']]
foe_labels['sParty_Imani'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Irene'] = [species['SPECIES_SHROOMISH'],species['SPECIES_MARILL']]
foe_labels['sParty_Isaac1'] = [species['SPECIES_WHISMUR'],species['SPECIES_ZIGZAGOON'],species['SPECIES_ARON'],species['SPECIES_POOCHYENA'],species['SPECIES_TAILLOW'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Isaac2'] = [species['SPECIES_LOUDRED'],species['SPECIES_LINOONE'],species['SPECIES_ARON'],species['SPECIES_MIGHTYENA'],species['SPECIES_SWELLOW'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Isaac3'] = [species['SPECIES_LOUDRED'],species['SPECIES_LINOONE'],species['SPECIES_ARON'],species['SPECIES_MIGHTYENA'],species['SPECIES_SWELLOW'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Isaac4'] = [species['SPECIES_LOUDRED'],species['SPECIES_LINOONE'],species['SPECIES_ARON'],species['SPECIES_MIGHTYENA'],species['SPECIES_SWELLOW'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Isaac5'] = [species['SPECIES_LOUDRED'],species['SPECIES_LINOONE'],species['SPECIES_LAIRON'],species['SPECIES_MIGHTYENA'],species['SPECIES_SWELLOW'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Isabella'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Isabelle'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Isaiah1'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Isaiah2'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Isaiah3'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Isaiah4'] = [species['SPECIES_STARMIE']]
foe_labels['sParty_Isaiah5'] = [species['SPECIES_STARMIE']]
foe_labels['sParty_Isobel'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Ivan'] = [species['SPECIES_MAGIKARP'],species['SPECIES_MAGIKARP'],species['SPECIES_MAGIKARP']]
foe_labels['sParty_Jace'] = [species['SPECIES_SLUGMA']]
foe_labels['sParty_Jack'] = [species['SPECIES_GYARADOS']]
foe_labels['sParty_Jacki1'] = [species['SPECIES_KADABRA'],species['SPECIES_LUNATONE']]
foe_labels['sParty_Jacki2'] = [species['SPECIES_KADABRA'],species['SPECIES_LUNATONE']]
foe_labels['sParty_Jacki3'] = [species['SPECIES_KADABRA'],species['SPECIES_LUNATONE']]
foe_labels['sParty_Jacki4'] = [species['SPECIES_KADABRA'],species['SPECIES_LUNATONE']]
foe_labels['sParty_Jacki5'] = [species['SPECIES_LUNATONE'],species['SPECIES_ALAKAZAM']]
foe_labels['sParty_Jackson1'] = [species['SPECIES_BRELOOM']]
foe_labels['sParty_Jackson2'] = [species['SPECIES_BRELOOM']]
foe_labels['sParty_Jackson3'] = [species['SPECIES_BRELOOM']]
foe_labels['sParty_Jackson4'] = [species['SPECIES_BRELOOM']]
foe_labels['sParty_Jackson5'] = [species['SPECIES_KECLEON'],species['SPECIES_BRELOOM']]
foe_labels['sParty_Jaclyn'] = [species['SPECIES_ABRA']]
foe_labels['sParty_Jacob'] = [species['SPECIES_VOLTORB'],species['SPECIES_VOLTORB'],species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Jaiden'] = [species['SPECIES_NINJASK'],species['SPECIES_GULPIN']]
foe_labels['sParty_James1'] = [species['SPECIES_NINCADA'],species['SPECIES_NINCADA']]
foe_labels['sParty_James2'] = [species['SPECIES_NINJASK']]
foe_labels['sParty_James3'] = [species['SPECIES_DUSTOX'],species['SPECIES_NINJASK']]
foe_labels['sParty_James4'] = [species['SPECIES_SURSKIT'],species['SPECIES_DUSTOX'],species['SPECIES_NINJASK']]
foe_labels['sParty_James5'] = [species['SPECIES_SURSKIT'],species['SPECIES_NINJASK'],species['SPECIES_DUSTOX'],species['SPECIES_NINJASK']]
foe_labels['sParty_Jani'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Janice'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Jared'] = [species['SPECIES_DODUO'],species['SPECIES_SKARMORY'],species['SPECIES_TROPIUS']]
foe_labels['sParty_Jasmine'] = [species['SPECIES_MAGNEMITE'],species['SPECIES_MAGNEMITE'],species['SPECIES_VOLTORB']]
foe_labels['sParty_Jaylen'] = [species['SPECIES_TRAPINCH']]
foe_labels['sParty_Jazmyn'] = [species['SPECIES_ABSOL']]
foe_labels['sParty_Jeff'] = [species['SPECIES_SLUGMA'],species['SPECIES_SLUGMA']]
foe_labels['sParty_Jeffrey1'] = [species['SPECIES_SURSKIT'],species['SPECIES_SURSKIT'],species['SPECIES_SURSKIT']]
foe_labels['sParty_Jeffrey2'] = [species['SPECIES_SURSKIT'],species['SPECIES_SURSKIT'],species['SPECIES_SURSKIT']]
foe_labels['sParty_Jeffrey3'] = [species['SPECIES_SURSKIT'],species['SPECIES_SURSKIT'],species['SPECIES_MASQUERAIN']]
foe_labels['sParty_Jeffrey4'] = [species['SPECIES_SURSKIT'],species['SPECIES_WURMPLE'],species['SPECIES_SURSKIT'],species['SPECIES_MASQUERAIN']]
foe_labels['sParty_Jenna'] = [species['SPECIES_LOTAD'],species['SPECIES_LOMBRE'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Jennifer'] = [species['SPECIES_SABLEYE']]
foe_labels['sParty_Jenny1'] = [species['SPECIES_WAILMER']]
foe_labels['sParty_Jenny2'] = [species['SPECIES_WAILMER']]
foe_labels['sParty_Jenny3'] = [species['SPECIES_WAILMER']]
foe_labels['sParty_Jenny4'] = [species['SPECIES_STARYU'],species['SPECIES_WAILMER']]
foe_labels['sParty_Jenny5'] = [species['SPECIES_LUVDISC'],species['SPECIES_WAILMER'],species['SPECIES_STARMIE']]
foe_labels['sParty_Jerome'] = [species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Jerry1'] = [species['SPECIES_RALTS']]
foe_labels['sParty_Jerry2'] = [species['SPECIES_RALTS'],species['SPECIES_MEDITITE']]
foe_labels['sParty_Jerry3'] = [species['SPECIES_KIRLIA'],species['SPECIES_MEDITITE']]
foe_labels['sParty_Jerry4'] = [species['SPECIES_KIRLIA'],species['SPECIES_MEDICHAM']]
foe_labels['sParty_Jerry5'] = [species['SPECIES_KIRLIA'],species['SPECIES_BANETTE'],species['SPECIES_MEDICHAM']]
foe_labels['sParty_Jessica1'] = [species['SPECIES_KECLEON'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Jessica2'] = [species['SPECIES_KECLEON'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Jessica3'] = [species['SPECIES_KECLEON'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Jessica4'] = [species['SPECIES_KECLEON'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Jessica5'] = [species['SPECIES_KECLEON'],species['SPECIES_SEVIPER']]
foe_labels['sParty_Jocelyn'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Joey'] = [species['SPECIES_MACHOP']]
foe_labels['sParty_Johanna'] = [species['SPECIES_GOLDEEN']]
foe_labels['sParty_JohnAndJay1'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_JohnAndJay2'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_JohnAndJay3'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_JohnAndJay4'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_JohnAndJay5'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Johnson'] = [species['SPECIES_SHROOMISH'],species['SPECIES_LOTAD']]
foe_labels['sParty_Jonah'] = [species['SPECIES_WAILMER'],species['SPECIES_TENTACOOL'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_Jonas'] = [species['SPECIES_KOFFING']]
foe_labels['sParty_Jonathan'] = [species['SPECIES_KECLEON'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Jose'] = [species['SPECIES_WURMPLE'],species['SPECIES_NINCADA']]
foe_labels['sParty_Joseph'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_VOLTORB']]
foe_labels['sParty_Josh'] = [species['SPECIES_GEODUDE']]
foe_labels['sParty_Joshua'] = [species['SPECIES_KADABRA'],species['SPECIES_SOLROCK']]
foe_labels['sParty_Josue'] = [species['SPECIES_TAILLOW'],species['SPECIES_WINGULL']]
foe_labels['sParty_Julie'] = [species['SPECIES_SANDSLASH'],species['SPECIES_NINETALES'],species['SPECIES_TROPIUS']]
foe_labels['sParty_Julio'] = [species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Justin'] = [species['SPECIES_KECLEON']]
foe_labels['sParty_Kai'] = [species['SPECIES_BARBOACH']]
foe_labels['sParty_Kara'] = [species['SPECIES_SEAKING']]
foe_labels['sParty_Karen1'] = [species['SPECIES_SHROOMISH']]
foe_labels['sParty_Karen2'] = [species['SPECIES_SHROOMISH'],species['SPECIES_WHISMUR']]
foe_labels['sParty_Karen3'] = [species['SPECIES_SHROOMISH'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Karen4'] = [species['SPECIES_BRELOOM'],species['SPECIES_LOUDRED']]
foe_labels['sParty_Karen5'] = [species['SPECIES_BRELOOM'],species['SPECIES_EXPLOUD']]
foe_labels['sParty_KateAndJoy'] = [species['SPECIES_SPINDA'],species['SPECIES_SLAKING']]
foe_labels['sParty_Katelyn1'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Katelyn2'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Katelyn3'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Katelyn4'] = [species['SPECIES_STARMIE']]
foe_labels['sParty_Katelyn5'] = [species['SPECIES_STARMIE']]
foe_labels['sParty_Katelynn'] = [species['SPECIES_GARDEVOIR'],species['SPECIES_SLAKING']]
foe_labels['sParty_Kathleen'] = [species['SPECIES_KADABRA']]
foe_labels['sParty_Katie'] = [species['SPECIES_GOLDEEN'],species['SPECIES_SPHEAL']]
foe_labels['sParty_Kayla'] = [species['SPECIES_WOBBUFFET'],species['SPECIES_NATU'],species['SPECIES_KADABRA']]
foe_labels['sParty_Kaylee'] = [species['SPECIES_LANTURN'],species['SPECIES_PELIPPER']]
foe_labels['sParty_Kayley'] = [species['SPECIES_CASTFORM']]
foe_labels['sParty_Keegan'] = [species['SPECIES_SLUGMA']]
foe_labels['sParty_Keigo'] = [species['SPECIES_KOFFING'],species['SPECIES_NINJASK']]
foe_labels['sParty_Keira'] = [species['SPECIES_LAIRON'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Kelvin'] = [species['SPECIES_MACHOKE'],species['SPECIES_SPHEAL']]
foe_labels['sParty_Kent'] = [species['SPECIES_NINJASK']]
foe_labels['sParty_Kevin'] = [species['SPECIES_SPHEAL']]
foe_labels['sParty_KimAndIris'] = [species['SPECIES_SWABLU'],species['SPECIES_NUMEL']]
foe_labels['sParty_Kindra'] = [species['SPECIES_DUSKULL'],species['SPECIES_SHUPPET']]
foe_labels['sParty_KiraAndDan1'] = [species['SPECIES_VOLBEAT'],species['SPECIES_ILLUMISE']]
foe_labels['sParty_KiraAndDan2'] = [species['SPECIES_VOLBEAT'],species['SPECIES_ILLUMISE']]
foe_labels['sParty_KiraAndDan3'] = [species['SPECIES_VOLBEAT'],species['SPECIES_ILLUMISE']]
foe_labels['sParty_KiraAndDan4'] = [species['SPECIES_VOLBEAT'],species['SPECIES_ILLUMISE']]
foe_labels['sParty_KiraAndDan5'] = [species['SPECIES_VOLBEAT'],species['SPECIES_ILLUMISE']]
foe_labels['sParty_Kirk'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_VOLTORB']]
foe_labels['sParty_Kiyo'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Koichi'] = [species['SPECIES_MACHOP'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Koji1'] = [species['SPECIES_MACHOKE']]
foe_labels['sParty_Koji2'] = [species['SPECIES_MACHOKE'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Koji3'] = [species['SPECIES_MAKUHITA'],species['SPECIES_MACHOKE'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Koji4'] = [species['SPECIES_HARIYAMA'],species['SPECIES_MACHOKE'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Koji5'] = [species['SPECIES_HARIYAMA'],species['SPECIES_MACHAMP'],species['SPECIES_MACHAMP']]
foe_labels['sParty_Kyla'] = [species['SPECIES_WAILMER']]
foe_labels['sParty_Kyra'] = [species['SPECIES_DODUO'],species['SPECIES_DODRIO']]
foe_labels['sParty_Lao1'] = [species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING']]
foe_labels['sParty_Lao2'] = [species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING']]
foe_labels['sParty_Lao3'] = [species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING']]
foe_labels['sParty_Lao4'] = [species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING'],species['SPECIES_KOFFING']]
foe_labels['sParty_Larry'] = [species['SPECIES_NUZLEAF']]
foe_labels['sParty_Laura'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Laurel'] = [species['SPECIES_LUVDISC'],species['SPECIES_LUVDISC']]
foe_labels['sParty_Lawrence'] = [species['SPECIES_BALTOY'],species['SPECIES_SANDSHREW']]
foe_labels['sParty_LeaAndJed'] = [species['SPECIES_LUVDISC'],species['SPECIES_LUVDISC']]
foe_labels['sParty_Leaf'] = [species['SPECIES_BULBASAUR']]
foe_labels['sParty_Leah'] = [species['SPECIES_SPOINK']]
foe_labels['sParty_Lenny'] = [species['SPECIES_GEODUDE'],species['SPECIES_MACHOP']]
foe_labels['sParty_Leonard'] = [species['SPECIES_MACHOP'],species['SPECIES_PELIPPER'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Leonardo'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_Leonel'] = [species['SPECIES_MANECTRIC']]
foe_labels['sParty_Leroy'] = [species['SPECIES_MAWILE'],species['SPECIES_STARMIE']]
foe_labels['sParty_LilaAndRoy1'] = [species['SPECIES_CHINCHOU'],species['SPECIES_CARVANHA']]
foe_labels['sParty_LilaAndRoy2'] = [species['SPECIES_CHINCHOU'],species['SPECIES_CARVANHA']]
foe_labels['sParty_LilaAndRoy3'] = [species['SPECIES_LANTURN'],species['SPECIES_CARVANHA']]
foe_labels['sParty_LilaAndRoy4'] = [species['SPECIES_LANTURN'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_LilaAndRoy5'] = [species['SPECIES_LANTURN'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_Lilith'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Linda'] = [species['SPECIES_HORSEA'],species['SPECIES_SEADRA']]
foe_labels['sParty_LisaAndRay'] = [species['SPECIES_GOLDEEN'],species['SPECIES_TENTACOOL']]
foe_labels['sParty_Lola1'] = [species['SPECIES_AZURILL'],species['SPECIES_AZURILL']]
foe_labels['sParty_Lola2'] = [species['SPECIES_MARILL'],species['SPECIES_MARILL']]
foe_labels['sParty_Lola3'] = [species['SPECIES_MARILL'],species['SPECIES_MARILL']]
foe_labels['sParty_Lola4'] = [species['SPECIES_MARILL'],species['SPECIES_MARILL']]
foe_labels['sParty_Lola5'] = [species['SPECIES_AZUMARILL'],species['SPECIES_AZUMARILL']]
foe_labels['sParty_Lorenzo'] = [species['SPECIES_SEEDOT'],species['SPECIES_NUZLEAF'],species['SPECIES_LOMBRE']]
foe_labels['sParty_Lucas1'] = [species['SPECIES_GEODUDE'],species['SPECIES_NUMEL']]
foe_labels['sParty_Lucas2'] = [species['SPECIES_WAILMER']]
foe_labels['sParty_Lucy'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_Luis'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_Lung'] = [species['SPECIES_KOFFING'],species['SPECIES_NINJASK']]
foe_labels['sParty_Lydia1'] = [species['SPECIES_WINGULL'],species['SPECIES_SHROOMISH'],species['SPECIES_MARILL'],species['SPECIES_ROSELIA'],species['SPECIES_SKITTY'],species['SPECIES_GOLDEEN']]
foe_labels['sParty_Lydia2'] = [species['SPECIES_WINGULL'],species['SPECIES_SHROOMISH'],species['SPECIES_MARILL'],species['SPECIES_ROSELIA'],species['SPECIES_SKITTY'],species['SPECIES_GOLDEEN']]
foe_labels['sParty_Lydia3'] = [species['SPECIES_PELIPPER'],species['SPECIES_BRELOOM'],species['SPECIES_MARILL'],species['SPECIES_ROSELIA'],species['SPECIES_DELCATTY'],species['SPECIES_GOLDEEN']]
foe_labels['sParty_Lydia4'] = [species['SPECIES_PELIPPER'],species['SPECIES_BRELOOM'],species['SPECIES_MARILL'],species['SPECIES_ROSELIA'],species['SPECIES_DELCATTY'],species['SPECIES_GOLDEEN']]
foe_labels['sParty_Lydia5'] = [species['SPECIES_PELIPPER'],species['SPECIES_BRELOOM'],species['SPECIES_AZUMARILL'],species['SPECIES_ROSELIA'],species['SPECIES_DELCATTY'],species['SPECIES_SEAKING']]
foe_labels['sParty_Lyle'] = [species['SPECIES_WURMPLE'],species['SPECIES_WURMPLE'],species['SPECIES_WURMPLE'],species['SPECIES_WURMPLE']]
foe_labels['sParty_Macey'] = [species['SPECIES_NATU']]
foe_labels['sParty_Madeline1'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Madeline2'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Madeline3'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Madeline4'] = [species['SPECIES_ROSELIA'],species['SPECIES_NUMEL']]
foe_labels['sParty_Madeline5'] = [species['SPECIES_ROSELIA'],species['SPECIES_CAMERUPT']]
foe_labels['sParty_Makayla'] = [species['SPECIES_ROSELIA'],species['SPECIES_MEDICHAM']]
foe_labels['sParty_Marc'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE']]
foe_labels['sParty_Marcel'] = [species['SPECIES_MANECTRIC'],species['SPECIES_SHIFTRY']]
foe_labels['sParty_Marcos'] = [species['SPECIES_VOLTORB']]
foe_labels['sParty_Maria1'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Maria2'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Maria3'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Maria4'] = [species['SPECIES_DODRIO']]
foe_labels['sParty_Maria5'] = [species['SPECIES_DODRIO']]
foe_labels['sParty_Mariela'] = [species['SPECIES_CHIMECHO']]
foe_labels['sParty_Mark'] = [species['SPECIES_RHYHORN']]
foe_labels['sParty_Marlene'] = [species['SPECIES_MEDITITE'],species['SPECIES_SPOINK']]
foe_labels['sParty_Martha'] = [species['SPECIES_SKITTY'],species['SPECIES_SWABLU']]
foe_labels['sParty_Matt'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_GOLBAT']]
foe_labels['sParty_Matthew'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_Maura'] = [species['SPECIES_KADABRA']]
foe_labels['sParty_MaxieMagmaHideout'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_CROBAT'],species['SPECIES_CAMERUPT']]
foe_labels['sParty_MaxieMossdeep'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_CROBAT'],species['SPECIES_CAMERUPT']]
foe_labels['sParty_MaxieMtChimney'] = [species['SPECIES_MIGHTYENA'],species['SPECIES_ZUBAT'],species['SPECIES_CAMERUPT']]
foe_labels['sParty_MayLilycoveMudkip'] = [species['SPECIES_TROPIUS'],species['SPECIES_SLUGMA'],species['SPECIES_PELIPPER'],species['SPECIES_GROVYLE']]
foe_labels['sParty_MayLilycoveTorchic'] = [species['SPECIES_TROPIUS'],species['SPECIES_LUDICOLO'],species['SPECIES_SLUGMA'],species['SPECIES_MARSHTOMP']]
foe_labels['sParty_MayLilycoveTreecko'] = [species['SPECIES_TROPIUS'],species['SPECIES_PELIPPER'],species['SPECIES_LUDICOLO'],species['SPECIES_COMBUSKEN']]
foe_labels['sParty_MayLinkPlaceholder'] = [species['SPECIES_KYOGRE']]
foe_labels['sParty_MayRoute103Mudkip'] = [species['SPECIES_TREECKO']]
foe_labels['sParty_MayRoute103Torchic'] = [species['SPECIES_MUDKIP']]
foe_labels['sParty_MayRoute103Treecko'] = [species['SPECIES_TORCHIC']]
foe_labels['sParty_MayRoute110Mudkip'] = [species['SPECIES_WINGULL'],species['SPECIES_SLUGMA'],species['SPECIES_GROVYLE']]
foe_labels['sParty_MayRoute110Torchic'] = [species['SPECIES_LOMBRE'],species['SPECIES_SLUGMA'],species['SPECIES_MARSHTOMP']]
foe_labels['sParty_MayRoute110Treecko'] = [species['SPECIES_WINGULL'],species['SPECIES_LOMBRE'],species['SPECIES_COMBUSKEN']]
foe_labels['sParty_MayRoute119Mudkip'] = [species['SPECIES_SLUGMA'],species['SPECIES_LOMBRE'],species['SPECIES_GROVYLE']]
foe_labels['sParty_MayRoute119Torchic'] = [species['SPECIES_LOMBRE'],species['SPECIES_SLUGMA'],species['SPECIES_MARSHTOMP']]
foe_labels['sParty_MayRoute119Treecko'] = [species['SPECIES_PELIPPER'],species['SPECIES_LOMBRE'],species['SPECIES_COMBUSKEN']]
foe_labels['sParty_MayRustboroMudkip'] = [species['SPECIES_WINGULL'],species['SPECIES_TREECKO']]
foe_labels['sParty_MayRustboroTorchic'] = [species['SPECIES_TORKOAL'],species['SPECIES_MUDKIP']]
foe_labels['sParty_MayRustboroTreecko'] = [species['SPECIES_LOTAD'],species['SPECIES_TORCHIC']]
foe_labels['sParty_MelAndPaul'] = [species['SPECIES_DUSTOX'],species['SPECIES_BEAUTIFLY']]
foe_labels['sParty_Melina'] = [species['SPECIES_DODUO']]
foe_labels['sParty_Melissa'] = [species['SPECIES_MARILL']]
foe_labels['sParty_Micah'] = [species['SPECIES_MANECTRIC'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Michelle'] = [species['SPECIES_TORKOAL'],species['SPECIES_MEDICHAM'],species['SPECIES_LUDICOLO']]
foe_labels['sParty_Mike1'] = [species['SPECIES_PELIPPER'],species['SPECIES_POOCHYENA']]
foe_labels['sParty_Mike2'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE'],species['SPECIES_MACHOP']]
foe_labels['sParty_Missy'] = [species['SPECIES_GOLDEEN']]
foe_labels['sParty_Mitchell'] = [species['SPECIES_LUNATONE'],species['SPECIES_SOLROCK']]
foe_labels['sParty_MiuAndYuki'] = [species['SPECIES_BEAUTIFLY'],species['SPECIES_DUSTOX']]
foe_labels['sParty_Mollie'] = [species['SPECIES_WHISCASH'],species['SPECIES_MEDITITE']]
foe_labels['sParty_Myles'] = [species['SPECIES_MAKUHITA'],species['SPECIES_WINGULL'],species['SPECIES_TROPIUS'],species['SPECIES_ZIGZAGOON'],species['SPECIES_ELECTRIKE'],species['SPECIES_NUMEL']]
foe_labels['sParty_Nancy'] = [species['SPECIES_MARILL'],species['SPECIES_LOMBRE']]
foe_labels['sParty_Nate'] = [species['SPECIES_SPOINK']]
foe_labels['sParty_Ned'] = [species['SPECIES_TENTACOOL']]
foe_labels['sParty_Nicholas'] = [species['SPECIES_WOBBUFFET']]
foe_labels['sParty_Nicolas1'] = [species['SPECIES_ALTARIA'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Nicolas2'] = [species['SPECIES_ALTARIA'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Nicolas3'] = [species['SPECIES_ALTARIA'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Nicolas4'] = [species['SPECIES_BAGON'],species['SPECIES_ALTARIA'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Nikki'] = [species['SPECIES_MARILL'],species['SPECIES_SPHEAL']]
foe_labels['sParty_Nob1'] = [species['SPECIES_MACHOP']]
foe_labels['sParty_Nob2'] = [species['SPECIES_MACHOKE']]
foe_labels['sParty_Nob3'] = [species['SPECIES_MACHOP'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Nob4'] = [species['SPECIES_MACHOP'],species['SPECIES_MACHOKE'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Nolan'] = [species['SPECIES_BARBOACH']]
foe_labels['sParty_Noland'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_Nolen'] = [species['SPECIES_TENTACRUEL']]
foe_labels['sParty_Olivia'] = [species['SPECIES_CLAMPERL'],species['SPECIES_CORPHISH'],species['SPECIES_LOMBRE']]
foe_labels['sParty_Owen'] = [species['SPECIES_KECLEON'],species['SPECIES_GRAVELER'],species['SPECIES_WAILORD']]
foe_labels['sParty_Pablo1'] = [species['SPECIES_STARYU'],species['SPECIES_STARYU']]
foe_labels['sParty_Pablo2'] = [species['SPECIES_STARYU'],species['SPECIES_STARYU']]
foe_labels['sParty_Pablo3'] = [species['SPECIES_WINGULL'],species['SPECIES_STARYU'],species['SPECIES_STARYU']]
foe_labels['sParty_Pablo4'] = [species['SPECIES_PELIPPER'],species['SPECIES_STARYU'],species['SPECIES_STARYU']]
foe_labels['sParty_Pablo5'] = [species['SPECIES_PELIPPER'],species['SPECIES_STARMIE'],species['SPECIES_STARMIE']]
foe_labels['sParty_Pat'] = [species['SPECIES_POOCHYENA'],species['SPECIES_SHROOMISH'],species['SPECIES_ELECTRIKE'],species['SPECIES_MARILL'],species['SPECIES_SANDSHREW'],species['SPECIES_GULPIN']]
foe_labels['sParty_Patricia'] = [species['SPECIES_BANETTE'],species['SPECIES_LUNATONE']]
foe_labels['sParty_Paul'] = [species['SPECIES_NUMEL'],species['SPECIES_ODDISH'],species['SPECIES_WINGULL']]
foe_labels['sParty_Paula'] = [species['SPECIES_BRELOOM']]
foe_labels['sParty_Paxton'] = [species['SPECIES_SWELLOW'],species['SPECIES_BRELOOM']]
foe_labels['sParty_Perry'] = [species['SPECIES_WINGULL']]
foe_labels['sParty_Pete'] = [species['SPECIES_TENTACOOL']]
foe_labels['sParty_Phil'] = [species['SPECIES_SWELLOW']]
foe_labels['sParty_Phillip'] = [species['SPECIES_TENTACRUEL'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Presley'] = [species['SPECIES_TROPIUS'],species['SPECIES_XATU']]
foe_labels['sParty_Preston'] = [species['SPECIES_KIRLIA']]
foe_labels['sParty_Quincy'] = [species['SPECIES_SLAKING'],species['SPECIES_DUSCLOPS']]
foe_labels['sParty_Rachel'] = [species['SPECIES_GOLDEEN']]
foe_labels['sParty_Red'] = [species['SPECIES_CHARMANDER']]
foe_labels['sParty_Reed'] = [species['SPECIES_SPHEAL'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_ReliAndIan'] = [species['SPECIES_AZUMARILL'],species['SPECIES_WINGULL']]
foe_labels['sParty_Reyna'] = [species['SPECIES_MEDITITE'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Rhett'] = [species['SPECIES_MAKUHITA']]
foe_labels['sParty_Richard'] = [species['SPECIES_PELIPPER']]
foe_labels['sParty_Rick'] = [species['SPECIES_WURMPLE'],species['SPECIES_WURMPLE']]
foe_labels['sParty_Ricky1'] = [species['SPECIES_ZIGZAGOON']]
foe_labels['sParty_Ricky2'] = [species['SPECIES_LINOONE']]
foe_labels['sParty_Ricky3'] = [species['SPECIES_LINOONE']]
foe_labels['sParty_Ricky4'] = [species['SPECIES_LINOONE']]
foe_labels['sParty_Ricky5'] = [species['SPECIES_LINOONE']]
foe_labels['sParty_Riley'] = [species['SPECIES_NINCADA'],species['SPECIES_KOFFING']]
foe_labels['sParty_Robert1'] = [species['SPECIES_SWABLU']]
foe_labels['sParty_Robert2'] = [species['SPECIES_NATU'],species['SPECIES_SWABLU']]
foe_labels['sParty_Robert3'] = [species['SPECIES_NATU'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Robert4'] = [species['SPECIES_NATU'],species['SPECIES_ALTARIA']]
foe_labels['sParty_Robert5'] = [species['SPECIES_ALTARIA'],species['SPECIES_XATU']]
foe_labels['sParty_Robin'] = [species['SPECIES_SKITTY'],species['SPECIES_SHROOMISH'],species['SPECIES_MARILL']]
foe_labels['sParty_Rodney'] = [species['SPECIES_GYARADOS']]
foe_labels['sParty_Roger'] = [species['SPECIES_MAGIKARP'],species['SPECIES_MAGIKARP'],species['SPECIES_GYARADOS']]
foe_labels['sParty_Roland'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_Ronald'] = [species['SPECIES_MAGIKARP'],species['SPECIES_GYARADOS'],species['SPECIES_GYARADOS'],species['SPECIES_GYARADOS'],species['SPECIES_GYARADOS'],species['SPECIES_GYARADOS']]
foe_labels['sParty_Rose1'] = [species['SPECIES_ROSELIA'],species['SPECIES_SHROOMISH'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Rose2'] = [species['SPECIES_SHROOMISH'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Rose3'] = [species['SPECIES_SHROOMISH'],species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Rose4'] = [species['SPECIES_SHROOMISH'],species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Rose5'] = [species['SPECIES_BRELOOM'],species['SPECIES_GLOOM'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Ruben'] = [species['SPECIES_SHIFTRY'],species['SPECIES_NOSEPASS']]
foe_labels['sParty_Sally'] = [species['SPECIES_ODDISH']]
foe_labels['sParty_Samantha'] = [species['SPECIES_XATU']]
foe_labels['sParty_Samuel'] = [species['SPECIES_SWELLOW'],species['SPECIES_MAWILE'],species['SPECIES_KADABRA']]
foe_labels['sParty_Santiago'] = [species['SPECIES_TENTACRUEL'],species['SPECIES_WAILMER']]
foe_labels['sParty_Sawyer1'] = [species['SPECIES_GEODUDE']]
foe_labels['sParty_Sawyer2'] = [species['SPECIES_GEODUDE'],species['SPECIES_NUMEL']]
foe_labels['sParty_Sawyer3'] = [species['SPECIES_MACHOP'],species['SPECIES_NUMEL'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Sawyer4'] = [species['SPECIES_MACHOP'],species['SPECIES_NUMEL'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Sawyer5'] = [species['SPECIES_MACHOKE'],species['SPECIES_CAMERUPT'],species['SPECIES_GOLEM']]
foe_labels['sParty_Sebastian'] = [species['SPECIES_CACTURNE']]
foe_labels['sParty_Shane'] = [species['SPECIES_SANDSHREW'],species['SPECIES_NUZLEAF']]
foe_labels['sParty_Shannon'] = [species['SPECIES_CLAYDOL']]
foe_labels['sParty_Sharon'] = [species['SPECIES_SEAKING']]
foe_labels['sParty_Shawn'] = [species['SPECIES_VOLTORB'],species['SPECIES_MAGNEMITE']]
foe_labels['sParty_Shayla'] = [species['SPECIES_SHROOMISH'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Sheila'] = [species['SPECIES_SHROOMISH']]
foe_labels['sParty_Shelby1'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Shelby2'] = [species['SPECIES_MEDITITE'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Shelby3'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Shelby4'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Shelby5'] = [species['SPECIES_MEDICHAM'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_ShellySeafloorCavern'] = [species['SPECIES_SHARPEDO'],species['SPECIES_MIGHTYENA']]
foe_labels['sParty_ShellyWeatherInstitute'] = [species['SPECIES_CARVANHA'],species['SPECIES_MIGHTYENA']]
foe_labels['sParty_Shirley'] = [species['SPECIES_NUMEL']]
foe_labels['sParty_Sienna'] = [species['SPECIES_LUVDISC'],species['SPECIES_LUVDISC']]
foe_labels['sParty_Simon'] = [species['SPECIES_AZURILL'],species['SPECIES_MARILL']]
foe_labels['sParty_Sophia'] = [species['SPECIES_SWABLU'],species['SPECIES_ROSELIA']]
foe_labels['sParty_Sophie'] = [species['SPECIES_MARILL'],species['SPECIES_LOMBRE']]
foe_labels['sParty_Spencer'] = [species['SPECIES_TENTACOOL'],species['SPECIES_WINGULL']]
foe_labels['sParty_Spenser'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_Stan'] = [species['SPECIES_HORSEA']]
foe_labels['sParty_Steve1'] = [species['SPECIES_ARON']]
foe_labels['sParty_Steve2'] = [species['SPECIES_LAIRON']]
foe_labels['sParty_Steve3'] = [species['SPECIES_LAIRON'],species['SPECIES_RHYHORN']]
foe_labels['sParty_Steve4'] = [species['SPECIES_LAIRON'],species['SPECIES_RHYHORN']]
foe_labels['sParty_Steve5'] = [species['SPECIES_AGGRON'],species['SPECIES_RHYDON']]
foe_labels['sParty_Susie'] = [species['SPECIES_LUVDISC']]
foe_labels['sParty_Sylvia'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_TabithaMagmaHideout'] = [species['SPECIES_NUMEL'],species['SPECIES_MIGHTYENA'],species['SPECIES_ZUBAT'],species['SPECIES_CAMERUPT']]
foe_labels['sParty_TabithaMossdeep'] = [species['SPECIES_CAMERUPT'],species['SPECIES_MIGHTYENA'],species['SPECIES_GOLBAT']]
foe_labels['sParty_TabithaMtChimney'] = [species['SPECIES_NUMEL'],species['SPECIES_POOCHYENA'],species['SPECIES_NUMEL'],species['SPECIES_ZUBAT']]
foe_labels['sParty_Takao'] = [species['SPECIES_MACHOP']]
foe_labels['sParty_Takashi'] = [species['SPECIES_NINJASK'],species['SPECIES_KOFFING']]
foe_labels['sParty_Talia'] = [species['SPECIES_STARYU']]
foe_labels['sParty_Tammy'] = [species['SPECIES_DUSKULL'],species['SPECIES_SHUPPET']]
foe_labels['sParty_Tanya'] = [species['SPECIES_LUVDISC']]
foe_labels['sParty_Tara'] = [species['SPECIES_HORSEA'],species['SPECIES_MARILL']]
foe_labels['sParty_Tasha'] = [species['SPECIES_SHUPPET']]
foe_labels['sParty_Taylor'] = [species['SPECIES_WURMPLE'],species['SPECIES_CASCOON'],species['SPECIES_DUSTOX']]
foe_labels['sParty_Ted'] = [species['SPECIES_RALTS']]
foe_labels['sParty_Terry'] = [species['SPECIES_GIRAFARIG']]
foe_labels['sParty_Thalia1'] = [species['SPECIES_WAILMER'],species['SPECIES_HORSEA']]
foe_labels['sParty_Thalia2'] = [species['SPECIES_WAILMER'],species['SPECIES_HORSEA']]
foe_labels['sParty_Thalia3'] = [species['SPECIES_LUVDISC'],species['SPECIES_WAILMER'],species['SPECIES_SEADRA']]
foe_labels['sParty_Thalia4'] = [species['SPECIES_LUVDISC'],species['SPECIES_WAILMER'],species['SPECIES_SEADRA']]
foe_labels['sParty_Thalia5'] = [species['SPECIES_LUVDISC'],species['SPECIES_WAILORD'],species['SPECIES_KINGDRA']]
foe_labels['sParty_Thomas'] = [species['SPECIES_ZANGOOSE']]
foe_labels['sParty_Tiana'] = [species['SPECIES_ZIGZAGOON'],species['SPECIES_SHROOMISH']]
foe_labels['sParty_Tiffany'] = [species['SPECIES_CARVANHA'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_Timmy'] = [species['SPECIES_ARON'],species['SPECIES_ELECTRIKE']]
foe_labels['sParty_Timothy1'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Timothy2'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Timothy3'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Timothy4'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Timothy5'] = [species['SPECIES_HARIYAMA']]
foe_labels['sParty_Tisha'] = [species['SPECIES_CHINCHOU']]
foe_labels['sParty_Tommy'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE']]
foe_labels['sParty_Tony1'] = [species['SPECIES_CARVANHA']]
foe_labels['sParty_Tony2'] = [species['SPECIES_SHARPEDO']]
foe_labels['sParty_Tony3'] = [species['SPECIES_SHARPEDO']]
foe_labels['sParty_Tony4'] = [species['SPECIES_STARYU'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_Tony5'] = [species['SPECIES_STARMIE'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_ToriAndTia'] = [species['SPECIES_SPINDA'],species['SPECIES_SPINDA']]
foe_labels['sParty_Travis'] = [species['SPECIES_SANDSHREW']]
foe_labels['sParty_Trent1'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE']]
foe_labels['sParty_Trent2'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Trent3'] = [species['SPECIES_GEODUDE'],species['SPECIES_GEODUDE'],species['SPECIES_GRAVELER'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Trent4'] = [species['SPECIES_GEODUDE'],species['SPECIES_GRAVELER'],species['SPECIES_GRAVELER'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Trent5'] = [species['SPECIES_GRAVELER'],species['SPECIES_GRAVELER'],species['SPECIES_GRAVELER'],species['SPECIES_GOLEM']]
foe_labels['sParty_Tucker'] = [species['SPECIES_BELDUM']]
foe_labels['sParty_TyraAndIvy'] = [species['SPECIES_ROSELIA'],species['SPECIES_GRAVELER']]
foe_labels['sParty_Tyron'] = [species['SPECIES_SANDSHREW']]
foe_labels['sParty_Valerie1'] = [species['SPECIES_SABLEYE']]
foe_labels['sParty_Valerie2'] = [species['SPECIES_SABLEYE'],species['SPECIES_SPOINK']]
foe_labels['sParty_Valerie3'] = [species['SPECIES_SPOINK'],species['SPECIES_SABLEYE']]
foe_labels['sParty_Valerie4'] = [species['SPECIES_SPOINK'],species['SPECIES_SABLEYE']]
foe_labels['sParty_Valerie5'] = [species['SPECIES_DUSKULL'],species['SPECIES_SABLEYE'],species['SPECIES_GRUMPIG']]
foe_labels['sParty_Vicky'] = [species['SPECIES_MEDITITE']]
foe_labels['sParty_Vincent'] = [species['SPECIES_SABLEYE'],species['SPECIES_MEDICHAM'],species['SPECIES_SHARPEDO']]
foe_labels['sParty_Violet'] = [species['SPECIES_ROSELIA'],species['SPECIES_GLOOM']]
foe_labels['sParty_Virgil'] = [species['SPECIES_RALTS']]
foe_labels['sParty_Vito'] = [species['SPECIES_DODRIO'],species['SPECIES_KADABRA'],species['SPECIES_ELECTRODE'],species['SPECIES_SHIFTRY']]
foe_labels['sParty_Vivi'] = [species['SPECIES_MARILL'],species['SPECIES_SHROOMISH'],species['SPECIES_NUMEL']]
foe_labels['sParty_Vivian'] = [species['SPECIES_MEDITITE'],species['SPECIES_MEDITITE']]
foe_labels['sParty_Wade'] = [species['SPECIES_TENTACOOL']]
foe_labels['sParty_WallyMauville'] = [species['SPECIES_RALTS']]
foe_labels['sParty_WallyVR1'] = [species['SPECIES_ALTARIA'],species['SPECIES_DELCATTY'],species['SPECIES_ROSELIA'],species['SPECIES_MAGNETON'],species['SPECIES_GARDEVOIR']]
foe_labels['sParty_WallyVR2'] = [species['SPECIES_ALTARIA'],species['SPECIES_DELCATTY'],species['SPECIES_ROSELIA'],species['SPECIES_MAGNETON'],species['SPECIES_GARDEVOIR']]
foe_labels['sParty_WallyVR3'] = [species['SPECIES_ALTARIA'],species['SPECIES_DELCATTY'],species['SPECIES_ROSELIA'],species['SPECIES_MAGNETON'],species['SPECIES_GARDEVOIR']]
foe_labels['sParty_WallyVR4'] = [species['SPECIES_ALTARIA'],species['SPECIES_DELCATTY'],species['SPECIES_ROSELIA'],species['SPECIES_MAGNETON'],species['SPECIES_GARDEVOIR']]
foe_labels['sParty_WallyVR5'] = [species['SPECIES_ALTARIA'],species['SPECIES_DELCATTY'],species['SPECIES_ROSELIA'],species['SPECIES_MAGNETON'],species['SPECIES_GARDEVOIR']]
foe_labels['sParty_Walter1'] = [species['SPECIES_MANECTRIC']]
foe_labels['sParty_Walter2'] = [species['SPECIES_MANECTRIC']]
foe_labels['sParty_Walter3'] = [species['SPECIES_LINOONE'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Walter4'] = [species['SPECIES_LINOONE'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Walter5'] = [species['SPECIES_LINOONE'],species['SPECIES_GOLDUCK'],species['SPECIES_MANECTRIC']]
foe_labels['sParty_Warren'] = [species['SPECIES_GRAVELER'],species['SPECIES_LUDICOLO']]
foe_labels['sParty_Wayne'] = [species['SPECIES_TENTACOOL'],species['SPECIES_TENTACOOL'],species['SPECIES_WAILMER']]
foe_labels['sParty_Wendy'] = [species['SPECIES_MAWILE'],species['SPECIES_ROSELIA'],species['SPECIES_PELIPPER']]
foe_labels['sParty_William'] = [species['SPECIES_RALTS'],species['SPECIES_RALTS'],species['SPECIES_KIRLIA']]
foe_labels['sParty_Wilton1'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_WAILMER'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Wilton2'] = [species['SPECIES_ELECTRIKE'],species['SPECIES_WAILMER'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Wilton3'] = [species['SPECIES_MANECTRIC'],species['SPECIES_WAILMER'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Wilton4'] = [species['SPECIES_MANECTRIC'],species['SPECIES_WAILMER'],species['SPECIES_MAKUHITA']]
foe_labels['sParty_Wilton5'] = [species['SPECIES_MANECTRIC'],species['SPECIES_WAILMER'],species['SPECIES_HARIYAMA']]
foe_labels['sParty_Wyatt'] = [species['SPECIES_ARON'],species['SPECIES_ARON']]
foe_labels['sParty_Yasu'] = [species['SPECIES_NINJASK']]
foe_labels['sParty_Yuji'] = [species['SPECIES_MAKUHITA'],species['SPECIES_MACHOKE']]
foe_labels['sParty_Zander'] = [species['SPECIES_HARIYAMA']]

item_labels = {}

item_labels['gNewGamePCItems'] = ('pc',items['ITEM_POTION'])

item_labels['RustboroCity_DevonCorp_3F_EventScript_GiveExpShare'] = ('giveitem',items['ITEM_MASTER_BALL'],False,None)
item_labels['PlayersHouse_1F_EventScript_TryGiveAmuletCoin'] = ('giveitem',items['ITEM_AMULET_COIN'],False,None)
item_labels['OldaleTown_EventScript_ExplainPokemonMart'] = ('giveitem',items['ITEM_POTION'],False,None)
item_labels['Route104_EventScript_Boy2'] = ('giveitem',items['ITEM_TM09'],True,None)
item_labels['Route104_EventScript_WhiteHerbFlorist'] = ('giveitem',items['ITEM_WHITE_HERB'],False,None)
item_labels['Route104_EventScript_ExpertF'] = ('giveitem',items['ITEM_CHESTO_BERRY'],False,None)
item_labels['PetalburgWoods_EventScript_DevonResearcherPostBattle'] = ('giveitem',items['ITEM_GREAT_BALL'],False,None)
item_labels['PetalburgWoods_EventScript_Girl'] = ('giveitem',items['ITEM_MIRACLE_SEED'],False,None)
item_labels['RustboroCity_Flat2_2F_EventScript_NinjaBoy'] = ('giveitem',items['ITEM_PREMIER_BALL'],False,None)
item_labels['RustboroCity_EventScript_ReturnGoods'] = ('giveitem',items['ITEM_GREAT_BALL'],False,None)
item_labels['Route114_FossilManiacsHouse_EventScript_FossilManiacsBrother'] = ('giveitem',items['ITEM_TM28'],True,None)
item_labels['Route114_EventScript_RoarGentleman'] = ('giveitem',items['ITEM_TM05'],True,None)
item_labels['FallarborTown_CozmosHouse_EventScript_PlayerHasMeteorite'] = ('giveitem',items['ITEM_TM27'],True,None)
item_labels['Route111_WinstrateFamilysHouse_EventScript_Victoria'] = ('giveitem',items['ITEM_MACHO_BRACE'],False,None)
item_labels['LavaridgeTown_HerbShop_EventScript_OldMan'] = ('giveitem',items['ITEM_CHARCOAL'],False,None)
item_labels['VerdanturfTown_BattleTentLobby_EventScript_AttractGiver'] = ('giveitem',items['ITEM_TM45'],True,None)
item_labels['Route116_EventScript_GiveRepeatBall'] = ('giveitem',items['ITEM_REPEAT_BALL'],False,None)
item_labels['GraniteCave_StevensRoom_EventScript_Steven'] = ('giveitem',items['ITEM_TM47'],True,None)
item_labels['DewfordTown_Hall_EventScript_SludgeBombMan'] = ('giveitem',items['ITEM_TM36'],True,None)
item_labels['DewfordTown_House2_EventScript_Man'] = ('giveitem',items['ITEM_SILK_SCARF'],False,None)
item_labels['Route109_EventScript_SoftSandGirl'] = ('giveitem',items['ITEM_SOFT_SAND'],False,None)
item_labels['Route109_SeashoreHouse_EventScript_DefeatedTrainers'] = ('giveitem',items['ITEM_SODA_POP'],False,None)
item_labels['SlateportCity_BattleTentLobby_EventScript_TormentGiver'] = ('giveitem',items['ITEM_TM41'],True,None)
item_labels['SlateportCity_OceanicMuseum_1F_EventScript_FamiliarGrunt'] = ('giveitem',items['ITEM_TM46'],True,None)
item_labels['PacifidlogTown_House2_EventScript_GiveReturn'] = ('giveitem',items['ITEM_TM27'],True,None)
item_labels['PacifidlogTown_House2_EventScript_GiveFrustration'] = ('giveitem',items['ITEM_TM21'],True,None)
item_labels['MossdeepCity_EventScript_KingsRockBoy'] = ('giveitem',items['ITEM_KINGS_ROCK'],False,None)
item_labels['ShoalCave_LowTideLowerRoom_EventScript_BlackBelt'] = ('giveitem',items['ITEM_FOCUS_BAND'],False,None)
item_labels['SootopolisCity_House1_EventScript_BrickBreakBlackBelt'] = ('giveitem',items['ITEM_TM31'],True,None)
item_labels['LilycoveCity_House2_EventScript_FatMan'] = ('giveitem',items['ITEM_TM44'],True,None)
item_labels['Route123_EventScript_GigaDrainGirl'] = ('giveitem',items['ITEM_TM19'],True,None)
item_labels['FortreeCity_House2_EventScript_HiddenPowerGiver'] = ('giveitem',items['ITEM_TM10'],True,None)
item_labels['FortreeCity_House4_EventScript_WingullReturned'] = ('giveitem',items['ITEM_MENTAL_HERB'],False,None)
item_labels['MtPyre_1F_EventScript_CleanseTagWoman'] = ('giveitem',items['ITEM_CLEANSE_TAG'],False,None)

item_id = encounter_id

# Gym Badge TMs:
## Rock Tomb TM39 0x0802
item_labels['RustboroCity_Gym_EventScript_GiveRockTomb'] = ('giveitem',items['ITEM_TM39'],True,item_id)
item_id+=1
## Bulk Up TM08 0xe901
item_labels['DewfordTown_Gym_EventScript_GiveBulkUp'] = ('giveitem',items['ITEM_TM08'],True,item_id)
item_labels['DewfordTown_Gym_EventScript_GiveBulkUp2'] = ('giveitem',items['ITEM_TM08'],True,item_id)
item_id+=1
## Shockwave TM34 0x0302
item_labels['MauvilleCity_Gym_EventScript_GiveShockWave'] = ('giveitem',items['ITEM_TM34'],True,item_id)
item_labels['MauvilleCity_Gym_EventScript_GiveShockWave2'] = ('giveitem',items['ITEM_TM34'],True,item_id)
item_id+=1
## Overheat TM50 0x1302
item_labels['LavaridgeTown_Gym_1F_EventScript_GiveOverheat'] = ('giveitem',items['ITEM_TM50'],True,item_id)
item_labels['LavaridgeTown_Gym_1F_EventScript_GiveOverheat2'] = ('giveitem',items['ITEM_TM50'],True,item_id)
item_id+=1
## Facade TM42 0x0b02
item_labels['PetalburgCity_Gym_EventScript_GiveFacade'] = ('giveitem',items['ITEM_TM42'],True,item_id)
item_id+=1
## Aerial Ace TM40 0x0902
item_labels['FortreeCity_Gym_EventScript_GiveAerialAce'] = ('giveitem',items['ITEM_TM40'],True,item_id)
item_labels['FortreeCity_Gym_EventScript_GiveAerialAce2'] = ('giveitem',items['ITEM_TM40'],True,item_id)
item_id+=1
## Calm Mind TM04 0xeitem_id
item_labels['MossdeepCity_Gym_EventScript_GiveCalmMind'] = ('giveitem',items['ITEM_TM04'],True,item_id)
item_labels['MossdeepCity_Gym_EventScript_GiveCalmMind2'] = ('giveitem',items['ITEM_TM04'],True,item_id)
item_id+=1
## Water Pulse TM03 0xe401
item_labels['SootopolisCity_Gym_1F_EventScript_GiveWaterPulse'] = ('giveitem',items['ITEM_TM03'],True,item_id)
item_labels['SootopolisCity_Gym_1F_EventScript_GiveWaterPulse2'] = ('giveitem',items['ITEM_TM03'],True,item_id)
item_id+=1

# Scattered Items:

item_labels['Route102_EventScript_ItemPotion'] = ('finditem',items['ITEM_POTION'],False,None)
item_labels['Route103_EventScript_ItemGuardSpec'] = ('finditem',items['ITEM_GUARD_SPEC'],False,None)
item_labels['Route103_EventScript_ItemPPUp'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['Route104_EventScript_ItemPPUp'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['Route104_EventScript_ItemPokeBall'] = ('finditem',items['ITEM_POKE_BALL'],False,None)
item_labels['Route104_EventScript_ItemXAccuracy'] = ('finditem',items['ITEM_X_ACCURACY'],False,None)
item_labels['Route104_EventScript_ItemPotion'] = ('finditem',items['ITEM_POTION'],False,None)
item_labels['Route105_EventScript_ItemIron'] = ('finditem',items['ITEM_IRON'],False,None)
item_labels['Route106_EventScript_ItemProtein'] = ('finditem',items['ITEM_PROTEIN'],False,None)
item_labels['Route108_EventScript_ItemStarPiece'] = ('finditem',items['ITEM_STAR_PIECE'],False,None)
item_labels['Route109_EventScript_ItemPPUp'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['Route109_EventScript_ItemPotion'] = ('finditem',items['ITEM_POTION'],False,None)
item_labels['Route110_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['Route110_EventScript_ItemDireHit'] = ('finditem',items['ITEM_DIRE_HIT'],False,None)
item_labels['Route110_EventScript_ItemElixir'] = ('finditem',items['ITEM_ELIXIR'],False,None)
item_labels['Route111_EventScript_ItemTM37'] = ('finditem',items['ITEM_TM37'],True,None)
item_labels['Route111_EventScript_ItemStardust'] = ('finditem',items['ITEM_STARDUST'],False,None)
item_labels['Route111_EventScript_ItemHPUp'] = ('finditem',items['ITEM_HP_UP'],False,None)
item_labels['Route111_EventScript_ItemElixir'] = ('finditem',items['ITEM_ELIXIR'],False,None)
item_labels['Route112_EventScript_ItemNugget'] = ('finditem',items['ITEM_NUGGET'],False,None)
item_labels['Route113_EventScript_ItemMaxEther'] = ('finditem',items['ITEM_MAX_ETHER'],False,None)
item_labels['Route113_EventScript_ItemSuperRepel'] = ('finditem',items['ITEM_SUPER_REPEL'],False,None)
item_labels['Route113_EventScript_ItemHyperPotion'] = ('finditem',items['ITEM_SUPER_POTION'],False,None)
item_labels['Route114_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['Route114_EventScript_ItemProtein'] = ('finditem',items['ITEM_PROTEIN'],False,None)
item_labels['Route114_EventScript_ItemEnergyPowder'] = ('finditem',items['ITEM_ENERGY_POWDER'],False,None)
item_labels['Route115_EventScript_ItemSuperPotion'] = ('finditem',items['ITEM_SUPER_POTION'],False,None)
item_labels['Route115_EventScript_ItemTM01'] = ('finditem',items['ITEM_TM01'],True,None)
item_labels['Route115_EventScript_ItemIron'] = ('finditem',items['ITEM_IRON'],False,None)
item_labels['Route115_EventScript_ItemGreatBall'] = ('finditem',items['ITEM_GREAT_BALL'],False,None)
item_labels['Route115_EventScript_ItemHealPowder'] = ('finditem',items['ITEM_HEAL_POWDER'],False,None)
item_labels['Route115_EventScript_ItemPPUp'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['Route116_EventScript_ItemXSpecial'] = ('finditem',items['ITEM_X_SP_ATK'],False,None)
item_labels['Route116_EventScript_ItemEther'] = ('finditem',items['ITEM_ETHER'],False,None)
item_labels['Route116_EventScript_ItemRepel'] = ('finditem',items['ITEM_REPEL'],False,None)
item_labels['Route116_EventScript_ItemHPUp'] = ('finditem',items['ITEM_HP_UP'],False,None)
item_labels['Route116_EventScript_ItemPotion'] = ('finditem',items['ITEM_POTION'],False,None)
item_labels['Route117_EventScript_ItemGreatBall'] = ('finditem',items['ITEM_GREAT_BALL'],False,None)
item_labels['Route117_EventScript_ItemRevive'] = ('finditem',items['ITEM_REVIVE'],False,None)
item_labels['Route118_EventScript_ItemHyperPotion'] = ('finditem',items['ITEM_HYPER_POTION'],False,None)
item_labels['Route119_EventScript_ItemSuperRepel'] = ('finditem',items['ITEM_SUPER_REPEL'],False,None)
item_labels['Route119_EventScript_ItemZinc'] = ('finditem',items['ITEM_ZINC'],False,None)
item_labels['Route119_EventScript_ItemElixir'] = ('finditem',items['ITEM_ELIXIR'],False,None)
item_labels['Route119_EventScript_ItemLeafStone'] = ('finditem',items['ITEM_LEAF_STONE'],False,None)
item_labels['Route119_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['Route119_EventScript_ItemHyperPotion'] = ('finditem',items['ITEM_HYPER_POTION'],False,None)
item_labels['Route119_EventScript_ItemHyperPotion2'] = ('finditem',items['ITEM_HYPER_POTION'],False,None)
item_labels['Route119_EventScript_ItemElixir2'] = ('finditem',items['ITEM_ELIXIR'],False,None)
item_labels['Route120_EventScript_ItemNugget'] = ('finditem',items['ITEM_NUGGET'],False,None)
item_labels['Route120_EventScript_ItemFullHeal'] = ('finditem',items['ITEM_FULL_HEAL'],False,None)
item_labels['Route120_EventScript_ItemHyperPotion'] = ('finditem',items['ITEM_HYPER_POTION'],False,None)
item_labels['Route120_EventScript_ItemNestBall'] = ('finditem',items['ITEM_NEST_BALL'],False,None)
item_labels['Route120_EventScript_ItemRevive'] = ('finditem',items['ITEM_REVIVE'],False,None)
item_labels['Route121_EventScript_ItemCarbos'] = ('finditem',items['ITEM_CARBOS'],False,None)
item_labels['Route121_EventScript_ItemRevive'] = ('finditem',items['ITEM_REVIVE'],False,None)
item_labels['Route121_EventScript_ItemZinc'] = ('finditem',items['ITEM_ZINC'],False,None)
item_labels['Route123_EventScript_ItemCalcium'] = ('finditem',items['ITEM_CALCIUM'],False,None)
item_labels['Route123_EventScript_ItemUltraBall'] = ('finditem',items['ITEM_ULTRA_BALL'],False,None)
item_labels['Route123_EventScript_ItemElixir'] = ('finditem',items['ITEM_ELIXIR'],False,None)
item_labels['Route123_EventScript_ItemPPUp'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['Route123_EventScript_ItemRevivalHerb'] = ('finditem',items['ITEM_REVIVAL_HERB'],False,None)
item_labels['Route124_EventScript_ItemRedShard'] = ('finditem',items['ITEM_RED_SHARD'],False,None)
item_labels['Route124_EventScript_ItemBlueShard'] = ('finditem',items['ITEM_BLUE_SHARD'],False,None)
item_labels['Route124_EventScript_ItemYellowShard'] = ('finditem',items['ITEM_YELLOW_SHARD'],False,None)
item_labels['Route125_EventScript_ItemBigPearl'] = ('finditem',items['ITEM_BIG_PEARL'],False,None)
item_labels['Route126_EventScript_ItemGreenShard'] = ('finditem',items['ITEM_GREEN_SHARD'],False,None)
item_labels['Route127_EventScript_ItemZinc'] = ('finditem',items['ITEM_ZINC'],False,None)
item_labels['Route127_EventScript_ItemCarbos'] = ('finditem',items['ITEM_CARBOS'],False,None)
item_labels['Route127_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['Route132_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['Route132_EventScript_ItemProtein'] = ('finditem',items['ITEM_PROTEIN'],False,None)
item_labels['Route133_EventScript_ItemBigPearl'] = ('finditem',items['ITEM_BIG_PEARL'],False,None)
item_labels['Route133_EventScript_ItemStarPiece'] = ('finditem',items['ITEM_STAR_PIECE'],False,None)
item_labels['Route133_EventScript_ItemMaxRevive'] = ('finditem',items['ITEM_MAX_REVIVE'],False,None)
item_labels['Route134_EventScript_ItemCarbos'] = ('finditem',items['ITEM_CARBOS'],False,None)
item_labels['Route134_EventScript_ItemStarPiece'] = ('finditem',items['ITEM_STAR_PIECE'],False,None)
item_labels['PetalburgCity_EventScript_ItemMaxRevive'] = ('finditem',items['ITEM_MAX_REVIVE'],False,None)
item_labels['PetalburgCity_EventScript_ItemEther'] = ('finditem',items['ITEM_ETHER'],False,None)
item_labels['MauvilleCity_EventScript_ItemXSpeed'] = ('finditem',items['ITEM_X_SPEED'],False,None)
item_labels['RustboroCity_EventScript_ItemXDefend'] = ('finditem',items['ITEM_X_DEFENSE'],False,None)
item_labels['LilycoveCity_EventScript_ItemMaxRepel'] = ('finditem',items['ITEM_MAX_REPEL'],False,None)
item_labels['MossdeepCity_EventScript_ItemNetBall'] = ('finditem',items['ITEM_NET_BALL'],False,None)
item_labels['PetalburgWoods_EventScript_ItemXAttack'] = ('finditem',items['ITEM_X_ATTACK'],False,None)
item_labels['PetalburgWoods_EventScript_ItemGreatBall'] = ('finditem',items['ITEM_GREAT_BALL'],False,None)
item_labels['PetalburgWoods_EventScript_ItemEther'] = ('finditem',items['ITEM_ETHER'],False,None)
item_labels['PetalburgWoods_EventScript_ItemParalyzeHeal'] = ('finditem',items['ITEM_PARALYZE_HEAL'],False,None)
item_labels['RusturfTunnel_EventScript_ItemPokeBall'] = ('finditem',items['ITEM_POKE_BALL'],False,None)
item_labels['RusturfTunnel_EventScript_ItemMaxEther'] = ('finditem',items['ITEM_MAX_ETHER'],False,None)
item_labels['GraniteCave_1F_EventScript_ItemEscapeRope'] = ('finditem',items['ITEM_ESCAPE_ROPE'],False,None)
item_labels['GraniteCave_B1F_EventScript_ItemPokeBall'] = ('finditem',items['ITEM_POKE_BALL'],False,None)
item_labels['GraniteCave_B2F_EventScript_ItemRepel'] = ('finditem',items['ITEM_REPEL'],False,None)
item_labels['GraniteCave_B2F_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['JaggedPass_EventScript_ItemBurnHeal'] = ('finditem',items['ITEM_BURN_HEAL'],False,None)
item_labels['FieryPath_EventScript_ItemFireStone'] = ('finditem',items['ITEM_FIRE_STONE'],False,None)
item_labels['FieryPath_EventScript_ItemTM06'] = ('finditem',items['ITEM_TM06'],True,None)
item_labels['MeteorFalls_1F_1R_EventScript_ItemTM23'] = ('finditem',items['ITEM_TM23'],True,None)
item_labels['MeteorFalls_1F_1R_EventScript_ItemFullHeal'] = ('finditem',items['ITEM_FULL_HEAL'],False,None)
item_labels['MeteorFalls_1F_1R_EventScript_ItemMoonStone'] = ('finditem',items['ITEM_MOON_STONE'],False,None)
item_labels['MeteorFalls_1F_1R_EventScript_ItemPPUP'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['MeteorFalls_B1F_2R_EventScript_ItemTM02'] = ('finditem',items['ITEM_TM02'],True,None)
item_labels['NewMauville_Inside_EventScript_ItemUltraBall'] = ('finditem',items['ITEM_ULTRA_BALL'],False,None)
item_labels['NewMauville_Inside_EventScript_ItemEscapeRope'] = ('finditem',items['ITEM_ESCAPE_ROPE'],False,None)
item_labels['NewMauville_Inside_EventScript_ItemThunderStone'] = ('finditem',items['ITEM_THUNDER_STONE'],False,None)
item_labels['NewMauville_Inside_EventScript_ItemFullHeal'] = ('finditem',items['ITEM_FULL_HEAL'],False,None)
item_labels['NewMauville_Inside_EventScript_ItemParalyzeHeal'] = ('finditem',items['ITEM_PARALYZE_HEAL'],False,None)
item_labels['AbandonedShip_Rooms_1F_EventScript_ItemHarborMail'] = ('finditem',items['ITEM_HARBOR_MAIL'],False,None)
item_labels['AbandonedShip_Rooms_B1F_EventScript_ItemEscapeRope'] = ('finditem',items['ITEM_ESCAPE_ROPE'],False,None)
item_labels['AbandonedShip_Rooms2_B1F_EventScript_ItemDiveBall'] = ('finditem',items['ITEM_DIVE_BALL'],False,None)
item_labels['AbandonedShip_Room_B1F_EventScript_ItemTM13'] = ('finditem',items['ITEM_TM13'],True,None)
item_labels['AbandonedShip_Rooms2_1F_EventScript_ItemRevive'] = ('finditem',items['ITEM_REVIVE'],False,None)
item_labels['AbandonedShip_HiddenFloorRooms_EventScript_ItemLuxuryBall'] = ('finditem',items['ITEM_LUXURY_BALL'],False,None)
item_labels['AbandonedShip_HiddenFloorRooms_EventScript_ItemWaterStone'] = ('finditem',items['ITEM_WATER_STONE'],False,None)
item_labels['AbandonedShip_HiddenFloorRooms_EventScript_ItemTM18'] = ('finditem',items['ITEM_TM18'],True,None)
item_labels['ScorchedSlab_EventScript_ItemTM11'] = ('finditem',items['ITEM_TM11'],True,None)
item_labels['SafariZone_Northwest_EventScript_ItemTM22'] = ('finditem',items['ITEM_TM22'],True,None)
item_labels['SafariZone_North_EventScript_ItemCalcium'] = ('finditem',items['ITEM_CALCIUM'],False,None)
item_labels['SafariZone_Southwest_EventScript_ItemMaxRevive'] = ('finditem',items['ITEM_MAX_REVIVE'],False,None)
item_labels['SafariZone_Northeast_EventScript_ItemNugget'] = ('finditem',items['ITEM_NUGGET'],False,None)
item_labels['SafariZone_Southeast_EventScript_ItemBigPearl'] = ('finditem',items['ITEM_BIG_PEARL'],False,None)
item_labels['MtPyre_2F_EventScript_ItemUltraBall'] = ('finditem',items['ITEM_ULTRA_BALL'],False,None)
item_labels['MtPyre_3F_EventScript_ItemSuperRepel'] = ('finditem',items['ITEM_SUPER_REPEL'],False,None)
item_labels['MtPyre_4F_EventScript_ItemSeaIncense'] = ('finditem',items['ITEM_SEA_INCENSE'],False,None)
item_labels['MtPyre_5F_EventScript_ItemLaxIncense'] = ('finditem',items['ITEM_LAX_INCENSE'],False,None)
item_labels['MtPyre_6F_EventScript_ItemTM30'] = ('finditem',items['ITEM_TM30'],True,None)
item_labels['MtPyre_Exterior_EventScript_ItemMaxPotion'] = ('finditem',items['ITEM_MAX_POTION'],False,None)
item_labels['MtPyre_Exterior_EventScript_ItemTM48'] = ('finditem',items['ITEM_TM48'],True,None)
item_labels['AquaHideout_B1F_EventScript_ItemMasterBall'] = ('finditem',items['ITEM_MASTER_BALL'],False,None)
item_labels['AquaHideout_B1F_EventScript_ItemNugget'] = ('finditem',items['ITEM_NUGGET'],False,None)
item_labels['AquaHideout_B1F_EventScript_ItemMaxElixir'] = ('finditem',items['ITEM_MAX_ELIXIR'],False,None)
item_labels['AquaHideout_B2F_EventScript_ItemNestBall'] = ('finditem',items['ITEM_NEST_BALL'],False,None)
item_labels['AquaHideout_B2F_EventScript_ItemMasterBall'] = ('finditem',items['ITEM_MASTER_BALL'],False,None)
item_labels['Route119_EventScript_ItemNugget'] = ('finditem',items['ITEM_NUGGET'],False,None)
item_labels['Route119_EventScript_ItemMaxElixir'] = ('finditem',items['ITEM_MAX_ELIXIR'],False,None)
item_labels['Route119_EventScript_ItemNestBall'] = ('finditem',items['ITEM_NEST_BALL'],False,None)
item_labels['ShoalCave_LowTideEntranceRoom_EventScript_ItemBigPearl'] = ('finditem',items['ITEM_BIG_PEARL'],False,None)
item_labels['ShoalCave_LowTideInnerRoom_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['ShoalCave_LowTideStairsRoom_EventScript_ItemIceHeal'] = ('finditem',items['ITEM_ICE_HEAL'],False,None)
item_labels['ShoalCave_LowTideIceRoom_EventScript_ItemTM07'] = ('finditem',items['ITEM_TM07'],True,None)
item_labels['ShoalCave_LowTideIceRoom_EventScript_ItemNeverMeltIce'] = ('finditem',items['ITEM_NEVER_MELT_ICE'],False,None)
item_labels['SeafloorCavern_Room9_EventScript_ItemTM26'] = ('finditem',items['ITEM_TM26'],True,None)
item_labels['Route110_TrickHousePuzzle1_EventScript_ItemOrangeMail'] = ('finditem',items['ITEM_ORANGE_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle2_EventScript_ItemHarborMail'] = ('finditem',items['ITEM_HARBOR_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle2_EventScript_ItemWaveMail'] = ('finditem',items['ITEM_WAVE_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle3_EventScript_ItemShadowMail'] = ('finditem',items['ITEM_SHADOW_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle3_EventScript_ItemWoodMail'] = ('finditem',items['ITEM_WOOD_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle4_EventScript_ItemMechMail'] = ('finditem',items['ITEM_MECH_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle6_EventScript_ItemGlitterMail'] = ('finditem',items['ITEM_GLITTER_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle7_EventScript_ItemTropicMail'] = ('finditem',items['ITEM_TROPIC_MAIL'],False,None)
item_labels['Route110_TrickHousePuzzle8_EventScript_ItemBeadMail'] = ('finditem',items['ITEM_BEAD_MAIL'],False,None)
item_labels['VictoryRoad_1F_EventScript_ItemMaxElixir'] = ('finditem',items['ITEM_MAX_ELIXIR'],False,None)
item_labels['VictoryRoad_1F_EventScript_ItemPPUp'] = ('finditem',items['ITEM_PP_UP'],False,None)
item_labels['VictoryRoad_B1F_EventScript_ItemTM29'] = ('finditem',items['ITEM_TM29'],False,None)
item_labels['VictoryRoad_B1F_EventScript_ItemFullRestore'] = ('finditem',items['ITEM_FULL_RESTORE'],False,None)
item_labels['VictoryRoad_B2F_EventScript_ItemFullHeal'] = ('finditem',items['ITEM_FULL_HEAL'],False,None)
item_labels['ArtisanCave_B1F_EventScript_ItemHPUp'] = ('finditem',items['ITEM_HP_UP'],False,None)
item_labels['ArtisanCave_1F_EventScript_ItemCarbos'] = ('finditem',items['ITEM_CARBOS'],False,None)
item_labels['MagmaHideout_1F_EventScript_ItemRareCandy'] = ('finditem',items['ITEM_RARE_CANDY'],False,None)
item_labels['MagmaHideout_2F_2R_EventScript_MaxElixir'] = ('finditem',items['ITEM_MAX_ELIXIR'],False,None)
item_labels['MagmaHideout_2F_2R_EventScript_ItemFullRestore'] = ('finditem',items['ITEM_FULL_RESTORE'],False,None)
item_labels['MagmaHideout_3F_1R_EventScript_ItemNugget'] = ('finditem',items['ITEM_NUGGET'],False,None)
item_labels['MagmaHideout_3F_2R_EventScript_ItemPPMax'] = ('finditem',items['ITEM_PP_MAX'],False,None)
item_labels['MagmaHideout_4F_EventScript_MaxRevive'] = ('finditem',items['ITEM_MAX_REVIVE'],False,None)
item_labels['MagmaHideout_3F_3R_EventScript_ItemEscapeRope'] = ('finditem',items['ITEM_ESCAPE_ROPE'],False,None)

# Hidden items

hidden_item_labels = {}

hidden_item_labels['MtPyre_Summit_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_ZINC'], False),
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		]

hidden_item_labels['Route110_TrickHouseEnd_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_NUGGET'], False),
		]

hidden_item_labels['Underwater_Route126_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_ULTRA_BALL'], False),
		('bg_hidden_item_event',items['ITEM_STARDUST'], False),
		('bg_hidden_item_event',items['ITEM_PEARL'], False),
		('bg_hidden_item_event',items['ITEM_IRON'], False),
		('bg_hidden_item_event',items['ITEM_YELLOW_SHARD'], False),
		('bg_hidden_item_event',items['ITEM_BIG_PEARL'], False),
		('bg_hidden_item_event',items['ITEM_BLUE_SHARD'], False),
		]

hidden_item_labels['Underwater_Route127_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_STAR_PIECE'], False),
		('bg_hidden_item_event',items['ITEM_HP_UP'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_RED_SHARD'], False),
		]

hidden_item_labels['Route117_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_REPEL'], False),
		]

hidden_item_labels['FallarborTown_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_NUGGET'], False),
		]

hidden_item_labels['Route105_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_BIG_PEARL'], False),
		]

hidden_item_labels['Route109_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_REVIVE'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_GREAT_BALL'], False),
		('bg_hidden_item_event',items['ITEM_ETHER'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['LavaridgeTown_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_ICE_HEAL'], False),
		]

hidden_item_labels['Route120_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		('bg_hidden_item_event',items['ITEM_REVIVE'], False),
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		('bg_hidden_item_event',items['ITEM_ZINC'], False),
		]

hidden_item_labels['AbandonedShip_HiddenFloorRooms_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_ROOM_1_KEY'], False),
		('bg_hidden_item_event',items['ITEM_ROOM_2_KEY'], False),
		('bg_hidden_item_event',items['ITEM_ROOM_4_KEY'], False),
		('bg_hidden_item_event',items['ITEM_ROOM_6_KEY'], False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		]

hidden_item_labels['Route111_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_STARDUST'], False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_PROTEIN'], False),
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		]

hidden_item_labels['Route106_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_POKE_BALL'], False),
		('bg_hidden_item_event',items['ITEM_STARDUST'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['VictoryRoad_B2F_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_ELIXIR'], False),
		('bg_hidden_item_event',items['ITEM_MAX_REPEL'], False),
		]

hidden_item_labels['Underwater_Route124_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_CARBOS'], False),
		('bg_hidden_item_event',items['ITEM_GREEN_SHARD'], False),
		('bg_hidden_item_event',items['ITEM_PEARL'], False),
		('bg_hidden_item_event',items['ITEM_BIG_PEARL'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_CALCIUM'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['Route104_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_SUPER_POTION'], False),
		('bg_hidden_item_event',items['ITEM_POKE_BALL'], False),
		('bg_hidden_item_event',items['ITEM_POTION'], False),
		('bg_hidden_item_event',items['ITEM_ANTIDOTE'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['GraniteCave_B2F_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_EVERSTONE'], False),
		('bg_hidden_item_event',items['ITEM_EVERSTONE'], False),
		]

hidden_item_labels['PetalburgCity_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		]

hidden_item_labels['Route113_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_ETHER'], False),
		('bg_hidden_item_event',items['ITEM_TM32'], True),
		('bg_hidden_item_event',items['ITEM_NUGGET'], False),
		]

hidden_item_labels['Route128_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['Route114_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_CARBOS'], False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_REVIVE'], False),
		]

hidden_item_labels['Route115_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['LilycoveCity_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		('bg_hidden_item_event',items['ITEM_PP_UP'], False),
		('bg_hidden_item_event',items['ITEM_POKE_BALL'], False),
		]

hidden_item_labels['JaggedPass_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_FULL_HEAL'], False),
		('bg_hidden_item_event',items['ITEM_GREAT_BALL'], False),
		]

hidden_item_labels['Route110_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_REVIVE'], False),
		('bg_hidden_item_event',items['ITEM_GREAT_BALL'], False),
		('bg_hidden_item_event',items['ITEM_POKE_BALL'], False),
		('bg_hidden_item_event',items['ITEM_FULL_HEAL'], False),
		]

hidden_item_labels['Route116_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_SUPER_POTION'], False),
		('bg_hidden_item_event',items['ITEM_BLACK_GLASSES'], False),
		]

hidden_item_labels['VictoryRoad_1F_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_ULTRA_BALL'], False),
		]

hidden_item_labels['SafariZone_Northeast_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		('bg_hidden_item_event',items['ITEM_ZINC'], False),
		]

hidden_item_labels['Route121_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_HP_UP'], False),
		('bg_hidden_item_event',items['ITEM_NUGGET'], False),
		('bg_hidden_item_event',items['ITEM_FULL_HEAL'], False),
		('bg_hidden_item_event',items['ITEM_MAX_REVIVE'], False),
		]

hidden_item_labels['Route123_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_SUPER_REPEL'], False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_REVIVE'], False),
		('bg_hidden_item_event',items['ITEM_HYPER_POTION'], False),
		('bg_hidden_item_event',items['ITEM_PP_UP'], False),
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		]

hidden_item_labels['Route108_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_RARE_CANDY'], False),
		]

hidden_item_labels['SafariZone_Southeast_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_PP_UP'], False),
		('bg_hidden_item_event',items['ITEM_FULL_RESTORE'], False),
		]

hidden_item_labels['ArtisanCave_B1F_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_ZINC'], False),
		('bg_hidden_item_event',items['ITEM_CALCIUM'], False),
		('bg_hidden_item_event',items['ITEM_PROTEIN'], False),
		('bg_hidden_item_event',items['ITEM_IRON'], False),
		]

hidden_item_labels['PetalburgWoods_MapBGEvents'] = [
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_POTION'], False),
		('bg_hidden_item_event',items['ITEM_TINY_MUSHROOM'], False),
		('bg_hidden_item_event',items['ITEM_TINY_MUSHROOM'], False),
		('bg_hidden_item_event',items['ITEM_POKE_BALL'], False),
		]

hidden_item_labels['NavelRock_Top_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_SACRED_ASH'], False),
		]

hidden_item_labels['MtPyre_Exterior_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_ULTRA_BALL'], False),
		('bg_hidden_item_event',items['ITEM_MAX_ETHER'], False),
		]

hidden_item_labels['Route118_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_IRON'], False),
		('bg_hidden_item_event',items['ITEM_HEART_SCALE'], False),
		]

hidden_item_labels['Underwater_Route128_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_PROTEIN'], False),
		('bg_hidden_item_event',items['ITEM_PEARL'], False),
		]

hidden_item_labels['Route119_MapBGEvents'] = [
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_CALCIUM'], False),
		('bg_hidden_item_event',items['ITEM_ULTRA_BALL'], False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('ignore',None, False),
		('bg_hidden_item_event',items['ITEM_FULL_HEAL'], False),
		('bg_hidden_item_event',items['ITEM_MAX_ETHER'], False),
		]

hidden_item_labels['SSTidalLowerDeck_MapBGEvents'] = [
		('bg_hidden_item_event',items['ITEM_LEFTOVERS'], False),
		]

pickle.dump((mon_labels,trade_labels,foe_item_labels,foe_labels,item_labels,hidden_item_labels,item_id),args.output)
args.output.close()
