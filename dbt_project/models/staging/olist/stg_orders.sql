with src as (
  select * from {{ source('olist','orders') }}
)
, casted as (
  select
    order_id,
    customer_id,
    order_purchase_timestamp::timestamp as purchase_ts,
    order_status,
    order_approved_at::timestamp       as approved_ts,
    order_delivered_customer_date::timestamp as delivered_ts
  from src
)
select * from casted

