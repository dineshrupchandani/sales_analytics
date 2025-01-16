select o.*,c.*,p.*
from {{ ref("orders_1") }} as o
left join {{ ref("product_1") }} as p
ON O.PROD = P.PROD_ID 
left join {{ ref("customer_1") }} as c 
  on o.customer_id = c.cust_id
  

