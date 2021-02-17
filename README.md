# Pokémon Emerald Plus Dynamic Offset Randomizer

## Motivation

I wanted an upgraded Gen 3 game (like the sort-of-binary-but-not-really CFRU or the decomp-based Emerald Expansion) but randomized.

I tried to fiddle with the Universal Pokémon Randomizer's internals, but Java gives me a headache.

Instead, I decided to build my own makeshift randomizer in python. I also decided that I would do this with the Emerald Expansion.

## Problem

This presents an interesting question: if I just hunt down the offsets of the bytes I need to change to randomize the game, whenever I add or remove something and recompile the game, those offsets will misalign and I'll have to hunt them down all over again.

An alternative is to randomize the source tables and compile a randomized rom. This is a poor solution, though, because recompiling the whole thing is **very** slow. A randomized nuzlocke can have high rates of failure, especially when conforming to level caps. In those circumstances it's usually best to keep a handful of pre-randomized roms ready to swap. Compiling such a handful would cost far more time than it would save, though.

### The Symbol Table

The compilation toolchain employed by this project (and most C/C++ projects, really) produces a nice modern little ELF file, with its nifty symbol tables. The tables and other additional data are then stripped to create the binary ROM file.

But the symbol table can be very useful for our purposes. Rather than have static offsets that need manual change every time the game is updated, we reference the associated labels and scour the symbol tables and the ROM itself for the offsets that need to be randomized.

## Compile and Randomize

In order to compile, follow the toolchain installation procedures detailed [here](INSTALL.md) and [here](https://github.com/pret/pokeemerald/blob/master/INSTALL.md).

In order to randomize, python is required. This has been tested with Python 3.9.1, but most versions > 3.7 should work.

```sh
make -j$(nproc) # compiles the rom

arm-none-eabi-objdump -t pokeemerald.elf > randomizer/pokeemerald.table # Writes the symbol table to a file

randomizer/randomizer-make-list.py include/constants/species.h include/constants/items.h randomizer/reference.pickle randomizer/list.pickle # Parses the Species and Items constant lists and produces a reference lookup table, as well as a list of the symbols which need to be randomized

randomizer/randomizer-offsets.py randomizer/list.pickle randomizer/pokeemerald.table pokeemerald.gba randomizer/offsets.pickle # reads the list of symbols to be randomized, cross-references it with the symbol table, and fine-tunes the address to point exactly to the bytes that need changing

randomizer/randomizer-randomize.py randomizer/reference.pickle randomizer/offsets.pickle pokeemerald.gba randomizer/output.gba -seed RANDOM_SEED # reads the reference lookup table, and the fine-tuned offsets, and puts the randomized pokemon at those offsets.
```

## Simple mods implemented

 * [Highlight the nature boosted and bucked stats (DizzyEgg)](https://www.pokecommunity.com/showpost.php?p=10024409&postcount=21)
 * [Gen VI style Exp. Share (Lunos)](https://www.pokecommunity.com/showpost.php?p=10060538&postcount=26)
 * [Battle interface shows coloured type according to effectiveness (PokemonCrazy)](https://www.pokecommunity.com/showpost.php?p=10167016&postcount=83)
 * [Overworld Poison stops at 1HP (Lunos)](https://www.pokecommunity.com/showpost.php?p=10068565&postcount=32)
 * [Easy bike swap (Lunos)](https://www.pokecommunity.com/showpost.php?p=10161144&postcount=74)
 * [Pokemon Summary Screen shows IVs and EVs with L/R/start (PokemonCrazy)](https://www.pokecommunity.com/showpost.php?p=10161688&postcount=77)
 * [Stop Disappearing Berries (Buffel Saft)](https://www.pokecommunity.com/showpost.php?p=10142996&postcount=63)
 * [Badge progression marts (ghoulslash)](https://www.pokecommunity.com/showpost.php?p=10172995&postcount=96)
 * [Multiple Premier Balls in large ball purchases (Buffel Saft)](https://www.pokecommunity.com/showpost.php?p=10178662&postcount=110)
 * [Fast Nurse Joy (TheXaman)](https://www.pokecommunity.com/showpost.php?p=10213415&postcount=164)
 * [Overworld Rotom Changer (Buffel Saft)](https://www.pokecommunity.com/showpost.php?p=10214373&postcount=168)
 * [Better Whiteout Payout (lightbox87)](https://www.pokecommunity.com/showpost.php?p=10137272&postcount=58)
 * [HMs can be overwritten (Lunos)](https://www.pokecommunity.com/showpost.php?p=10182839&postcount=119)
 * [R button enables auto-run (ghoulslash)](https://www.pokecommunity.com/showpost.php?p=10161076&postcount=72)
 * [Running while surfing boosts speed (ghoulslash)](https://www.pokecommunity.com/showpost.php?p=10137446&postcount=59)
   * I modified this to work with auto-run: if a player is auto-running, they're also auto-fast-surfing
 * [No pokemon struct encryption (ghoulslash)](https://www.pokecommunity.com/showthread.php?p=10114674#post10114674)
 * [Repeated potion usage doesn't return to menu (ghoulslash)](https://www.pokecommunity.com/showthread.php?p=10206290#post10206290)
 * [Eggs don't show on Pokecenter animation (ghoulslash)](https://github.com/pret/pokeemerald/wiki/Pokecenters-Disregard-Eggs)
 * [Bag can be sorted by pressing start (ghoulslash)](https://www.pokecommunity.com/showthread.php?p=10167488#post10167488)

## My own modifications to the game

 * National Dex enabled from the start
 * Safari Zone starts out entirely open
 * Lines with Mega Evolutions have a high chance of holding the respective Mega Stone
 * Steven gives all the event tickets before 8th Gym (inspired by Speedchoice)
 * No trade evolutions (inspired by the Universal Randomizer)
 * Easily changed lookup table for the roamer (only the roamer, not the Southern Island overworld event)
 * Devon scientist can revive all fossils
 * Local mart clerks to complement the badge-progressing marts (sort of like in the higher gens)

## Acknowledgements

* [**Pokémon Emerald Decompilation Project**](https://github.com/pret/pokeemerald)
* [**DizzyEgg's Pokeemerald Expansion**](https://github.com/DizzyEggg/pokeemerald)
* [**ROM Hacking Hideout's continuation of the Expansion**](https://github.com/rh-hideout/pokeemerald-expansion)
* [**Decomp Simple Modifications Directory**](https://www.pokecommunity.com/showthread.php?t=416647)
* [**Pokémon Emerald Speedchoice**](https://github.com/ProjectRevoTPP/pokeemerald-speedchoice)
* [**Universal Pokémon Randomizer**](https://pokehacks.dabomstew.com/randomizer/)
