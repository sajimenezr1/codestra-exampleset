from diagrams import Diagram
from diagrams.aws.database import RDS
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.storage import SimpleStorageServiceS3

# "Load balancer with no cluster and 3 EC2 instances connected to same RDS"
with Diagram("lb-3EC2-rds", direction="TB", outformat="jpg") as diag:
    ELB("load balancer") >> [EC2("backend instance"),
                  EC2("backend instance"),
                  EC2("backend instance"),
                  EC2("backend instance"),
                  EC2("backend instance")] >> RDS("database")
