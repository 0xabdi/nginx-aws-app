# nginx-aws-app
A simple app running on nginx docker container hosted on AWS ECS Fargate cluster.

## Prerequisites
AWS access key and secret key needs to be generated from your AWS account and stored as [Github Action Repository Secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) ( `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`). The AWS region should also be set in the `.github/workflows/deploy.yml` file as `AWS_REGION`.

## Architecture
The architecture diagram was generated using `graphviz` and the `diagrams` python library. Run the following command to generate the diagram on a MacOS machine:
```sh
    brew install graphviz && \
    python3 -m venv env && \
    source env/bin/activate && \
    pip install -r requirements.txt && \
    python diagram.py
```

## Opportunities for Improvement
1. Serve content on port 443 using HTTPs instead of on port 80.
2. Instead of using AWS access key and secet key to authenticate to the AWS account, use [GitHub OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/using-openid-connect-to-authenticate-to-aws) to authenticate to AWS. This will remove the need to store AWS access key and secret key in GitHub secrets thereby reducing the attack surface in case the secrets get comprmised since OIDC tokens are short-lived.
3. Instead of directly using terarform `resource` blocks, use terraform modules to create reusable components. This will make the code more modular and easier to maintain.
4. Use [Terraform Cloud](https://www.terraform.io/cloud) or `s3` backend to manage the terraform state file instead of storing it in a local file. This will make it easier to collaborate with other team members and manage the state file.
5. ...

## References
Some of the terraform code used in this repo was adapted from "[Using Terraform and Fargate to create Amazon’s ECS](https://medium.com/@olayinkasamuel44/using-terraform-and-fargate-to-create-amazons-ecs-e3308c1b9166)"
