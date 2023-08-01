import pandas as pd
from pandasql import sqldf as ps

listing_df = pd.read_csv("data/listings.csv")
calendar_df = pd.read_csv("data/calendar.csv")


## Modify dataframe into fact & dimension table

# dimension table for airbnb listings
dim_listings_columns = ['id', 'listing_url', 'host_id', 'name', 'description', 'neighborhood_overview', 'picture_url', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms_text', 'beds', 'amenities']
dim_listings = listing_df[dim_listings_columns]
dim_listings = dim_listings.rename(columns={'id': 'listing_id', 'name': 'listing_name', 'description': 'listing_description'}).sort_values(by=['listing_id'], ascending=True)
dim_listings.info()

## bathrooms field is evolved from number to textual description (Example: 2 bathrooms/1 Shared bathroom)

# dimension table for airbnb hosts 
dim_hosts = listing_df.iloc[:, 9:27]

# Dimension table for review stats
dim_review_stats = listing_df.iloc[:, [0] + list(range(56, len(listing_df.columns)))]
dim_review_stats = dim_review_stats.rename(columns={'id': 'listing_id'}).sort_values(by=['listing_id'], ascending=True)


# converting calendar date column into datetime format
calendar_df['date'] = pd.to_datetime(calendar_df['date'])

# Data enrichment for datetime in various level
calendar_df['year'] = calendar_df['date'].dt.year
calendar_df['month'] = calendar_df['date'].dt.month
calendar_df['day'] = calendar_df['date'].dt.day
calendar_df['quarter'] = calendar_df['date'].dt.quarter
calendar_df['weekday'] = calendar_df['date'].dt.weekday
calendar_df['week'] = calendar_df['date'].dt.week


# Dimension table for datetime
dim_datetime_columns = ['date', 'year', 'month', 'day','quarter', 'weekday', 'week']
dim_datetime = calendar_df[dim_datetime_columns]
dim_datetime['datetime_id'] = dim_datetime.index
dim_datetime = dim_datetime[['datetime_id', 'date', 'year', 'month','day','quarter', 'weekday', 'week']]

# Fact table
fact_table_base = calendar_df[[col for col in calendar_df.columns if col not in dim_datetime_columns]]
fact_table_columns = ['listing_id', 'host_id', 'reviewer_id', 'review_id', 'datetime_id', 'available', 'price', 'minimum_night', 'maximum_night']

# SQL for pandas dataframe to generate fact tabel
fact_tabel_sql = '''
SELECT l.listing_id, h.host_id, rr.reviewer_id, r.review_id, dt.datetime_id, available, price, minimum_night, maximum_night
FROM fact_table_base f 
INNER JOIN list_dim l ON f.listing_id = l.listing_id
INNER JOIN host_dim h ON f.host_id = h.host_id
INNER JOIN reviewer_dim rr ON f.reviewer_id = rr.reviewer_id
INNER JOIN review_dim r ON f.review_id = r.review_id
INNER JOIN datetime_id_dim dt ON f.datetime_id = dt.datetime_id
ORDER BY datetime_id
'''

# rename the columns name
fact_table = ps.sqldf(fact_tabel_sql)
fact_table.rename(columns = fact_table_columns, inplace = True)