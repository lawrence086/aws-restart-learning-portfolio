# Network Firewall exercise

I worked with stateless forwarding to the stateful engine and Suricata-style rules inspecting HTTP traffic on port 80. I sent `wget` requests using two URI patterns.

One request appeared to hang, so I stopped it. To check whether the firewall rule matched, I’d compare it with a request the firewall should allow and look for a matching entry in the firewall logs.

[Back to AWS labs](README.md)
