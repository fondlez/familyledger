.. _cmd_examples:

More Command Line Examples
==========================

The following are more examples showing different ways to use the command line 
options of Family Ledger.

[web] Show me where all my items are
------------------------------------

.. raw:: html

   <div class='cli'>
   &gt; ledger_web --view location
   </div>
   
.. note::
  Since Ledger Web allows selecting any view, this just changes the default 
  view on startup from Character View to Location View.
  
[excel] Give me item ids, not links to Twinhead or Wowhead
----------------------------------------------------------

.. raw:: html

   <div class='cli'>
   &gt; ledger --db id
   </div>

[console] How much gold do I have?
----------------------------------

.. raw:: html

   <div class='cli'>
   &gt; ledger --view factiongold -o -
   </div>

::

  realm	faction	gold
  Kronos	Horde	135820g 69s 85c
  Kronos	Alliance	1814g 90s 29c


**Advanced**: let us put this in a batch file called `gold.cmd` and
place it in a `c:\\scripts` folder which is on your Windows system PATH. Now 
you can call "gold" from the command line anywhere.

.. code-block:: batch

  @echo off
  rem [Family Ledger] Returns total gold from World of Warcraft accounts.
  c:\utils\familyledger\ledger.exe --log-disable --view factiongold -o - ^
  "C:\Program Files\World of Warcraft 1.12"
  pause
  
[console] How much gold is on each of my characters?
----------------------------------------------------

.. raw:: html

   <div class='cli'>
   &gt; ledger --view gold -o -
   </div>
   
::

  realm	account	faction	character	gold
  Kronos	MALFOY	Horde	draco	135820g 69s 85c
  Kronos	POTTER	Alliance	lily	1125g 85s 81c
  Kronos	POTTER	Alliance	harry	689g 04s 48c

[console] WTB Nexus Crystals
----------------------------

.. raw:: html

   <div class='cli'>
   &gt; ledger --view location -s nexus
   </div>

::

  realm	account	faction	character	item name	item rarity	item quantity	location	item link
  Kronos	MALFOY	Horde	draco	Nexus Crystal	4-Epic	200	bank	https://vanilla-twinhead.twinstar.cz/?item=20725
  Kronos	POTTER	Alliance	harry	Nexus Crystal	4-Epic	1	bags	https://vanilla-twinhead.twinstar.cz/?item=20725
  Kronos	POTTER	Alliance	lily	Nexus Crystal	4-Epic	4	bank	https://vanilla-twinhead.twinstar.cz/?item=20725
  
**Advanced**: let us put this in a batch file called `fam.cmd` and
place it in a `c:\\scripts` folder which is on your Windows system PATH. Now 
you can call "fam" from the command line anywhere, e.g. ``fam nexus`` or ``fam
"major healing"``.

.. code-block:: batch

  @echo off
  rem [Family Ledger] Searches item data from World of Warcraft accounts.
  c:\utils\familyledger\ledger.exe --log-disable --view location -s %* ^
  "C:\Program Files\World of Warcraft 1.12"
  pause

[console] I am desperate, maybe it's in the mail?
-------------------------------------------------

.. raw:: html

   <div class='cli'>
   &gt; ledger --view mail -s plague
   </div>

::

  realm	account	faction	character	item name	item rarity	item quantity	item link
  Kronos	POTTER	Alliance	lily	Plaguebloom	1-Common	20	https://vanilla-twinhead.twinstar.cz/?item=13466
  
.. warning::
  There are known issues with the Mail View (see :ref:`bugs`).