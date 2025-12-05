#!/bin/bash
# scripts/run-weather-job.sh

echo "=== Setting up HDFS ==="

# Create HDFS directories
hdfs dfs -mkdir -p /input
hdfs dfs -mkdir -p /output

# Remove any existing output
hdfs dfs -rm -r -f /output/weather-results

# Put data files in HDFS (skip if already exists)
for file in /app/data/*; do
    if [ -f "$file" ]; then
        echo "Uploading $(basename "$file") to HDFS..."
        hdfs dfs -put -f "$file" /input/
    fi
done

echo "=== Running MapReduce Job ==="

# Run Hadoop Streaming job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files /app/src/mapper.py,/app/src/reducer.py \
    -mapper "python2 /app/src/mapper.py" \
    -reducer "python2 /app/src/reducer.py" \
    -input /input \
    -output /output/weather-results

echo "=== Job Complete ==="
echo "Results stored in HDFS: /output/weather-results"

# Show first 20 lines of output
echo "=== First 20 lines of output ==="
hdfs dfs -cat /output/weather-results/part-00000 | head -20