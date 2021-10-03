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

  ingress {
    description = "SSH"
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port = 80
    to_port = 80
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

resource "aws_key_pair" "ssh" {
  key_name = "ssh-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDWmlCsmbMsOhLHbZgydTdIXyVWTQO3alIsh3tV0uJKkug6UG+OyBbhUD+N2zaf69+IAC5lG0ADHt7+iMxCl2y6IAt/DHMBkVAbJV8qCJo4V2PHlg0C+gpvUXAtL14C1k5OjhW04e9lkl9c6j7WhFe73/YtvON0tAzlbn2oumFXEsHJKJGlE4YTvfpj+FhxsucvJPg59WPFIn3MSb3Nfny49sExGYucxWgnw5DG5AoNakhFPVFisKV22qsItKn0QvdZ0FHOlMxeZqNuT0naobXbvJso11abVZRdAtcuFPVkFhPD/2Vms1M7xJt8VPrXfvZChPr4WbvKyoKPpEn2OwufxhPAeAIGOaYzm9FDxyWFUB5UJWj97/IO0XzS0PjDmk+eQlSVaqQPO8dRTo0K7AJEOmHKeEROPv4f64iWVpX5sqqLEpRSsscVP/jKHg7qZcPYF7oOD+BENqP2kQTlj4Aloh84eiAiN1oODaSexQJUCZM7l6qhBcxfxTWOH1/9igc= leo@Leo-pc"
}

resource "aws_instance" "development_environment" {
  ami = "ami-00399ec92321828f5"
  instance_type = "t2.micro"
  key_name = "ssh-key"

  security_groups = [
    aws_security_group.open_ports.name]

  tags = {
    Name = "DEV ENVIRONMENT"
  }
}


output "IP" {
  value = [
    aws_instance.development_environment.public_ip]
}
