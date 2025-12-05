# Weather Distribution MapReduce Project

## Quick Start

### 1. Clone and Build
```bash
git clone https://github.com/Yosef/weather-distrib.git
cd weather-distrib
docker build -t weather-hadoop .
```

### 2. Run the Container
```bash
docker run -d -p 8088:8088 -p 9870:9870 --name weather weather-hadoop
```

### 3. Execute the MapReduce Job
```bash
docker exec -it weather bash
./scripts/run-weather-job.sh
```