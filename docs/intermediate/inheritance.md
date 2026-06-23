# Inheritance

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 8.5/10 ✅ Excellent

    - Technical Accuracy: 31/35
    - Code Quality: 22/25
    - Educational Value: 20/25
    - Documentation: 12/15

    Last reviewed: June 22, 2026
<!-- markdownlint-enable MD046 -->

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

## Common pitfalls

Don't forget to implement the abstract method in the subclass. If you don't, you
will get a `TypeError` when you try to instantiate the subclass.

Additionally, don't make too many levels of inheritance. It is better to have a
flat hierarchy than a deep one. You can always use composition instead of
inheritance.
