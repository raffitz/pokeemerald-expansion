#!/usr/bin/env python

import argparse
import pickle

parser = argparse.ArgumentParser(description='Get offsets for the randomizer')
parser.add_argument('labels',type=argparse.FileType('rb'),help='The randomizable labels list (from randomizer-make-list.py)')
parser.add_argument('table',type=open,help='The symbols table (objdump -t pokeemerald.elf > file.table)')
parser.add_argument('binary',type=argparse.FileType('rb'),help='The binary rom (pokeemerald.gba)')
parser.add_argument('output',type=argparse.FileType('wb'),help='The output offsets file')

args = parser.parse_args()

(mon_labels,trade_labels,foe_item_labels,foe_labels,item_labels,hidden_item_labels,max_id) = pickle.load(args.labels)

mon_addresses = set()
trade_addresses = set()
foe_item_addresses = set()
foe_addresses = set()
item_addresses = set()
hidden_item_addresses = set()

# Mons Format: (Address, Catch Em All, exclusive ID)
mons = []
# Items Format: (Address, type, exclusive ID associated)
items = []


def process_mon(address,data,label):
	global mons
	global items
	(entry_types,more_data) = data
	for entry_type in entry_types:
		# print('DEBG \t%s'%entry_type)
		if entry_type == 'Starters':
			# 3 starters, data adjacent
			for i in range(3):
				# print('DEBG \t\tAdding entry')
				mons.append((address + 2*i, False, None))
		elif entry_type == 'LandMons':
			# 12 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(12):
				# print('DEBG \t\tAdding entry')
				mons.append((address + 2 + 4*i, True, None))
		elif entry_type == 'WaterMons':
			# 5 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(5):
				# print('DEBG \t\tAdding entry')
				mons.append((address + 2 + 4*i, True, None))
		elif entry_type == 'FishingMons':
			# 10 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(10):
				# print('DEBG \t\tAdding entry')
				mons.append((address + 2 + 4*i, True, None))
		elif entry_type == 'RockSmashMons':
			# 5 mon table, first two bytes of each entry are level boundaries (unchanged), second two are pokemon
			for i in range(5):
				# print('DEBG \t\tAdding entry')
				mons.append((address + 2 + 4*i, True, None))
		elif entry_type == 'hard':
			# No previous data
			if more_data is None:
				print('WARN hard entry type without any data %s'%label)
				continue
			(eid,even_more_data) = more_data
			# print('DEBG \t\tAdding entry')
			mons.append((address, False, eid))
			# print('DEBG \t\tAdding entry')
			mons.append((address + 2, False, eid + 1))
		else:
			# print('DEBG \tprocessing script command %s'%entry_type)
			# Script command
			if more_data is None:
				print('WARN script cmd %s entry type without any data %s'%(entry_type,label))
				continue
			(eid,even_more_data) = more_data
			if even_more_data is None:
				print('WARN script cmd %s entry type without pokemon data %s'%(entry_type,label))
				continue
			(pokemon,item) = even_more_data
			if entry_type == 'bufferspeciesname':
				# 0x7d 0xSI 0xPKMN
				start = address
				limit = address + 128
				entry = None
				mismatch = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0x7d:
						_string_id = args.binary.read(1)
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 2, False, eid)
							address = start + 4
						else:
							mismatch = pkmn
					start += 1
				if entry is None:
					if mismatch is None:
						print('WARN script cmd %s did not find cmd byte 0x7d within range %s'%(entry_type,label))
					else:
						print('WARN script cmd %s pkmn mismatch %d != %d %s'%(entry_type,pokemon,mismatch,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			elif entry_type == 'giveegg':
				# 0x7a 0xPKMN
				start = address
				limit = address + 128
				entry = None
				mismatch = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0x7a:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 1, False, eid)
							address = start + 3
						else:
							mismatch = pkmn
					start += 1
				if entry is None:
					if mismatch is None:
						print('WARN script cmd %s did not find cmd byte 0x7a within range %s'%(entry_type,label))
					else:
						print('WARN script cmd %s pkmn mismatch %d != %d %s'%(entry_type,pokemon,mismatch,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			elif entry_type == 'givemon':
				# 0x79 0xPKMN 0xLV 0xITEM ...
				start = address
				limit = address + 128
				entry = None
				mismatch_item = None
				mismatch_mon = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0x79:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							if item is not None:
								_lvl = args.binary.read(1)
								item_bin = args.binary.read(2)
								item_read = int.from_bytes(item_bin, byteorder='little', signed=False)
								if item_read == item:
									items.append((start + 4,'gift',eid))
									entry = (start + 1, False, eid)
									address = start + 6
								else:
									mismatch_item = item_read
							else:
								items.append((start + 4,'gift',eid))
								entry = (start + 1, False, eid)
								address = start + 6
						else:
							mismatch_mon = pkmn
					start += 1
				if entry is None:
					if mismatch_item is not None:
						print('WARN script cmd %s item mismatch %d != %d %s'%(entry_type,item,mismatch_item,label))
					elif mismatch_mon is not None:
						print('WARN script cmd %s pkmn mismatch %d != %d %s'%(entry_type,pokemon,mismatch_mon,label))
					else:
						print('WARN script cmd %s did not find cmd byte 0x79 within range %s'%(entry_type,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			elif entry_type == 'playmoncry':
				# 0xa1 0xPKMN ...
				start = address
				limit = address + 128
				entry = None
				mismatch = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0xa1:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 1, False, eid)
							address = start + 3
						else:
							mismatch = pkmn
					start += 1
				if entry is None:
					if mismatch is None:
						print('WARN script cmd %s did not find cmd byte 0xa1 within range %s'%(entry_type,label))
					else:
						print('WARN script cmd %s pkmn mismatch %d != %d %s'%(entry_type,pokemon,mismatch,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			elif entry_type == 'setvar':
				# 0x16 0xVADD 0xPKMN
				start = address
				limit = address + 128
				entry = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0x16:
						_var_address = args.binary.read(2)
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 3, False, eid)
							address = start + 5
					start += 1
				if entry is None:
					print('WARN script cmd %s did not find cmd byte 0x16 within range %s'%(entry_type,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			elif entry_type == 'setwildbattle':
				# 0xb6 0xPKMN 0xLV 0xITEM ...
				start = address
				limit = address + 128
				entry = None
				mismatch_item = None
				mismatch_mon = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0xb6:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							if item is not None:
								_lvl = args.binary.read(1)
								item_bin = args.binary.read(2)
								item_read = int.from_bytes(item_bin, byteorder='little', signed=False)
								if item_read == item:
									items.append((start + 4,'gift',eid))
									entry = (start + 1, False, eid)
									address = start + 6
								else:
									mismatch_item = item_read
							else:
								items.append((start + 4,'gift',eid))
								entry = (start + 1, False, eid)
								address = start + 6
						else:
							mismatch_mon = pkmn
					start += 1
				if entry is None:
					if mismatch_item is not None:
						print('WARN script cmd %s item mismatch %d != %d %s'%(entry_type,item,mismatch_item,label))
					elif mismatch_mon is not None:
						print('WARN script cmd %s pkmn mismatch %d != %d %s'%(entry_type,pokemon,mismatch_mon,label))
					else:
						print('WARN script cmd %s did not find cmd byte 0xb6 within range %s'%(entry_type,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			elif entry_type == 'showmonpic':
				# 0x75 0xPKMN ...
				start = address
				limit = address + 128
				entry = None
				mismatch = None
				while entry == None and start < limit:
					args.binary.seek(start)
					b = args.binary.read(1)
					if int.from_bytes(b,byteorder='little',signed=False) == 0x75:
						pkmn_bin = args.binary.read(2)
						pkmn = int.from_bytes(pkmn_bin, byteorder='little', signed=False)
						if pkmn == pokemon:
							entry = (start + 1, False, eid)
							address = start + 3
						else:
							mismatch = pkmn
					start += 1
				if entry is None:
					if mismatch is None:
						print('WARN script cmd %s did not find cmd byte 0x75 within range %s'%(entry_type,label))
					else:
						print('WARN script cmd %s pkmn mismatch %d != %d %s'%(entry_type,pokemon,mismatch,label))
				else:
					# print('DEBG \t\tAdding entry')
					mons.append(entry)
			else:
				print('WARN unable to match entry type %s %s'%(entry_type,label))

id_counter = max_id

def process_trade(address,data,label):
	global mons
	global items
	global id_counter
	for entry in data:
		args.binary.seek(address)
		(pkmn,item,requested) = entry
		# struct defined in src/trade.c
		_nickname = args.binary.read(11)	# POKEMON_NAME_LENGTH + 1		11	11	0x0b
		_noise = args.binary.read(1)		# PADDING				1	12	0x0c
		species = args.binary.read(2)		#					2	14	0x0e
		_ivs = args.binary.read(6)		# NUM_STATS				6	20	0x14
		_abn = args.binary.read(1)		#					1	21	0x15
		_noise = args.binary.read(3)		# PADDING				3	24	0x18
		_otid = args.binary.read(4)		#					4	28	0x1c
		_cond = args.binary.read(5)		# CONTEST_CATEGORIES_COUNT		5	33	0x21
		_noise = args.binary.read(3)		# PADDING				3	36	0x24
		_pers = args.binary.read(4)		#					4	40	0x28
		hitem = args.binary.read(2)		#					2	42	0x2a
		_mail = args.binary.read(1)		#					1	43	0x2b
		_otname = args.binary.read(11)		#					11	54	0x36
		_otgndr = args.binary.read(1)		#					1	55	0x37
		_sheen = args.binary.read(1)		#					1	56	0x38
		tradereq = args.binary.read(2)		#					2	58	0x3a
		_noise = args.binary.read(2)		# PADDING				3	36	0x3c
		species_i = int.from_bytes(species, byteorder='little', signed=False)
		if species_i != pkmn:
			print('WARN in-game-trade pkmn mismatch %d != %d %s'%(pkmn,species_i,label))
		else:
			mons.append((address + 0x0c,False,id_counter))
		hitem_i = int.from_bytes(hitem, byteorder='little', signed=False)
		if hitem_i != item:
			print('WARN in-game-trade held item mismatch %d != %d %s'%(item,hitem_i,label))
		else:
			items.append((address + 0x28,'gift',id_counter))
		tradereq_i = int.from_bytes(tradereq, byteorder='little', signed=False)
		if tradereq_i != requested:
			print('WARN in-game-trade request mismatch %d != %d %s'%(requested,tradereq_i,label))
		else:
			mons.append((address + 0x38,False,None))
		address += 0x3c
		id_counter += 1

def process_foe_item(address,data,label):
	global mons
	global items
	global id_counter
	for entry in data:
		args.binary.seek(address)
		(pkmn,item) = entry
		# struct defined in include/data.h
		_iv = args.binary.read(2)
		_lvl = args.binary.read(1)
		_noise = args.binary.read(1)
		species = args.binary.read(2)
		hitem = args.binary.read(2)

		species_i = int.from_bytes(species, byteorder='little', signed=False)
		if species_i != pkmn:
			print('WARN foe item pkmn mismatch %d != %d %s'%(pkmn,species_i,label))
		else:
			mons.append((address + 0x0c,False,id_counter))
		hitem_i = int.from_bytes(hitem, byteorder='little', signed=False)
		if hitem_i != item:
			print('WARN foe item item mismatch %d != %d %s'%(item,hitem_i,label))
		else:
			items.append((address + 0x28,'held',id_counter))
		address += 8
		id_counter += 1

def process_foe(address,data,label):
	global mons
	global items
	global id_counter
	for pkmn in data:
		args.binary.seek(address)
		# struct defined in include/data.h
		_iv = args.binary.read(2)
		_lvl = args.binary.read(1)
		_noise = args.binary.read(1)
		species = args.binary.read(2)

		species_i = int.from_bytes(species, byteorder='little', signed=False)
		if species_i != pkmn:
			print('WARN foe pkmn mismatch %d != %d %s'%(pkmn,species_i,label))
		else:
			mons.append((address + 0x0c,False,id_counter))
		address += 8
		id_counter += 1

def process_item(address,data,label):
	global mons
	global items
	global id_counter
	(entry_type,item,item_type,eid) = data
	if entry_type == 'pc':
		args.binary.seek(address)
		item_bin = args.binary.read(2)
		item_read = int.from_bytes(item_bin, byteorder='little', signed=False)
		if item_read != item:
			print('WARN pc item mismatch %d != %d %s'%(item_read,item,label))
		else:
			items.append((address,item_type,eid))
	elif entry_type == 'giveitem' or entry_type == 'finditem':
		# giveitem and finditem are actually a couple of setorcopyvars and calls to functions
		# 0x1a 0xVADD 0xITEM
		start = address
		limit = address + 128
		entry = None
		mismatch = None
		while entry == None and start < limit:
			args.binary.seek(start)
			b = args.binary.read(1)
			if int.from_bytes(b,byteorder='little',signed=False) == 0x1a:
				_vaddr = args.binary.read(2)
				item_bin = args.binary.read(2)
				item_read = int.from_bytes(item_bin, byteorder='little', signed=False)
				if item == item_read:
					entry = (start + 3,item_type,eid)
				else:
					mismatch = item_read
			start += 1
		if entry is None:
			if mismatch is not None:
				print('WARN script cmd %s item mismatch %d != %d %s'%(entry_type,item,mismatch,label))
			else:
				print('WARN script cmd %s did not find cmd byte 0x1a within range %s'%(entry_type,label))
		else:
			# print('DEBG \t\tAdding entry')
			items.append(entry)
	else:
		print('WARN unable to match entry type %s %s'%(entry_type,label))
		

STRUCT_SIZE = 12

def process_hidden_item(address,data,label):
	global mons
	global items
	global id_counter
	for entry in data:
		(entry_type,item,item_type) = entry
		if entry_type == 'ignore':
			address += STRUCT_SIZE
		elif entry_type == 'bg_hidden_item_event':
			args.binary.seek(address)
			_x = args.binary.read(2) #		0	2
			_y = args.binary.read(2) #		2	2
			_elv = args.binary.read(1) #		4	1
			_knd = args.binary.read(1) #		5	1
			_noise = args.binary.read(2) #		6	2
			item_bin = args.binary.read(2) #	8	2
			# flag					a	1
			# zero					b	1
			# inc _num_signs			c	2?
			# total size: 14			e
			item_read = int.from_bytes(item_bin, byteorder='little', signed=False)
			if item == item_read:
				items.append((address + 8,item_type,None))
			else:
				print('WARN hidden item mismatch %d != %d %s'%(item,item_read,label))
			address += STRUCT_SIZE
		else:
			print('WARN unable to match entry type %s %s'%(entry_type,label))
			address += STRUCT_SIZE


lines = args.table.readlines()

for line in lines:
	elements = line.split()
	if len(elements) == 0:
		continue
	if elements[-1] in mon_labels:
		# print('DEBG %s'%elements[-1])
		try:
			value = int(elements[0],16) - 0x8000000
			# print('DEBG \taddress = %d'%value)
			data = mon_labels[elements[-1]]
			process_mon(value,data,elements[-1])
			mon_addresses.add(elements[-1])
		except ValueError:
			pass
	if elements[-1] in trade_labels:
		try:
			value = int(elements[0],16) - 0x8000000
			# print('DEBG \taddress = %d'%value)
			data = trade_labels[elements[-1]]
			process_trade(value,data,elements[-1])
			trade_addresses.add(elements[-1])
		except ValueError:
			pass
	if elements[-1] in foe_item_labels:
		try:
			value = int(elements[0],16) - 0x8000000
			# print('DEBG \taddress = %d'%value)
			data = foe_item_labels[elements[-1]]
			process_foe_item(value,data,elements[-1])
			foe_item_addresses.add(elements[-1])
		except ValueError:
			pass
	if elements[-1] in foe_labels:
		try:
			value = int(elements[0],16) - 0x8000000
			# print('DEBG \taddress = %d'%value)
			data = foe_labels[elements[-1]]
			process_foe(value,data,elements[-1])
			foe_addresses.add(elements[-1])
		except ValueError:
			pass
	if elements[-1] in item_labels:
		try:
			value = int(elements[0],16) - 0x8000000
			# print('DEBG \taddress = %d'%value)
			data = item_labels[elements[-1]]
			process_item(value,data,elements[-1])
			item_addresses.add(elements[-1])
		except ValueError:
			pass
	if elements[-1] in hidden_item_labels:
		try:
			value = int(elements[0],16) - 0x8000000
			# print('DEBG \taddress = %d'%value)
			data = hidden_item_labels[elements[-1]]
			process_hidden_item(value,data,elements[-1])
			hidden_item_addresses.add(elements[-1])
		except ValueError:
			pass

missing_mons = set(mon_labels.keys()).difference(mon_addresses)
for label in missing_mons:
	print('WARN missing mon label %s'%label)

missing_trades = set(trade_labels.keys()).difference(trade_addresses)
for label in missing_trades:
	print('WARN missing trade label %s'%label)

missing_foe_item = set(foe_item_labels.keys()).difference(foe_item_addresses)
for label in missing_foe_item:
	print('WARN missing foe item label %s'%label)

missing_foe= set(foe_labels.keys()).difference(foe_addresses)
for label in missing_foe:
	print('WARN missing foe label %s'%label)

missing_item = set(item_labels.keys()).difference(item_addresses)
for label in missing_item:
	print('WARN missing item label %s'%label)

missing_hidden_item = set(hidden_item_labels.keys()).difference(hidden_item_addresses)
for label in missing_hidden_item:
	print('WARN missing hidden item label %s'%label)

pickle.dump((mons,items),args.output)
args.output.close()
