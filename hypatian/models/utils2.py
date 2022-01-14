"""shuzhai.models.utils."""
from hypatian.models import (
	InventoryLocation,
	RequisitionOrderStatus
)

InventoryLocation.create(name='Main Supply Room')
InventoryLocation.create(name='North Wing')
InventoryLocation.create(name='South Wing')
InventoryLocation.create(name='Car Stock')
InventoryLocation.create(name='Other Requisition')

RequisitionOrderStatus.create(name='Draft')
RequisitionOrderStatus.create(name='Pending')
RequisitionOrderStatus.create(name='Approved')
RequisitionOrderStatus.create(name='Rejected')
RequisitionOrderStatus.create(name='Closed')
