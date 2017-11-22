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
- hashFiles.py: an in-the-works Python script to do an MD5 hash on all files of an OS. Currently have the hashing part done. Has the differing operating systems to be able to be told apart, so that they can run down two tracks in the script, either UNIX or Windows. Added the ability to use the OS identification to figure out the root directory for directory walk to gather all files from a machine. Also started to look at how to write the output hashes to the output file.

