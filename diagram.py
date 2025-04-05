# -*- coding: utf-8 -*-
from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC, InternetGateway, RouteTable, ALB
from diagrams.aws.compute import ECS, Fargate
from diagrams.aws.network import PublicSubnet
from diagrams.aws.security import SecurityGroup
from diagrams.aws.devtools import CodeCommit

with Diagram("AWS Fargate Web App Architecture", show=False, direction="TB"):

    with Cluster("VPC: webapp_vpc"):
        igw = InternetGateway("Internet Gateway")
        rt = RouteTable("Route Table")

        with Cluster("Public Subnets"):
            subnet1 = PublicSubnet("Subnet 1 (us-east-1a)")
            subnet2 = PublicSubnet("Subnet 2 (us-east-1b)")

        alb = ALB("Application Load Balancer")
        sg = SecurityGroup("Web Security Group")

        ecs_cluster = ECS("ECS Cluster")
        task = Fargate("nginxdemos/hello Task")
        service = Fargate("Fargate Service")

        igw >> rt >> [subnet1, subnet2]
        [subnet1, subnet2] >> alb >> service
        service >> task
        ecs_cluster >> service
        sg >> alb
