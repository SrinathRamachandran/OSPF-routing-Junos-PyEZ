# OSPF Configuration Automation (Juniper PyEZ)

A Python script to automate the configuration of OSPF interfaces and areas on Junos devices.
The script uses Juniper PyEZ to connect to routers, apply configuration templates, and commit changes — making routing deployments faster and more scalable in lab environments.

✨ Features

Configure IP addresses and enable OSPF on Junos interfaces

Assign interfaces to specific OSPF areas

Template-driven workflow for scalable deployment across multiple routers

Designed for lab and learning environments

🛠 Tech Stack

Python 3

Juniper PyEZ

Jinja2 (templating)

Junos OS

🚀 Usage
python3 ospf_config.py 


Where devices.yaml contains router connection details and interface/area assignments.

📌 Example

Configure ge-0/0/0.0 on router 1 into OSPF area 0

Configure ge-0/0/1.0 on router 2 into OSPF area 1

📚 Status

✅ Lab project as part of networking coursework, demonstrating routing protocol automation and scalability with Juniper Junos.
