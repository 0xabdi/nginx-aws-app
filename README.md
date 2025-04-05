# nginx-aws-app
A simple app running on nginx docker container hosted on AWS ECS Fargate cluster.

## Diagram
```sh
    brew install graphviz
    python3 -m venv env && \
    source env/bin/activate && \
    pip install -r requirements.txt && \
    python diagram.py
```

## Trade offs made
- I would let the app serve content on port 443 using HTTPs. However, I didn't have the time to configure the SSL certificate. In a real-world scenario, you would have an SSL certificate in place to ensure that the application is secure.
- I would pull from private registry like ECR instead of public registry like Docker Hub. However, I didn't have the time to configure the ECR. In a real-world scenario, you would have a private registry in place to ensure that the application is secure.
