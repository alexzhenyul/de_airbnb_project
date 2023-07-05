# Terraform - AWS infrastructre setup

### 
1. ec2 instances (airflow/kafka)
2. s3 buckets (raw/stage/analytical)

### download homebrew
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew tap hashicorp/tap
brew install terraform
terraform -version
```

### Terraform Installation on ec2 instance
1. Download Binary
   ```curl -O https://releases.hashicorp.com/terraform/0.12.16/terraform_0.12.16_linux_amd64.zip```
2. Unzip the binary to /usr/bin
   ```unzip terraform_0.12.16_linux_amd64.zip -d /usr/bin/```
3. check Terraform version
   ```terraform -v```
4. write the terraform main.tf for cloud infrastructure file
5. run terraform init command
   ```terraform init```
6. run terraform plan command
   ```terraform plan```
7. run terraform apply command and type "yes" to confirm
   ```terraform apply```