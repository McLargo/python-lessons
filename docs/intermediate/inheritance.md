# Inheritance

We are going to create a simple example that uses inheritance.

Class `Driver` is the base (abstract) class that represent a generic Driver. It
will contain the one common attribute, one method concrete and one abstract.

Concrete methods are methods that can be called from the base class, and
abstract methods are methods that needs to be implemented in the subclass.

::: src.intermediate.inheritance.inheritance.Driver

Subclass UsaDriver represents a Driver in USA. It defines the novel years and
the metric unit for the speed. Abstract method `speed_limit` is implemented.

::: src.intermediate.inheritance.inheritance.UsaDriver

Subclass SpainDriver represents a Driver in Spain. It defines the novel years
and the metric unit for the speed. Abstract method `speed_limit` is implemented.

::: src.intermediate.inheritance.inheritance.SpainDriver
