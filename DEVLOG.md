# Day 1 - 3/7/22 #

Made the decision to write this with classic python-tcod to take advantage of faster prototyping. Started research on behavior trees since I intend to use them as the basis of the game's main mechanic of semi-automated exploration. The general idea is that, much like in simulations like Dwarf Fortress, the player will not have direct control over the party of adventurers that explore the dungeon. Instead, the player will guide their progress by setting enemy targets, exploration objectives, combat strategy, and character builds. With this simple goal in mind, the plumbing for the screen system has been put in, making use of python-tcod's `tcod.event.EventDispatcher` class. As a rule, I will try to leave the game in a state where it can run after each coding session.

# Day 2 - 3/8/22 #

Very little progress. I had wanted to get the map structure and basic movement in, but work killed most of my desire to code, unfortunately. I have the beginnings of a map class, though I will need to remind myself of the canonical way to display map data in python-tcod.