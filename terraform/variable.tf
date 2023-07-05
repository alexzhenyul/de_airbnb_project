## AWS account level config: region
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-southeast-2"
}

## Key to allow connection to our EC2 instance
variable "key_name" {
  description = "EC2 key name"
  type        = string
  default     = "airbnb-key"
}

## EC2 instance type
variable "instance_type" {
  description = "Instance type for EC2"
  type        = string
  default     = "m4.xlarge"
}

## Alert email receiver
variable "alert_email_id" {
  description = "Email id to send alerts to "
  type        = string
  default     = "zhenyu.alexl@gmail.com"
}

## Your repository url
variable "repo_url" {
  description = "Repository url to clone into production machine"
  type        = string
  default     = "https://github.com/alexzhenyul/de_airbnb_project.git"
}

variable "aws_access_key"{
  default = "AKIATV7DS2LCJ2W6A46D"
}

variable "aws_secret_key"{
  default = "1il84OWvDpBbekOJIi7WfqRsnxZ0Zpf+xAeoH2vb"
}