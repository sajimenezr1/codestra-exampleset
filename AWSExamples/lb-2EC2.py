from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

# 'Load balancer of 2 EC2 instances of the same service in a container
with Diagram('lb-2EC2'):
    lb = ELB('Load Balancer')
    with Cluster('Instances'):
        instances = [EC2('Instance'), EC2('Instance')]
    lb>>instances