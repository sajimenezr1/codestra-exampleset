from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

# 'Load balancer of 2 EC2 instances of the same service  each one with one redundant intance 
with Diagram('lb-2EC2Redundant', direction="TB"):
    lb = ELB('Load Balancer')
    instances = []
    for _ in range(2):
        ec2 = EC2('Service 1 instance')
        redundantEC2 = EC2('Redundant service 1 instance')
        instances.append(redundantEC2 - ec2)
    lb >> instances