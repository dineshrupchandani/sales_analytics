
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with source_data as (

    select * from {{ source("orders","orders") }}

)

select *,to_date(order_date,'DD-MM-YYYY') as order_dt, 
  year(order_dt) as year,month(order_dt) as month,
  to_varchar(order_dt,'MM-YYYY') as month_year,
  
from source_data

