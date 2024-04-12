from ninja import NinjaAPI
from apps.customers.api import router as customers_router

api = NinjaAPI(
  title='Authentication and Authorization Demo App'
)

api.add_router('customers/', customers_router)