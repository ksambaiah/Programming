# Set Hadoop-specific environment variables here.

# The only required environment variable is JAVA_HOME. All others are
# optional. When running a distributed configuration it is best to
# set JAVA_HOME in this file, so that it is correctly defined on
# remote nodes.

# The java implementation to use. Required.
export JAVA_HOME=/usr/java/jdk1.path_location
export HADOOP_HOME_WARN_SUPPRESS=1

# Hadoop home directory
export LD_LIBRARY_PATH=/usr/hdp/2.8.0.0/hadoop/lib/native
export HADOOP_HOME=${HADOOP_HOME:-/usr/hdp/current/hadoop-client}

# Hadoop Configuration Directory
#TODO: if env var set that can cause problems
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-/etc/hadoop/conf}

# Path to jsvc required by secure HDP 2.0 datanode
export JSVC_HOME=/usr/lib/bigtop-utils

# The maximum amount of heap to use, in MB. Default is 1000.
export HADOOP_HEAPSIZE="8192"

# Extra Java runtime options. Empty by default.
export HADOOP_OPTS="-Djava.net.preferIPv4Stack=true ${HADOOP_OPTS}"

# Extra Java runtime options. Empty by default.
export HADOOP_GC_OPTIONS="-XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=10M -verbose:gc -XX:+PrintGCDateStamps -XX:+PrintGCDetails -XX:+PrintGCTimeStamps"

# Command specific options appended to HADOOP_OPTS when specified
export HADOOP_NAMENODE_OPTS="-server -XX:ParallelGCThreads=8 -XX:+UseConcMarkSweepGC -XX:ErrorFile=/local/logs/hadoop/$USER/hs_err_pid%p.log -XX:NewSize=6552m -XX:MaxNewSize=6552m -Xloggc:/local/logs/hadoop/$USER/gc-nn.log ${HADOOP_GC_OPTIONS} -Xms61440m -Xmx61440m -Dhadoop.security.logger=INFO,DRFAS -Dhdfs.audit.logger=INFO,ZIPRFA ${HADOOP_NAMENODE_OPTS}"

export HADOOP_SECONDARYNAMENODE_OPTS="-server -XX:ParallelGCThreads=8 -XX:+UseConcMarkSweepGC -XX:ErrorFile=/local/logs/hadoop/$USER/hs_err_pid%p.log -XX:NewSize=6000m -XX:MaxNewSize=6000m -Xloggc:/local/logs/hadoop/$USER/gc-snn.log ${HADOOP_GC_OPTIONS} -Xms60559m -Xmx60559m -Dhadoop.security.logger=INFO,DRFAS -Dhdfs.audit.logger=INFO,DRFAAUDIT ${HADOOP_SECONDARYNAMENODE_OPTS}"

HADOOP_DATANODE_OPTS="-server -Xloggc:/local/logs/hadoop/$USER/gc-dn.log ${HADOOP_GC_OPTIONS} -Xms12288m -Xmx12288m -Dhadoop.security.logger=ERROR,DRFAS -XX:ParallelGCThreads=8 -XX:+UseConcMarkSweepGC -XX:MaxGCPauseMillis=1000 ${HADOOP_DATANODE_OPTS}"

HADOOP_BALANCER_OPTS="-server -Xmx4096m ${HADOOP_BALANCER_OPTS}"

# The following applies to multiple commands (fs, dfs, fsck, distcp etc)
export HADOOP_CLIENT_OPTS="-Xmx${HADOOP_HEAPSIZE}m $HADOOP_CLIENT_OPTS"
# On secure datanodes, user to run the datanode as after dropping privileges
export HADOOP_SECURE_DN_USER=${HADOOP_SECURE_DN_USER:-hdfs}

# Extra ssh options. Empty by default.
export HADOOP_SSH_OPTS="-o ConnectTimeout=5 -o SendEnv=HADOOP_CONF_DIR"

# Where log files are stored. $HADOOP_HOME/logs by default.
export HADOOP_LOG_DIR=/local/logs/hadoop/$USER

# History server logs
export HADOOP_MAPRED_LOG_DIR=/local/logs/mapred/$USER

# Where log files are stored in the secure data environment.
export HADOOP_SECURE_DN_LOG_DIR=/local/logs/hadoop/$HADOOP_SECURE_DN_USER

# File naming remote slave hosts. $HADOOP_HOME/conf/slaves by default.
# export HADOOP_SLAVES=${HADOOP_HOME}/conf/slaves

# host:path where hadoop code should be rsync'd from. Unset by default.
# export HADOOP_MASTER=master:/home/$USER/src/hadoop

# Seconds to sleep between slave commands. Unset by default. This
# can be useful in large clusters, where, e.g., slave rsyncs can
# otherwise arrive faster than the master can service them.
# export HADOOP_SLAVE_SLEEP=0.1

# The directory where pid files are stored. /tmp by default.
export HADOOP_PID_DIR=/var/run/hadoop/$USER
export HADOOP_SECURE_DN_PID_DIR=/var/run/hadoop/$HADOOP_SECURE_DN_USER

# History server pid
export HADOOP_MAPRED_PID_DIR=/var/run/hadoop-mapreduce/$USER


# A string representing this instance of hadoop. $USER by default.
export HADOOP_IDENT_STRING=$USER

# The scheduling priority for daemon processes. See 'man nice'.

# export HADOOP_NICENESS=10

# Use libraries from standard classpath
JAVA_JDBC_LIBS=""
#Add libraries required by mysql connector
for jarFile in `ls /usr/share/java/*mysql* 2>/dev/null`
do
 JAVA_JDBC_LIBS=${JAVA_JDBC_LIBS}:$jarFile
done
#Add libraries required by oracle connector
for jarFile in `ls /usr/share/java/*ojdbc* 2>/dev/null`
do
 JAVA_JDBC_LIBS=${JAVA_JDBC_LIBS}:$jarFile
done
#Add libraries required by nodemanager
#MAPREDUCE_LIBS=/usr/lib/hadoop-mapreduce/*
#export HADOOP_CLASSPATH=${HADOOP_CLASSPATH}${JAVA_JDBC_LIBS}:${MAPREDUCE_LIBS}
MAPREDUCE_LIBS=/usr/hdp/current/hadoop-mapreduce-client/*
export HADOOP_CLASSPATH=${HADOOP_CLASSPATH}${JAVA_JDBC_LIBS}:${MAPREDUCE_LIBS}:${JAVA_LIBRARY_PATH}

if [ -d "/usr/lib/tez" ]; then
 export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/usr/lib/tez/*:/usr/lib/tez/lib/*:/etc/tez/conf
fi

# Setting path to hdfs command line
#export HADOOP_LIBEXEC_DIR=/usr/lib/hadoop/libexec
export HADOOP_LIBEXEC_DIR=/usr/hdp/current/hadoop-client/libexec

#Mostly required for hadoop 2.0
export JAVA_LIBRARY_PATH=${JAVA_LIBRARY_PATH}:/usr/hdp/current/hadoop-client/lib/native/lib

# For hadoop metrics to TSDB.
if [ -e /opt/user/jars/metrics_tsdb.jar ]; then
 export HADOOP_CLASSPATH=${HADOOP_CLASSPATH}:/opt/user/jars/metrics_tsdb.jar
fi

