# Set up airflow in EC2 machine prepared from Terrafrom file

1. ssh into ec2 machine for airflow 
2. run the list of commands

```bash
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo install s3fs
```

3. check if airflow is install successfully

```airflow```

4. To run airflow server and check if airflow is ready alone with username & password

```airflow standalone```

5. Go to ec2 instance, copy the IPv4 IP address and paste it in browser:8080, if can't reach airflow UI, it's due to security group issue.
6. Go to ec2 instance's security group section, click on security group and edit inbound rule, add rule, for the sake of simplicty, add all trafic to anywhere, save it (note this is not the practise)
7. Login using the provided username & password