with src as (
  select * from {{ source('olist','order_reviews') }}
)
select
  review_id,
  order_id,
  review_score,
  review_comment_title,
  review_comment_message,
  review_creation_date::timestamp as creation_ts,
  review_answer_timestamp::timestamp as answer_ts
from src
