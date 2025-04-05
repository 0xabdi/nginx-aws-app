# nginx-aws-app
A simple app running on nginx docker container on AWS

## Authentication to aws account
```sh
    aws configure
```

## Diagram
```sh
    brew install graphviz
    python3 -m venv env && \
    source env/bin/activate && \
    pip install -r requirements.txt && \
    python diagram.py
```

## Trade offs made
- The app is not monitored, as there is no monitoring or logging in place. In a real-world scenario, you would have monitoring and logging in place to ensure that you can troubleshoot issues and monitor the health of the application.
- The app is not automated, as there is no CI/CD pipeline in place. In a real-world scenario, you would have a CI/CD pipeline in place to automate the deployment of the application.
- The app is not tested, as there are no tests in place. In a real-world scenario, you would have tests in place to ensure that the application is working as expected.
- I would let the app serve content on port 443 using HTTPs. However, I didn't have the time to configure the SSL certificate. In a real-world scenario, you would have an SSL certificate in place to ensure that the application is secure.
- I would pull from private registry like ECR instead of public registry like Docker Hub. However, I didn't have the time to configure the ECR. In a real-world scenario, you would have a private registry in place to ensure that the application is secure.
