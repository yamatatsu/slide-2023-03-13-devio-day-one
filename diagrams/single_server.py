# ref: https://diagrams.mingrammer.com/

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import Dynamodb
from diagrams.aws.general import Client


graph_attr = {
    "fontsize": "45",
    "splines": "curved"
}

with Diagram("Single Server", show=False, graph_attr=graph_attr):

    with Cluster("AWS"):
        server = EC2("Server")
        table = Dynamodb("DynamoDB")

        server >> Edge() << table

    clientA = Client("Client A")
    clientA >> Edge(label="WebSocket") << server

    clientB = Client("Client B")
    clientB >> Edge(label="WebSocket") << server
