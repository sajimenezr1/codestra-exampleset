from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.storage import SimpleStorageServiceS3

# 'Load balancer with cluster of 5 EC2 instances of the same service conected with same simple S3 storage 
with Diagram('lb-5EC2-S3', direction="TB"):
    lb = ELB('Load Balancer')
    with Cluster("EC2 instances"):
        instances = [EC2('Service 1 instance'), EC2('Service 1 instance'), EC2('Service 1 instance'), EC2('Service 1 instance'), EC2('Service 1 instance')]     
    S3 = SimpleStorageServiceS3('bucket')

    lb >> instances >>  S3