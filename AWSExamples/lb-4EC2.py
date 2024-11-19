from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB


# "Load balancer and 4 EC2 instances of app"
with Diagram("lb-4EC2", direction="LR"):
    lb=  ELB("load balancer")
    instances = []
    for _ in range(4):
        ec2Instance = EC2('App instance')
        instances.append(ec2Instance)

    lb >> instances
