# Use the Hadoop base image
FROM harisekhon/hadoop

# Install Python and pip (CentOS uses yum)
RUN yum install -y python3 python3-pip

# Set working directory for your project
WORKDIR /app

# Copy project files
COPY requirements.txt ./
COPY src/ ./src/
COPY data/ ./data/
COPY scripts/ ./scripts/

# Install Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Make Python scripts and shell scripts executable
RUN chmod +x /app/src/*.py
RUN chmod +x /app/scripts/*.sh

# The base image automatically:
# - Starts all Hadoop services (HDFS, YARN)
# - Exposes ports 8088 (YARN) and 9870 (HDFS)

# Keep the default command that starts Hadoop services