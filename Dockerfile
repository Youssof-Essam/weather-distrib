FROM harisekhon/hadoop

# 1. Install necessary system dependencies (Python 2.7 and pip).
# 'epel-release' is often needed on CentOS/RHEL to access older Python 2 packages.
# The core package for Python 2 is often just named 'python' or 'python2'.
RUN yum install -y epel-release && \
    yum install -y python python-pip && \
    yum clean all && \
    rm -rf /var/cache/yum

# Set working directory for your project
WORKDIR /app

# 2. Copy dependencies and install them
COPY requirements.txt ./
# 'pip' should link to the Python 2 environment.
# Note: These versions MUST be Python 2.7 compatible.
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy application code and data
COPY src/ ./src/
COPY data/ ./data/
COPY scripts/ ./scripts/

# 4. Fix permissions for execution
# This is crucial for Hadoop Streaming to execute your scripts.
RUN chmod +x /app/src/*.py
RUN chmod +x /app/scripts/*.sh

# Note: The base image's default CMD will start HDFS and YARN services.
