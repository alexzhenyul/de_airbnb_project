# Data Engineering Project - Airbnb

### Project Description
This project aims to utilize exploratory data analysis and machine learning techniques to accurately predict rental prices for Airbnb listings. In addition to the analytical and modeling aspects, the project will prioritize the implementation of data engineering best practices. This includes establishing a robust data infrastructure on AWS using Terraform and adhering to Infrastructure as Code principles. The project will also create a simulated real-world environment by developing ETL pipelines and orchestrating them through Airflow. The main objective is to generate meaningful insights and address below business problems, which will be visualized and presented in a user-friendly dashboard format. By integrating data analysis, machine learning, and data engineering, this project offers a comprehensive end-to-end solution, delivering valuable insights to support data-driven decision-making.

### Business problems
1. Analyze the key factors influencing the pricing of Airbnb listings.
2. Develop a regression model to accurately forecast the logarithm of rental prices.
3. Conduct exploratory data analysis to gain insights and understand patterns in the data.
4. Perform sentiment analysis on reviews to evaluate the overall sentiment towards Airbnb listings.

### Airbnb Dataset

```http://insideairbnb.com/get-the-data```

The following Airbnb activity is included in this Victoria Airbnb dataset for this project:
-  Melbourne, Barwon South West & Mornington Peninsula

1. Listings: detailed listings data including full descriptions and average review score;
2. Calendar: detailed calendar data for listings, including listing id and the price and availability for that day;
3. Reviews, detailed review data for listings including unique id for each reviewer and detailed comments;
4. Listings-Summary: summary information and metrics for listings (good for visualisations);
5. Reviews-Summary: summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing);
6. Neigborhoods: neighborhood list for geo filter. Sourced from city or open source GIS files;

### Data modeling 
![Data Modeling Diagram](/PNG/airbnb_er_diagram.png)

### Architecture diagram
![Architecture diagram](/PNG/airbnb_Architecture_diagram.png)

### Workflow
1. Setup data infrastructure (EC2 & s3 Buckets)
2. Configure EC2 for airflow, kafka, postgre
3. develop extract & ingestion pipeline into s3 raw bucket
  * Listings.csv - Batch processing (From Postgre to s3)
  * reviews.csv - Streaming processing (From Kafka to s3)
4. build transformation pipeline into s3 stage bucket
  * data modelling format
  * remove duplication, null entries & error
  * data quality check
  * data enrichment (datetimeline level for more granular view)
5. Conduct exploratory data analysis and forecasting with regression to predict listing's rental price using listings data
6. Perform sentiment analysis on reviews to evaluate the overall sentiment towards listings
7. Visualize findings via PowerBI delivering valuable insights
8. Adapt CI/CD principle into project for continuous delivery  

### Technologies
* Amazon Web Services
  * Multiple S3 Buckets: Data Lake (Raw/Stage/Prod)
  * Redshift: Data Warehouse
  * Boto3: AWS SDK Python
* Docker: Containerization
    * Docker-Compose: define and run multi-container docker application
    * Postgre Database
    * pgAdmin: web-based GUI tool to interactive with Postgre Database
    * Airflow: Workflow orchestration
    * dbt: Data transformation & quality check
    * Kafka: Streaming (Producer & Consumer)
* Terraform: Infrastructure-as-Code (IaC)
* Spark: Distributed Processing
* Kafka: Streaming
* GitHub: Version Control
* PowerBI: Business intelligence & Visualization

### Conclusion

### Improvement
-  Implement kafka via IaC