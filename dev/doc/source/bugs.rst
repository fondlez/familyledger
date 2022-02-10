.. _bugs:

Known Issues and Bugs
=====================

This section lists known issues and bugs and gives some information on how to 
submit bug reports.

Mail
----

Items in mail are sometimes reported incorrectly. This may be due to bug(s)
in the Possessions addon or some other low-level quirk.

Logging and checking the mail on a character may fix the item data, but it is
not guaranteed. There appears to be no way to know beforehand when the mail is 
reporting incorrectly or cannot be fixed.

In addition, valid item ids and therefore item links are usually not present
for mail item data. These will therefore normally appear blank or be omitted
entirely.

For these reasons, mail item data is not included by default in views that do
not show the storage location of items, e.g. in the Item View. If the opposite
is desired, the command line option `--include-mail` forces mail item data to 
such views.

.. _reporting_bugs:

Reporting Bugs
==============

Here are some tips on reporting bugs in Family Ledger.

Upgrade to the latest version
-----------------------------

The bug you are reporting may already be fixed in the latest version.

Also, check the :ref:`news` section to see what has changed in the latest
versions.

Read the documentation
-----------------------------

Read or search the Family Ledger documentation to see if the issue you are
encountering is already explained.

Use the official Family Ledger Issue tracker on GitHub
------------------------------------------------------

The official Family Ledger 
`Issue tracker is on GitHub <https://github.com/fondlez/familyledger/issues>`_.