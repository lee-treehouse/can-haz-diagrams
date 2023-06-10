from diagrams import Cluster, Diagram, Edge, Node
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.network import PrivateSubnet, PublicSubnet, RouteTable, VPCRouter
from diagrams.aws.general import InternetGateway
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User, Client


with Diagram(
    "Cruddur Network Diagram with Variations",
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
        "nodesep": "0.8",
    },
):
    # route table
    # internet gateway
    #

    # with Cluster("CFN Stack"):
    #     with Cluster("Inputs"):
    #         Blank("")
    #     with Cluster("Outputs"):
    #         Blank("")

    with Cluster(
        "CrdNetVPC", graph_attr={"fontsize": "18", "bgcolor": "white", "margin": "10"}
    ):
        with Cluster(
            "ap-southeast-2c",
            graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "15"},
        ):
            with Cluster(
                "10.0.20.0/24",
                graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "20"},
            ):
                priv3 = PrivateSubnet("CrdNetSubnetPriv3")

            with Cluster(
                "10.0.8.0/24",
                graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "20"},
            ):
                pub3 = PublicSubnet("CrdNetSubnetPub3")
                priv3 - Edge(color="transparent") - pub3

        with Cluster(
            "ap-southeast-2b",
            graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "15"},
        ):
            with Cluster(
                "10.0.16.0/24",
                graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "20"},
            ):
                priv2 = PrivateSubnet("CrdNetSubnetPriv2")

            with Cluster(
                "10.0.4.0/24",
                graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "20"},
            ):
                pub2 = PublicSubnet("CrdNetSubnetPub2")
                priv2 - Edge(color="transparent", style="dashed") - pub2

        with Cluster(
            "ap-southeast-2a",
            graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "15"},
        ):
            with Cluster(
                "10.0.12.0/24",
                graph_attr={"fontsize": "16", "bgcolor": "white", "margin": "20"},
            ):
                priv1 = PrivateSubnet("CrdNetSubnetPriv1")

            with Cluster(
                "10.0.0.0/24",
                graph_attr={
                    "fontsize": "16",
                    "bgcolor": "white",
                    "margin": "20",
                    "margin": "20",
                },
            ):
                pub1 = PublicSubnet("CrdNetSubnetPub1")
                priv1 - Edge(color="transparent", style="dashed") - pub1

        # https://graphviz.org/docs/attrs/fixedsize/
        vpcRouter = VPCRouter(
            "VPC Router",
            fixedsize="true",
            width="0.6",
            height="0.9",
        )

    # examples
    # metrics = Prometheus("metric")
    # metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    pub1 >> Edge(style="dashed") >> vpcRouter
    pub2 >> Edge(style="dashed") >> vpcRouter
    pub3 >> Edge(style="dashed") >> vpcRouter
    priv1 >> Edge(style="dashed") >> vpcRouter
    priv2 >> Edge(style="dashed") >> vpcRouter
    priv3 >> Edge(style="dashed") >> vpcRouter

    routeTable = RouteTable("Route Table")

    internetGateway = InternetGateway(label="Internet Gateway")

    routeTable << Edge(style="dashed", label="local (10.0.0.0/32)") << vpcRouter

    internetGateway << Edge(style="dashed", label="0.0.0.0/32") << routeTable

    # with Cluster(label="foo", graph_attr={"bgcolor": "red"}):
    #     Blank("bar")
    #     [User("Lee"), User("Andrew")]
    #     holly = User("Holly")
    #     kate = User("Kate")
    #     holly - kate
