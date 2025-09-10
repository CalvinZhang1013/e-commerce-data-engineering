-- fact_payments.sql
{{ config(materialized='table', schema='analytics') }}
with p as (select * from {{ ref('stg_order_payments') }}),
     o as (select order_id from {{ ref('fact_orders') }})  -- 或 stg_orders
select p.*
from p
join o using (order_id)

