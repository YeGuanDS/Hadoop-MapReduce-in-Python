# Hadoop-MapReduce-in-Python
an Hadoop MapReduce program using Python

#### Hadoop mapper/reducer implemented using Python iterators and generators 
To run the code, first copy your data to HDFS, then
```
bin/hadoop jar /path/to/contrib/streaming/hadoop-streaming*.jar \
          -files /path/to/mapper.py, /path/to/reducer.py \
          -mapper /path/to/mapper.py \
          -reducer /path/to/reducer.py \
          -input /path/to/input/folder/* \
          -output /path/to/output
```
