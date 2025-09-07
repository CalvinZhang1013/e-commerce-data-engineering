{{ config(materialized='table', schema='analytics') }}

select distinct
  seller_id
from {{ ref('stg_order_items') }}
