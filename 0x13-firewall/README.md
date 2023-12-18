This folder is about firewall. It conatain script that:
- install the ufw firewall and setup a few rules.
- Configure ufw so that it blocks all incoming traffic, except: 22 (SSH), 
  443 (HTTPS SSL) and 80 (HTTP).
- Configure ufw so that it redirects port 8080/TCP to port 80/TCP.
