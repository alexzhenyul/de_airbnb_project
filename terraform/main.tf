terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
    profile = "default"
    region = "ap-southeast-2"
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key
}

# Create security group for access to EC2 from your Anywhere
resource "aws_security_group" "sde_security_group" {
  name        = "sde_security_group"
  description = "Security group to allow inbound SCP & outbound 8080 (Airflow) connections"

  ingress {
    description = "Inbound SCP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "sde_security_group"
  }
}

# Create EC2 with IAM role to allow EMR, Redshift, & S3 access and security group 
resource "tls_private_key" "custom_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated_key" {
  key_name_prefix = var.key_name
  public_key      = tls_private_key.custom_key.public_key_openssh
}

data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220420"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}


resource "aws_instance" "airbnb_de_ec2" {
    ami             = data.aws_ami.ubuntu.id
    instance_type   = var.instance_type
    key_name        = aws_key_pair.generated_key.key_name
    security_groups = [aws_security_group.sde_security_group.name]
}



variable "s3_bucket_names" {
  type        = list
  default     = ["raw-bucket-alexl", "stage-bucket-alexl", "prod-bucket-alexl"]
}

resource "aws_s3_bucket" "airbnb_de_buckets" {
  count         = length(var.s3_bucket_names) //count will be 3
  bucket        = var.s3_bucket_names[count.index]
  #region        = "ap-southeast-2"
  force_destroy = true
}

# EC2 budget constraint
resource "aws_budgets_budget" "ec2" {
  name              = "budget-ec2-monthly"
  budget_type       = "COST"
  limit_amount      = "5"
  limit_unit        = "USD"
  time_period_end   = "2024-07-04_00:00"
  time_period_start = "2023-07-04_00:00"
  time_unit         = "MONTHLY"

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 80
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = [var.alert_email_id]
  }
}