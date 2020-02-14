.. _views:

Views Explained
===============

The item data from Family Ledger is presented in tables called Views. Views are 
simply different ways to see the same underlying item data. This helps quickly
determine the status of any specific item or helps further processing of the 
data, e.g. summary tables in Excel.

Here are the 8 views currently available, in no specific order:

.. note::
   All data is per server since it never makes sense to aggregate item data 
   across servers.

Factiongold View
----------------

This is the total money across all characters belonging to the same faction, 
i.e. all Alliance or Horde characters.

Gold View
---------

This is the money per character.

Character View
--------------

This lists all the items on each character, regardless of where that item is
stored. It includes items that are worn. 

By default, this view does not include items in the mail because there is no 
way to see where an item comes from (see :ref:`bugs`).

Item View
---------

This lists all the items (per server) and sums up other item information such 
as the total quantity for that item, which character has the most of that item
and how many this maximum item count character holds.

This view never includes items worn on a character. So, Item View and Worn View
complement each other.

By default, this view does not include items in the mail because there is no 
way to see where an item comes from (see :ref:`bugs`).

Location View
-------------

This lists all the items on each character except, unlike the Character View,
it shows the location of the items, i.e. bags, bank, mail or player 
('player' indicates a worn item).

Mail View
---------

This is virtually the same as the Location View, except filtered to show only 
the items in the mail and no item rarity nor link information (see :ref:`bugs`).

Worn View
---------

This lists all items worn on each character. The items are sorted overall by
the total rarity of the currently equipped items on that character and then by
the character slot. It should therefore naturally show first your most geared 
character across all accounts logged out at that time.

Raw View
--------

This is as close as possible to the original data, except in table format and 
with some mappings of identifiers to more meaningful information, e.g. the item 
rarity.
