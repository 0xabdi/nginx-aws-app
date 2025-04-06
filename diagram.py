# -*- coding: utf-8 -*-
from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC, InternetGateway, PublicSubnet, ElbApplicationLoadBalancer
from diagrams.aws.compute import ECS, Fargate
from diagrams.aws.security import IAMRole
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import InternetAlt1

with Diagram("AWS ECS Fargate Architecture", show=True, direction="TB"):
    internet = InternetAlt1("Internet")
    with Cluster("us-west-2"):
        with Cluster("VPC"):
            igw = InternetGateway("Internet Gateway")
            alb = ElbApplicationLoadBalancer("ALB")
            internet >> igw >> alb
            with Cluster("ECS Cluster"):
                with Cluster("us-west-2a"):
                    with Cluster("Public Subnets"):
                        subnet1 = PublicSubnet("Public Subnet 1")
                    with Cluster("Fargate"):
                        task = Fargate("nginxdemos/hello Task")
                        service = Fargate("Fargate Service")
                        iam_role = IAMRole("Task Execution Role")
                        logs = Cloudwatch("CloudWatch Logs")

                        alb >> [subnet1]
                        [subnet1] >> service
                        service >> task >> logs
                        iam_role >> task
                with Cluster("us-west-2b"):
                    with Cluster("Public Subnets"):
                        subnet2 = PublicSubnet("Public Subnet 2")
                    with Cluster("Fargate"):
                        task = Fargate("nginxdemos/hello Task")
                        service = Fargate("Fargate Service")
                        iam_role = IAMRole("Task Execution Role")
                        logs = Cloudwatch("CloudWatch Logs")

                        alb >> [subnet2]
                        [subnet2] >> service
                        service >> task >> logs
                        iam_role >> task
