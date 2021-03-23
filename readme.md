
## Software version
* python: 3.6
* docker: 20.10.5
* docker-compose: 1.26.0

## How to run 
### Generate random data
```
cd omnilytics-challenge
python random_data_generator.py
```

### Read and print the output data from previous step
```
python read_print_data.py
```

### Run docker
Docker-compose is used as an easy for volume mount, then the printed values can be exposed to host machine.

```
cd omnilytics-challenge
sudo docker-compose up
```
