terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-2"
}

resource "aws_budgets_budget" "monthly-budget" {
  name = "monthly-budget"
  budget_type = "COST"
  limit_amount = "0.1"
  limit_unit = "USD"
  time_period_start = "2021-09-01_00:00"
  time_unit = "MONTHLY"
}

resource "aws_security_group" "open_ports" {
  name = "open_ports"

  ingress{
      description = "SSH"
      from_port = 22
      to_port = 22
      protocol = "tcp"
      cidr_blocks = [
        "0.0.0.0/0"]
    }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

}

resource "aws_instance" "development_environment" {
  ami = "ami-00399ec92321828f5"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.open_ports.name]

  tags = {
    Name = "DEV ENVIRONMENT"
  }
}

output "IP" {
  value = [aws_instance.development_environment.public_ip]
}
