from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2

# EC2 instances connected, each one with redundant instance, grouped by Clusters
with Diagram('EC2-redundant-connected-clusters', direction="TB"):
    with Cluster('Application 1'):
        instance1 =EC2('App1 redundant instance')- EC2('App1 instance')  
    with Cluster("Application 2"):
        instance2 = EC2('App2 redundant instance') - EC2('App2 instance') 
    instance1 >> instance2