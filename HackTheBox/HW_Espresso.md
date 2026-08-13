comes with a firmware.bin file only 

did a binwalk with the -Y flag to identify CPU architecture 

90105         0x15FF9         ARM executable code, 16-bit (Thumb), little endian, at least 742 valid instructions

ls -lh reveals its only 4.0M in Size 

file firmware.bin only  outputs data 

Running a regular binwalk firmware.bin command outputs 

Decimal Hexadecimal and description of the file 
Decimal and hexadecimal are basically the starting location of what is being described in our output we have an 
ESP image at  4096 or 0x1000
3 ESP32 partition tables at 32768 or 0x8000 32800 or 0x8020 32832 or 0x8040
then another ESP image at 65536 or 0x10000
then a unix path /dev/uart/0 at 65824 or 0x10120



