TOOL KITS 

Since you cant read raw compiled binary code (.exe, .elf) with a normal text editor you need some tools to look under the hood 

- Static analysis(Disassemblers/Decompilers) - turns raw bytes back into readable assembly language or an approximation of C code
	- GHIDRA
- Dynamic Analysis (Debuggers) -lets you run the program one single instruction at a time, watch the CPU registers, lets you see exactly what is in memory while the program is running
	- x64dbg - for windows binaries 
	- GDB(with GEF or Pwndbg extensions) -Linux binaries 



WORKFLOW

Step A : reconnaissance (Information gathering)
- Check the file type: use file (on Linux) to see if its a 32-bit or 64-bit binary and whether its compiled for windows or Linux
- Look for Strings: Run a "Strings" search on the binary. If you see some text like "Incorrect, password" or "Success". this is where the program handles success and failure 

