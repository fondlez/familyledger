Family Ledger
=============

**Family Ledger** is an application for collecting and viewing in-game item data
held in World of Warcraft accounts.

It has only been tested with vanilla World of Warcraft patch 1.12 at this time.

There are actually two programs (scripts) for this application:

* **ledger**: a pure command line program that outputs tabular data to file
  or to console. Available output file formats include Excel, CSV and TSV.
* **ledger_web**: a program that starts a local web service so you can view 
  and refresh item data immediately in your web browser.

|

.. image:: dev/doc/source/_images/demo.png
   :class: center

|

It requires installing the `Possessions addon <https://github.com/Road-block/Possessions>`_ to your World of Warcraft folder.

Download from Releases: https://github.com/anuber-Kronos/familyledger/releases/latest

Alternatively, if you know Python, it is available via ``pip install familyledger`` on the official Python `PyPi package index <https://pypi.org/project/FamilyLedger/>`_.

See the full documentation at: https://familyledger.readthedocs.io
