class Person:
    self __init__(self, name: str):
        self.name = Name
    
    def__str__(self) -> str:
        return self.name

class Market:
    def __init__(self, num_counters: int = 0):
        self.num_counters = num_counters
        self.customers = {}
        self.total_revenue = 0.0
        def add_customer(self, customer: Person):
            self.customers[customer.name] = customer
            def remove_customeer(self, customer_name: str):
                if customer_name in self.customers:
                    self.customers.pop(customer_name)
                    def record_sale(self, amount: float):
                        self.total_revenue += amount
                        def get_total_revenue(Self) -> float:
                            return self.total_revenue
                        class superMarket(Market):
                            def __init__(self, num_counters: int = 0, loyalty_program: bool = False):
                                super().__init__(num_counters)
                                self.loyalty_program = loyalty_program
                                def enroll_loyalty_member(self, customer: Person):
                                    if self.loyalty_program:
                              