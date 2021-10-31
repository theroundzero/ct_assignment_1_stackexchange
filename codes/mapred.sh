
hadoop jar /usr/lib/hadoop/hadoop-streaming-3.2.2.jar -files map1.py,red1.py -mapper 'python map1.py' -reducer 'python red1.py' -input hdfs://assignment-1-m/owner_entries/$1 -output hdfs://assignment-1-m/output/output1

hadoop jar /usr/lib/hadoop/hadoop-streaming-3.2.2.jar -files map2.py,red2.py -mapper 'python map2.py' -reducer 'python red2.py' -input hdfs://assignment-1-m/output/output1/ -output hdfs://assignment-1-m/output/output2

hadoop jar /usr/lib/hadoop/hadoop-streaming-3.2.2.jar -files map3.py,red3.py -mapper 'python map3.py' -reducer 'python red3.py' -input hdfs://assignment-1-m/output/output2/ -output hdfs://assignment-1-m/output/output3

hadoop jar /usr/lib/hadoop/hadoop-streaming-3.2.2.jar -files map4.py -numReduceTasks 0 -input hdfs://assignment-1-m/output/output3/ -output hdfs://assignment-1-m/output/output4 -mapper 'python map4.py'

hdfs dfs -getmerge hdfs://assignment-1-m/output/output4 tfidResults/$1

hdfs dfs -rm -r /output/output*

