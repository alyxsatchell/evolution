#!/bin/bash

docker run -it --rm --workdir /evolution -v /home/adminuser/repos/evolution:/evolution:rw --name evo_sim -p 127.0.0.1:8001:5000 pyflask /bin/sh -c '. /evolution/start_evo_and_web.sh' 
