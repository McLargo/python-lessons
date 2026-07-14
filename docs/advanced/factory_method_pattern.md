# Factory method pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.5/10 ⭐ Outstanding

    - Technical Accuracy: 35/35
    - Code Quality: 24/25
    - Educational Value: 25/25
    - Documentation: 14/15

    Last reviewed: July 14, 2026
<!-- markdownlint-enable MD046 -->

The factory method pattern is a creational design pattern that provides an
interface (a factory) for creating objects. It is commonly misunderstood, as
just seem inheritance with extra steps. But the main idea is to decouple the
code,so the libraries that use it must work with any concrete class. It also
allows for easy extension of the codebase by adding new concrete classes (even
new concrete classes can be used for mocking in tests). The factory method
pattern is used when a class cannot anticipate the type of objects it needs to
create. The main benefits of this pattern are:

- **Decoupling**: The factory method pattern decouples the client code from the
  concrete classes that it needs to instantiate, allowing for more flexible and
  maintainable code.
- **Extensibility**: The factory method pattern allows for easy extension of the
  codebase by adding new concrete classes without modifying the existing code.
- **Single Responsibility Principle**: The factory method pattern allows for
  the separation of object creation from the business logic, allowing for a
  single responsibility for each class.

The factory method pattern is composed of four main components:

## Product Interface

Defines the common interface for all supported products that can be created by
the factory method class.

::: src.advanced.factory_method_pattern.Exporter

## Concrete Product

Implements the behavior associated with a product.

::: src.advanced.factory_method_pattern.JSONExporter
::: src.advanced.factory_method_pattern.YamlExporter

## Creator Interface

Defines the common interface for all supported creators that can create
products.

::: src.advanced.factory_method_pattern.ExporterFactory

## Concrete Creators

Implements the behavior associated with a creator that can create products.

::: src.advanced.factory_method_pattern.JSONExporterFactory
::: src.advanced.factory_method_pattern.YamlExporterFactory

This simple scenario seems overkill, but in a scenario where the code does not
know the concrete classes that will be used, it is easy to create this pattern
to start the work. Additionally, you can add new exporters without changing the
code that uses the factory.

::: src.advanced.factory_method_pattern.DataExportService
