from diagrams import Diagram
from diagrams.aws.compute import EC2

# 'EC2 instance with redundant
with Diagram('EC2-redundant'):
    EC2('App instance') - EC2('App redundant instance')