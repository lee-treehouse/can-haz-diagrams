from diagrams import Cluster, Diagram, Edge, Node
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.network import PrivateSubnet, PublicSubnet, RouteTable, VPCRouter
from diagrams.aws.general import InternetGateway
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User, Client
from diagrams.aws.management import CloudformationTemplate

with Diagram(
    "Cruddur CFN Overview - 10 June 2023",
    show=True,
    direction="TB",
    # labelloc https://graphviz.org/docs/attrs/labelloc/
    # https://graphviz.org/docs/attrs/fontsize/
    # https://graphviz.org/docs/attrs/pad/
    graph_attr={
        "labelloc": "t",
        "fontsize": "24",
        "pad": "0.15",
        "bgcolor": "white",
        "nodesep": "1.2",
    },
):
    with Cluster("cloudformation stuff"):
        Blank("Blank for now")
        templates = [
            CloudformationTemplate("Network"),
            CloudformationTemplate("Other"),
        ]
