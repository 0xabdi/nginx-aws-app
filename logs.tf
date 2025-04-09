# Set up CloudWatch group and log stream and retain logs for 30 days
resource "aws_cloudwatch_log_group" "nginx_log_group" {
  name              = "/ecs/nginx-app"
  retention_in_days = 30

  tags = {
    Name = "nginx-log-group"
  }
}

resource "aws_cloudwatch_log_stream" "nginx_log_stream" {
  name           = "nginx-log-stream"
  log_group_name = aws_cloudwatch_log_group.nginx_log_group.name
}
