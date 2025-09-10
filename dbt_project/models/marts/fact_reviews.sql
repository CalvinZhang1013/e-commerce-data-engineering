{{ config(materialized='table', schema='analytics') }}

-- fact_reviews.sql 同理
with r as (select * from {{ ref('stg_order_reviews') }}),
     o as (select order_id from {{ ref('fact_orders') }})
select r.* from r join o using (order_id)

