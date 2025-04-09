# -*- coding: utf-8 -*-
from diagrams import Diagram, Cluster
from diagrams.aws.network import InternetGateway, ElbApplicationLoadBalancer, NATGateway, RouteTable
from diagrams.aws.compute import Fargate, ElasticContainerServiceContainer
from diagrams.aws.general import InternetAlt1

with Diagram("AWS ECS Fargate Architecture", show=True, direction="TB"):
    internet = InternetAlt1("Internet")
    with Cluster("us-west-2"):
        with Cluster("VPC"):
            igw = InternetGateway("Internet Gateway")
            alb = ElbApplicationLoadBalancer("ALB")
            internet >> alb
            with Cluster("ECS Cluster"):
                with Cluster("us-west-2a"):
                    with Cluster("Public Subnet"):
                        nat_gateway = NATGateway("NAT Gateway")
                        public_route_table = RouteTable("Public Route Table")
                        nat_gateway >> igw
                    with Cluster("Private Subnet"):
                        private_route_table = RouteTable("Private Route Table")
                        private_route_table >> nat_gateway
                        with Cluster("Fargate"):
                            service = Fargate("Fargate Service")
                            task = ElasticContainerServiceContainer("nginxdemos/hello")
                            alb >> service >> task
                            private_route_table
                with Cluster("us-west-2b"):
                    with Cluster("Public Subnet"):
                        nat_gateway = NATGateway("NAT Gateway")
                        public_route_table = RouteTable("Public Route Table")
                        nat_gateway >> igw
                    with Cluster("Private Subnet"):
                        private_route_table = RouteTable("Private Route Table")
                        private_route_table >> nat_gateway
                        with Cluster("Fargate"):
                            service = Fargate("Fargate Service")
                            task = ElasticContainerServiceContainer("nginxdemos/hello")
                            alb >> service >> task
                            private_route_table
