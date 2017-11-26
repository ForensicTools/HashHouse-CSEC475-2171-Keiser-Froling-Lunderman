# Name: hash_Files.ps1
# Desc: recurses through files in the c drive and gets the MD5 hash of all, sending it to a text file

Get-ChildItem -recurse "C:\" | Get-FileHash -Algorithm MD5 | select Hash, Path > c:\Users\Public\OG_hashes.txt