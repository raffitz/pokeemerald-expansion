#!/usr/bin/env python

import sys
import argparse
import pickle

parser = argparse.ArgumentParser(description='Build label list')
parser.add_argument('species',type=open,help='The species header (include/constants/species.h)')
parser.add_argument('items',type=open,help='The items header (include/constants/items.h)')
parser.add_argument('output',type=argparse.FileType('wb'),help='The output label file')

args = parser.parse_args()

species = {}

lines = args.species.readlines()

for line in lines:
	elements = line.split()
	if len(elements) < 3:
		continue
	if elements[0] != '#define':
		continue
	if not elements[1].startswith('SPECIES_'):
		continue
	try:
		value = int(elements[2])
		if elements[1] in species:
			print('WARN %s %d %d'%(elements[1],species[elements[1]],value))
		species[elements[1]] = value
	except:
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
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_GiveCyndaquil'] = (['buffername','setvar','givemon'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Chikorita 0x9800
pokemon = species['SPECIES_CHIKORITA']
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_Chikorita'] = (['showmonpic'],(encounter_id,(pokemon,item)))
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_GiveChikorita'] = (['buffername','setvar','givemon'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Totodile 0x9e00
pokemon = species['SPECIES_TOTODILE']
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_Totodile'] = (['showmonpic'],(encounter_id,(pokemon,item)))
mon_labels['LittlerootTown_ProfessorBirchsLab_EventScript_GiveTotodile'] = (['buffername','setvar','givemon'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Beldum 0x7601
pokemon = species['SPECIES_BELDUM']
mon_labels['MossdeepCity_StevensHouse_EventScript_GiveBeldum'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['MossdeepCity_StevensHouse_EventScript_ReceivedBeldumFanfare'] = (['buffername','buffername'],(encounter_id,(pokemon,item)))
encounter_id+=1

### Castform 0x5f01 (HOLDING MYSTIC WATER 0xf800)
pokemon = species['SPECIES_CASTFORM']
item = items['ITEM_MYSTIC_WATER']
mon_labels['Route119_WeatherInstitute_2F_EventScript_ReceiveCastform'] = (['setvar','givemon'],(encounter_id,(pokemon,item)))
mon_labels['Route119_WeatherInstitute_2F_EventScript_ReceivedCastformFanfare'] = (['buffername'],(encounter_id,(pokemon,item)))
encounter_id+=1

item = None

### Wynaut Egg 0x6801
pokemon = species['SPECIES_WYNAUT']
mon_labels['LavaridgeTown_EventScript_EggWoman'] = (['giveegg'],None)

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
mon_labels['sRoamerMons'] = (['hard'],(encounter_id,(pokemon,item)))
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

# Trades
trade_labels = {}

trade_labels['sIngameTrades'] = [
		(species['SPECIES_SEEDOT'],items['ITEM_CHESTO_BERRY'],species['SPECIES_RALTS']), # Seedot, Chesto berry, Ralts
		(species['SPECIES_PLUSLE'],items['ITEM_WOOD_MAIL'],species['SPECIES_VOLBEAT']), # Plusle, Wood Mail, Volbeat
		(species['SPECIES_HORSEA'],items['ITEM_WAVE_MAIL'],species['SPECIES_BAGON']), # Horsea, Wave Mail, Bagon
		(species['SPECIES_MEOWTH'],items['ITEM_RETRO_MAIL'],species['SPECIES_SKITTY']), # Meowth, Retro Mail, Skitty
		]

pickle.dump([mon_labels,trade_labels],args.output)
