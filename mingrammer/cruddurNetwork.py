from diagrams import Cluster, Diagram, Edge, Node
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.network import PrivateSubnet, PublicSubnet, RouteTable, VPCRouter
from diagrams.aws.general import InternetGateway
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User, Client


with Diagram("Cruddur Network Diagram", show=True, direction="TB"):
    # route table
    # internet gateway
    #

    # with Cluster("CFN Stack"):
    #     with Cluster("Inputs"):
    #         Blank("")
    #     with Cluster("Outputs"):
    #         Blank("")

    with Cluster("CrdNetVPC"):
        with Cluster("ap-southeast-2c"):
            with Cluster("10.0.20.0/24"):
                priv3 = PrivateSubnet("CrdNetSubnetPriv3")

            with Cluster("10.0.8.0/24"):
                pub3 = PublicSubnet("CrdNetSubnetPub3")
                # priv3 - pub3

        with Cluster("ap-southeast-2b"):
            with Cluster("10.0.16.0/24"):
                priv2 = PrivateSubnet("CrdNetSubnetPriv2")

            with Cluster("10.0.4.0/24"):
                pub2 = PublicSubnet("CrdNetSubnetPub2")
                # priv2 - pub2

        with Cluster("ap-southeast-2a"):
            with Cluster("10.0.12.0/24"):
                priv1 = PrivateSubnet("CrdNetSubnetPriv1")

            with Cluster("10.0.0.0/24"):
                pub1 = PublicSubnet("CrdNetSubnetPub1")
                # priv1 - pub1

        vpcRouter = VPCRouter("VPC Router")

    # examples
    # metrics = Prometheus("metric")
    # metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    pub1 >> vpcRouter
    pub2 >> vpcRouter
    pub3 >> vpcRouter
    priv1 >> vpcRouter
    priv2 >> vpcRouter
    priv3 >> vpcRouter

    routeTable = RouteTable("Route Table")

    internetGateway = InternetGateway(label="Internet Gateway")

    routeTable << Edge(style="dashed", label="local (10.0.0.0/32)") << vpcRouter

    internetGateway << Edge(style="dashed", label="0.0.0.0/32") << routeTable
