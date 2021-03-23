FROM python:3

WORKDIR /usr/src/app

CMD [ "/bin/sh", "-c", "python read_print_data.py > docker_output_print.txt"]