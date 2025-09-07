{{ config(materialized='table', schema='analytics') }}

select
  review_id,
  order_id,
  review_score,
  review_comment_title,
  review_comment_message,
  creation_ts,
  answer_ts
from {{ ref('stg_order_reviews') }}
