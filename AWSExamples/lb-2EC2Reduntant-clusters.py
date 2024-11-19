from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

# Load balancer with 2EC2 instances , each one with redundant instance, grouped by Clusters
with Diagram('lb-2EC2Redundant-clusters', direction="TB"):
    lb = ELB('Load balancer')
    with Cluster('instance group'):
        instance =EC2('App redundant instance')- EC2('App instance')  
    with Cluster('instance group 2'):
        instance2 =EC2('App redundant instance')- EC2('App instance') 
    lb >> [instance, instance2]