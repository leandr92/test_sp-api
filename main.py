from sp_api.api import Orders, Tokens
from datetime import datetime, timedelta

credentials = dict(
    refresh_token='',
    lwa_app_id='',
    lwa_client_secret='',
    aws_access_key='',
    aws_secret_key='',
    role_arn=''
)


# test get orders without restricted data work completely
orders_without_rd = Orders(credentials=credentials).get_orders(
    LastUpdatedAfter=(datetime.utcnow() - timedelta(days=1)).isoformat()
)

print("orders_without_rd")
print(orders_without_rd)


# Test get RDT token only don't work
rdt_token = Tokens(credentials=credentials).create_restricted_data_token(restrictedResources=[{
     "method": "GET",
     "path": "/orders/v0/orders",
     "dataElements": ['shippingAddress']
    }
])
print("rdt_token")
print(rdt_token)

# test get orders with restricted data don't work
orders_with_rd = Orders(credentials=credentials).get_orders(
    RestrictedResources=['shippingAddress'],
    LastUpdatedAfter=(datetime.utcnow() - timedelta(days=1)).isoformat()
)

print("orders_with_rd")
print(orders_with_rd)