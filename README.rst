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

Alternatively, if you have Python (3.4.4 or higher), it is available via ``pip install familyledger`` from the official Python `PyPi package index <https://pypi.org/project/FamilyLedger/>`_.

See the full documentation at: https://familyledger.readthedocs.io

Frequently Asked Questions (FAQ)
--------------------------------

**Q. Does this application connect to the Internet?**

No.

This application requires no Internet access to work and nor does it ever attempt to connect to the Internet.

*Verification*: run any Internet monitor, firewall or anti-virus, including the built-in Windows Resource Monitor or firewall that will inform you if an application tries to access the Internet, especially newly installed programs. Power users have access to tools like Microsoft's Sysinternals TCPView or the famous NirSoft's CurrPorts for more detailed checks.

**Q. What files does this application access?**

This application only accesses the file contents of its own folder, any provided World of Warcraft folder, and Python naturally uses any system temporary directories, e.g. the user's system temporary directory in ``%USERPROFILE%\AppData\Local\Temp``.

*Verification*: run Nirsoft's ProcessActivityView or Microsoft's Sysinternals Process Monitor. The truly security paranoid power users can use sandbox tools like Shade, Sandboxie or even a virtual machine to check file access.

**Q. What data collection does this application make?**

None, if that is meant in the sense of data being sent outside of your own system.

*Verification*: follow the verification steps for Internet access and file access. In addition, the program is entirely open source so the code can be read.

**Q. How can I trust your Release executables?**

The good news is that you do not have to trust them. Since the program is fully open source, you can just download and run the program code yourself if wanted to. Since they are pure Python scripts with no binary extensions, you now know exactly what the code does. If you have Python installed, you can run ``pip install familyledger`` to download and install the Python package from the official Python package index. A similar thing can be achieved by downloading the source code directly from Github and running ``pip install -e .`` to install the code from that directory. Python itself will create stub executables from the scripts' entry points that you can use for convenience. They are just wrappers that use your installed Python plus the scripts.

The bad news is that the Release executables, as unknown executables, can never be fully trusted and there is an entire industry around attempts at such verification. The best I can do for those specific Release executables is: 

* you can upload the executables to `VirusTotal <https://www.virustotal.com>`_ to check for any glaring issues. Note. complaints about signing certificates obviously do not affect functionality because I am the one who is publishing the code and I provide checksums.
* offer checksum files so that they cannot be impersonated which you use together with a third-party checksum utility, e.g. 7-Zip's right-click file "CRC SHA" context menu or `Nirsoft's HashMyFiles <https://www.nirsoft.net/utils/hash_my_files.html>`_ or the very fast command line `Microsoft File Checksum Integrity Verifier (FCIV) <https://support.microsoft.com/en-us/help/841290/availability-and-description-of-the-file-checksum-integrity-verifier-u>`_.

If you have any other questions or feedback, please feel free to contact me.
