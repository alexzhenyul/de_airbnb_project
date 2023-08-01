import pandas as pd

review_df = pd.read_csv("data/reviews.csv")

# dimension table for airbnb reviewers
dim_reviewers_columns = ['reviewer_id', 'reviewer_name', 'id']
dim_reviewers = review_df[dim_reviewers_columns]
dim_reviewers = dim_reviewers.rename(columns={'id': 'comment_id'}).sort_values(by=['comment_id'], ascending=True)

# dimension table for airbnb reviews
dim_reviews_columns = ['id', 'reviewer_id', 'listing_id', 'date','comments']
dim_reviews = review_df[dim_reviews_columns]
dim_reviews = dim_reviews.rename(columns={'id': 'comment_id', 'date': 'comment_date'}).sort_values(by=['comment_id'], ascending=True)

