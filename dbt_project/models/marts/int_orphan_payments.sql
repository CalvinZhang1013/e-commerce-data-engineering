{{ config(materialized='view', schema='analytics') }}

-- int_orphan_payments.sql（可 materialized='view'）
with p as (select * from {{ ref('stg_order_payments') }}),
     o as (select order_id from {{ ref('stg_orders') }})
select p.*
from p
left join o using(order_id)
where o.order_id is null
