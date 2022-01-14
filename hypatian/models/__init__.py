"""hypatian.models.

These imports enable us to make all defined models members of the models module
(as opposed to just their python files)
"""
from hypatian.models.base_table import BaseTable
from hypatian.models.inventory_location import InventoryLocation
from hypatian.models.patient import Patient
from hypatian.models.patient_phone_number import PatientPhoneNumber
from hypatian.models.phone_number_type import PhoneNumberType
from hypatian.models.product import Product
from hypatian.models.product_category import ProductCategory
from hypatian.models.requisition_order import RequisitionOrder
from hypatian.models.requisition_order_status import RequisitionOrderStatus
from hypatian.models.unit_of_measure import UnitOfMeasure
from hypatian.models.user import User


__all__ = [
	'BaseTable'
	'InventoryLocation',
	'Patient',
	'PatientPhoneNumber',
	'PhoneNumberType',
	'Product',
	'ProductCategory',
	'UnitOfMeasure',
	'User'
]
