# ref: https://diagrams.mingrammer.com/

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.general import Client


graph_attr = {
    "fontsize": "45",
    "splines": "curved"
}

with Diagram("Demo App", show=False, graph_attr=graph_attr):

    with Cluster("AWS"):
        apig = APIGateway("API Gateway\nWebSocket API")
        function = Lambda("Lambda")
        table = Dynamodb("DynamoDB")

        apig >> Edge() <<  function >> Edge() << table

    clientA = Client("Client A")
    clientA >> Edge(label="WebSocket") << apig

    clientB = Client("Client B")
    clientB >> Edge(label="WebSocket") << apig
