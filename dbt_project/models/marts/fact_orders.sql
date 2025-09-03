{{ config(materialized='table', schema='analytics') }}

with o as (
  select * from {{ ref('stg_orders') }}
),
oi as (
  select * from {{ ref('stg_order_items') }}
),
pmt as (
  select order_id, sum(payment_value) as total_payment
  from {{ ref('stg_order_payments') }}
  group by order_id
)
select
  oi.order_item_id,
  o.order_id,
  o.customer_id,
  oi.product_id,
  oi.seller_id,
  o.purchase_ts::date as order_date,
  oi.price,
  oi.freight_value,
  coalesce(pmt.total_payment, 0) as total_payment
from oi
join o on oi.order_id = o.order_id
left join pmt on o.order_id = pmt.order_id
