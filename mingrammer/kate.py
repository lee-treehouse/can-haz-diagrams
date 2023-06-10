from diagrams import Cluster, Diagram
from diagrams.generic.os import IOS, Android
from diagrams.onprem.client import User, Client
from diagrams.generic.device import Mobile, Tablet

with Diagram("Kate Diagram", show=False, direction="LR"):
    user = User("Kate Bruhn")
    client = Client("Kate's Imac'")
    mobile = Mobile("Kate's Phone")
    tablet = Tablet("Kate's Ipad")

    user >> client
    user >> mobile
    user >> tablet

    apple = IOS("Apple")
    apple2 = IOS("Apple")
    android = Android("pixel")

    client - apple
    tablet - apple2
    mobile - android
