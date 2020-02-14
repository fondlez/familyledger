.. _ref_ledger_web:

Ledger Web - Program Arguments
==============================

..  code-block:: doscon

    ledger_web.exe -h
    usage: ledger_web.exe [-h] [-V] [-v] [-d] [-q]
                         [--log-level {debug,info,warning,error,critical}]
                         [--log-disable] [--lang LANG]
                         [--db {twinhead,wowhead,classicdb,id}]
                         [--include-mail INCLUDE_MAIL] [--gold-format GOLD_FORMAT]
                         [--view {character,location,mail,item,worn,gold,factiongold,raw}]
                         [folder]

    List possessions stored on accounts in a World of Warcaft vanilla 1.12 folder.
    This program currently requires the Possessions addon to be installed in World
    of Warcraft.

    positional arguments:
      folder                World of Warcraft folder path

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -v, --verbose
      -d, --debug
      -q, --quiet
      --log-level {debug,info,warning,error,critical}
                            level of logging (default: warning)
      --log-disable         disable logging to file
      --lang LANG           language (default: en)
      --db {twinhead,wowhead,classicdb,id}
                            item link database (default: twinhead)
      --include-mail INCLUDE_MAIL
                            include items in mail for views with location
                            ambiguity
      --gold-format GOLD_FORMAT
                            output format for gold (default:"{gold}g {silver:02d}s
                            {copper:02d}c")
      --view {character,location,mail,item,worn,gold,factiongold,raw}
                            view of the data (default: "character" for non-excel)