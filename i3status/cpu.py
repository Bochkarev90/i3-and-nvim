#!/usr/bin/env python3
# install the package "psutil" with the command "pip3 install psutil --user"
import psutil
print(psutil.cpu_percent(interval=1), end='')
