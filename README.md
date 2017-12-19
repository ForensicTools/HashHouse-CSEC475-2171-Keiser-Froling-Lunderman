# HashHouse-CSEC475-2171-Keiser-Froling-Lunderman

Authors:
 - Rebecca Froling
 - Morgan Keiser
 - Alex Lunderman

This repository is for our forensic tool called HashHouse. 
It will offer the ability to compare a complete set of hash files from a clean OS installation to a hash set from the same machine after the installation of any application of the users choosing.
This comparison will allow for users to know which files supposed to exist after a clean install.

Other Improvements:
- Will also be able test the post-application installation hash set for known malicious files.

Files included:
- hashFiles.py: Python script to do an MD5 hash on all files of an OS. Currently have the hashing part done. Has the ability to identify Windows OS versions 7, 8, and 10. Added the ability to use the OS identification to figure out the set of base hash files to compare the local set to. Has a comparison method that takes the base OS hashes and compares the local hashes so that all the unmatched hashes from the local machine are written to an output file.
- hash\_Files.ps1: PowerShell script that will output all the hashes of a clean Windows OS installation within the C-drive
