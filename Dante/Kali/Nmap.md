Network exploration tool and security / port scanner 



nmap -Pn -sC -sV -oA <NAME HERE> <IP HERE>

-Pn skips ping assumes host is up
-sC runs default NSE scripts 
-sV version detection (probes services repeatedly)
