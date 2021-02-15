#!/usr/bin/env python

import argparse
import pickle

parser = argparse.ArgumentParser(description='Get offsets for the randomizer')
parser.add_argument('labels',type=argparse.FileType('rb'),help='The randomizable labels list (from randomizer-make-list.py)')
parser.add_argument('table',type=open,help='The symbols table (objdump -t pokeemerald.elf > file.table)')
parser.add_argument('binary',type=argparse.FileType('rb'),help='The binary rom (pokeemerald.gba)')
parser.add_argument('output',type=argparse.FileType('wb'),help='The output offsets file')

args = parser.parse_args()

(mon_labels,trade_labels) = pickle.load(args.labels)

mon_addresses = set()
trade_addresses = set()

# Mons Format: (Address, Catch Em All, exclusive ID)
mons = []
# Items Format: (Address, is_tm)
items = []


def process_mon(address,data):
	(entry_types,more_data) = data
	for entry_type in entry_types:
		if entry_type == 'Starters':
			# 3 starters, data adjacent
			for i in range(3):
				mons.add((address + 2*i, False, None))
		elif entry_type == 'LandMons':
			# 12 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(12):
				mons.add((address + 2 + 4*i, True, None))
		elif entry_type == 'WaterMons':
			# 5 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(5):
				mons.add((address + 2 + 4*i, True, None))
		elif entry_type == 'FishingMons':
			# 10 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(10):
				mons.add((address + 2 + 4*i, True, None))
		elif entry_type == 'RockSmashMons':
			# 5 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(5):
				mons.add((address + 2 + 4*i, True, None))
		elif entry_type == 'hard':
			# No previous data
			if more_data is None:
				print('WARN hard entry type without any data')
				continue
			(eid,even_more_data) = more_data
			mons.add((address, False, eid))
			mons.add((address + 2, False, eid + 1))
		else:
			# Script command
			if more_data is None:
				print('WARN script cmd %s entry type without any data'%entry_type)
				continue
			(eid,even_more_data) = more_data
			if even_more_data is None:
				print('WARN script cmd %s entry type without pokemon data'%entry_type)
				continue
			(pokemon,item) = even_more_data
			if entry_type == 'bufferspeciesname':
				# 0x7d 0xSI 0xPKMN
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0x7d:
						_string_id = args.binary.read(1)
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 2, False, eid)
							address = start + 4
							break
						else:
							print('WARN script cmd %s pkmn mismatch %d != %d'%(entry_type,pokemon,pkmn))
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0x7d within range'%entry_type)
				else:
					mons.add(entry)
			elif entry_type == 'giveegg':
				# 0x7a 0xPKMN
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0x7a:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 1, False, eid)
							address = start + 3
							break
						else:
							print('WARN script cmd %s pkmn mismatch %d != %d'%(entry_type,pokemon,pkmn))
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0x7a within range'%entry_type)
				else:
					mons.add(entry)
			elif entry_type == 'givemon':
				# 0x79 0xPKMN 0xLV 0xITEM ...
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0x79:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							if item is not None:
								_lvl = args.binary.read(1)
								item_bin = args.binary.read(2)
								item_read = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
								if item_read == item:
									items.add((start + 4,False))
									entry = (start + 1, False, eid)
									address = start + 6
									break
								else:
									print('WARN script cmd %s item mismatch %d != %d'%(entry_type,item,item_read))
							else:
								items.add((start + 4,False))
								entry = (start + 1, False, eid)
								address = start + 6
								break
						else:
							print('WARN script cmd %s pkmn mismatch %d != %d'%(entry_type,pokemon,pkmn))
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0x79 within range'%entry_type)
				else:
					mons.add(entry)
			elif entry_type == 'playmoncry':
				# 0xa1 0xPKMN ...
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0xa1:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 1, False, eid)
							address = start + 3
							break
						else:
							print('WARN script cmd %s pkmn mismatch %d != %d'%(entry_type,pokemon,pkmn))
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0xa1 within range'%entry_type)
				else:
					mons.add(entry)
			elif entry_type == 'setvar':
				# 0x16 0xVADD 0xPKMN
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0x16:
						_var_address = args.binary.read(2)
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 3, False, eid)
							address = start + 5
							break
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0x16 within range'%entry_type)
				else:
					mons.add(entry)
			elif entry_type == 'setwildbattle':
				# 0xb6 0xPKMN 0xLV 0xITEM ...
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0xb6:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							if item is not None:
								_lvl = args.binary.read(1)
								item_bin = args.binary.read(2)
								item_read = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
								if item_read == item:
									items.add((start + 4,False))
									entry = (start + 1, False, eid)
									address = start + 6
									break
								else:
									print('WARN script cmd %s item mismatch %d != %d'%(entry_type,item,item_read))
							else:
								items.add((start + 4,False))
								entry = (start + 1, False, eid)
								address = start + 6
								break
						else:
							print('WARN script cmd %s pkmn mismatch %d != %d'%(entry_type,pokemon,pkmn))
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0xb6 within range'%entry_type)
				else:
					mons.add(entry)
			elif entry_type == 'showmonpic':
				# 0x75 0xPKMN ...
				start = address
				limit = address + 128
				entry = None
				while start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,signed=False) == 0x75:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 1, False, eid)
							address = start + 3
							break
						else:
							print('WARN script cmd %s pkmn mismatch %d != %d'%(entry_type,pokemon,pkmn))
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0x75 within range'%entry_type)
				else:
					mons.add(entry)

lines = args.table.readlines()

for line in lines:
	elements = line.split()
	if len(elements) == 0:
		continue
	if elements[-1] in mon_labels:
		try:
			value = int(elements[0],16) - 0x8000000
			data = mon_labels[elements[-1]]
			process_mon(value,data)
			mon_addresses.add(elements[-1])
		except:
			pass
	# TODO other labels (trades, enemies, items)

missing_mons = mon_addresses.difference(set(mon_labels.keys()))
for label in missing_mons:
	print('WARN missing label %s'%label)

pickle.dump((mons,items),args.output)
