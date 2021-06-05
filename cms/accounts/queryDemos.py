#*** (1) Returns all customers from customer table
customers = Customer.objects.all()

#(2) Return first customer in table
firstCustomer = Customer.objects.first()

#(3) Returns last customer in table
lastCustomer = Customer.objects.last()

#(4) Returns single customer by name
customerByName = Customer.bojects.get(name="rakesh")

#(5) Return single customer By name
customerById = Customer.objects.get(id=2)

#(6)Return all orders related to fustomer
firstCustomer.order_set.all()

#(7)Return orders custome name: (query parent name)
order = order.objects.first()
parentName = order.customer.customerByName

#(8)Returns products from products table with
products = Product.objects.filter(category="out Door")

#(9)Order/Sort Objects by id
leastToGreater = Product.objects.all().order_by
greaterToLeast = products.all().order_by

#(10)





'''

A: Because there are many different products and this value changes constantly you would most likely not 
want to store tha value in the databsse but rather just make this a function we can run each time we load
the customers profile.
'''

#Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product_name="Ball").count()

#Returns total count for each product orderd 
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] += 1


#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}

#RELATED SET EXAMPLE	
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(parentModel)
	name = models.CharField(max_length=200, null=True)

Parent = parentModel.objects.first()
#Rerurns all child models related to parent 
parent childmodel_set.all()
