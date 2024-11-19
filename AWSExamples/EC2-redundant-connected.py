from diagrams import Diagram
from diagrams.aws.compute import EC2

# 'EC2 instances connected, each one with redundant
with Diagram('EC2-redundant-connected'):

    instance1 =EC2('App1 redundant instance')- EC2('App1 instance')  
    instance2 = EC2('App2 redundant instance') - EC2('App2 instance') 
    instance1 >> instance2