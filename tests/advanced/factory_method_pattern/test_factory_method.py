"""Tests for the factory method pattern implementation."""

import json

import yaml

from advanced.factory_method_pattern import (
    DataExportService,
    Exporter,
    ExporterFactory,
    JSONExporter,
    JSONExporterFactory,
    YamlExporter,
    YamlExporterFactory,
)


class MockExporter(Exporter):
    """Mock exporter for testing purposes.

    This exporter tracks what data it received and returns a predictable
    output. Useful for testing the DataExportService without real exporters.
    """

    def __init__(self):
        """Initialize the mock exporter."""
        self.export_called = False
        self.last_data = None

    def export(self, data: dict) -> str:
        """Export the data and track the call.

        Args:
            data: The data to be exported.

        Returns:
            A simple string representation for testing.
        """
        self.export_called = True
        self.last_data = data
        return f"MOCK_EXPORT:{data}"


class MockExporterFactory(ExporterFactory):
    """Mock factory for testing purposes.

    This factory creates MockExporter instances and tracks whether
    create_exporter was called. Useful for testing dependency injection.
    """

    def __init__(self):
        """Initialize the mock factory."""
        self.create_called = False
        self.created_exporter = None

    def create_exporter(self) -> Exporter:
        """Create a mock exporter and track the call.

        Returns:
            An instance of MockExporter.
        """
        self.create_called = True
        self.created_exporter = MockExporter()
        return self.created_exporter


class TestJSONExporter:
    """Tests for the JSON exporter."""

    def test_export_with_indent(self):
        """Test JSON export with indentation."""
        exporter = JSONExporter(indent=2)
        data = {"name": "Alice", "age": 30}
        result = exporter.export(data)

        # Verify it's valid JSON
        parsed = json.loads(result)
        assert parsed == data

        # Verify indentation is present
        assert "\n" in result

    def test_export_compact(self):
        """Test JSON export without indentation."""
        exporter = JSONExporter(indent=None)
        data = {"name": "Bob"}
        result = exporter.export(data)

        # Verify it's valid JSON
        parsed = json.loads(result)
        assert parsed == data

        # Compact format has no newlines
        assert "\n" not in result

    def test_export_nested_data(self):
        """Test JSON export with nested structures."""
        exporter = JSONExporter()
        data = {"user": {"name": "Alice", "roles": ["admin", "user"]}}
        result = exporter.export(data)

        parsed = json.loads(result)
        assert parsed == data
        assert parsed["user"]["roles"] == ["admin", "user"]

    def test_export_empty_dict(self):
        """Test JSON export with empty dictionary."""
        exporter = JSONExporter()
        result = exporter.export({})
        assert result == "{}"


class TestYamlExporter:
    """Tests for the YAML exporter."""

    def test_export_block_style(self):
        """Test YAML export with block style (default)."""
        exporter = YamlExporter(default_flow_style=False)
        data = {"name": "Alice", "age": 30}
        result = exporter.export(data)

        # Verify it's valid YAML
        parsed = yaml.safe_load(result)
        assert parsed == data

        # Block style has newlines
        assert "\n" in result

    def test_export_flow_style(self):
        """Test YAML export with flow style."""
        exporter = YamlExporter(default_flow_style=True)
        data = {"name": "Bob"}
        result = exporter.export(data)

        # Verify it's valid YAML
        parsed = yaml.safe_load(result)
        assert parsed == data

    def test_export_nested_data(self):
        """Test YAML export with nested structures."""
        exporter = YamlExporter()
        data = {"user": {"name": "Alice", "roles": ["admin", "user"]}}
        result = exporter.export(data)

        parsed = yaml.safe_load(result)
        assert parsed == data

    def test_export_empty_dict(self):
        exporter = YamlExporter()
        result = exporter.export({})
        parsed = yaml.safe_load(result)
        assert parsed is None or parsed == {}


class TestJSONExporterFactory:
    """Tests for the JSON exporter factory."""

    def test_create_exporter(self):
        """Test creating a JSON exporter."""
        factory = JSONExporterFactory(indent=2)
        exporter = factory.create_exporter()

        assert isinstance(exporter, JSONExporter)
        assert isinstance(exporter, Exporter)
        assert exporter.indent == 2

    def test_create_exporter_default_indent(self):
        """Test creating a JSON exporter with default indent."""
        factory = JSONExporterFactory()
        exporter = factory.create_exporter()

        assert exporter.indent == 4

    def test_created_exporter_works(self):
        """Test that the created exporter actually works."""
        factory = JSONExporterFactory()
        exporter = factory.create_exporter()

        result = exporter.export({"test": "data"})
        parsed = json.loads(result)
        assert parsed == {"test": "data"}


class TestYamlExporterFactory:
    """Tests for the YAML exporter factory."""

    def test_create_exporter(self):
        """Test creating a YAML exporter."""
        factory = YamlExporterFactory(default_flow_style=True)
        exporter = factory.create_exporter()

        assert isinstance(exporter, YamlExporter)
        assert isinstance(exporter, Exporter)
        assert exporter.default_flow_style is True

    def test_create_exporter_default_flow_style(self):
        """Test creating a YAML exporter with default flow style."""
        factory = YamlExporterFactory()
        exporter = factory.create_exporter()

        assert exporter.default_flow_style is False

    def test_created_exporter_works(self):
        """Test that the created exporter actually works."""
        factory = YamlExporterFactory()
        exporter = factory.create_exporter()

        result = exporter.export({"test": "data"})
        parsed = yaml.safe_load(result)
        assert parsed == {"test": "data"}


class TestDataExportService:
    """Tests for the data export service.

    These tests demonstrate WHY the factory pattern is useful:
    - The service works with ANY factory
    - We can easily inject different factories for different formats
    - Testing is easier (we can inject mock factories)
    """

    def test_export_user_report_with_json_factory(self):
        """Test user report export with JSON format."""
        factory = JSONExporterFactory(indent=2)
        service = DataExportService(factory)

        users = [{"name": "Alice", "age": 30}]
        report = service.export_user_report(users)

        # Verify it's valid JSON
        parsed = json.loads(report)
        assert parsed["users"] == users

    def test_export_user_report_with_yaml_factory(self):
        """Test user report export with YAML format."""
        factory = YamlExporterFactory()
        service = DataExportService(factory)

        users = [{"name": "Bob", "age": 25}]
        report = service.export_user_report(users)

        # Verify it's valid YAML
        parsed = yaml.safe_load(report)
        assert parsed["users"] == users

    def test_export_user_report_with_empty_users(self):
        """Test user report export with no users."""
        factory = JSONExporterFactory()
        service = DataExportService(factory)

        report = service.export_user_report([])

        parsed = json.loads(report)
        assert parsed["users"] == []

    def test_export_user_report_with_multiple_users(self):
        """Test user report export with multiple users."""
        factory = JSONExporterFactory()
        service = DataExportService(factory)

        users = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
        ]
        report = service.export_user_report(users)

        parsed = json.loads(report)
        assert len(parsed["users"]) == 3

    def test_service_does_not_know_concrete_type(self):
        """Test that the service works with the abstract factory interface.

        This demonstrates the key benefit: DataExportService doesn't know
        which concrete factory it's using.
        """
        # We can pass ANY factory that implements ExporterFactory
        factories = [
            JSONExporterFactory(),
            YamlExporterFactory(),
        ]

        for factory in factories:
            # Service accepts any factory
            service = DataExportService(factory)
            users = [{"name": "Test"}]

            # And it works regardless of the concrete type!
            report = service.export_user_report(users)
            assert "Test" in report


class TestFactoryPolymorphism:
    """Tests demonstrating polymorphic behavior of factories."""

    def test_all_factories_implement_interface(self):
        """Test that all factories implement the ExporterFactory interface."""
        factories = [
            JSONExporterFactory(),
            YamlExporterFactory(),
        ]

        for factory in factories:
            assert isinstance(factory, ExporterFactory)
            assert hasattr(factory, "create_exporter")
            assert callable(factory.create_exporter)

    def test_all_exporters_implement_interface(self):
        """Test that all exporters implement the Exporter interface."""
        exporters = [
            JSONExporter(),
            YamlExporter(),
        ]

        for exporter in exporters:
            assert isinstance(exporter, Exporter)
            assert hasattr(exporter, "export")
            assert callable(exporter.export)

    def test_factory_returns_correct_interface(self):
        """Test that factories return objects implementing Exporter."""
        factories = [
            JSONExporterFactory(),
            YamlExporterFactory(),
        ]

        for factory in factories:
            exporter = factory.create_exporter()
            assert isinstance(exporter, Exporter)

            # And it should work
            result = exporter.export({"test": "data"})
            assert isinstance(result, str)
            assert len(result) > 0


class TestMockExporter:
    """Tests for the MockExporter class."""

    def test_mock_exporter_tracks_calls(self):
        """Test that MockExporter tracks method calls."""
        exporter = MockExporter()

        # Initially not called
        assert exporter.export_called is False
        assert exporter.last_data is None

        # After calling export
        data = {"test": "data"}
        result = exporter.export(data)

        # Tracks the call
        assert exporter.export_called is True
        assert exporter.last_data == data
        assert result == f"MOCK_EXPORT:{data}"

    def test_mock_exporter_implements_interface(self):
        """Test that MockExporter implements the Exporter interface."""
        exporter = MockExporter()
        assert isinstance(exporter, Exporter)


class TestMockExporterFactory:
    """Tests for the MockExporterFactory class."""

    def test_mock_factory_tracks_calls(self):
        """Test that MockExporterFactory tracks method calls."""
        factory = MockExporterFactory()

        # Initially not called
        assert factory.create_called is False
        assert factory.created_exporter is None

        # After calling create_exporter
        exporter = factory.create_exporter()

        # Tracks the call
        assert factory.create_called is True
        assert factory.created_exporter is exporter
        assert isinstance(exporter, MockExporter)

    def test_mock_factory_implements_interface(self):
        """Test MockExporterFactory implements ExporterFactory interface."""
        factory = MockExporterFactory()
        assert isinstance(factory, ExporterFactory)


class TestDataExportServiceWithMocks:
    """Tests demonstrating how mocks make testing easier.

    These tests show the key benefit of the Factory Method pattern:
    we can inject mock factories for testing without the service knowing.
    """

    def test_service_with_mock_factory(self):
        """Test DataExportService with a mock factory."""
        factory = MockExporterFactory()
        service = DataExportService(factory)

        users = [{"name": "Alice", "age": 30}]
        report = service.export_user_report(users)

        # Verify the factory was used
        assert factory.create_called is True

        # Verify the exporter was called with correct data
        assert factory.created_exporter.export_called is True
        assert factory.created_exporter.last_data == {"users": users}

        # Verify the result
        assert "MOCK_EXPORT" in report

    def test_service_does_not_need_real_exporters_for_testing(self):
        """Test that we can test the service without real exporters.

        This is a huge benefit: we can test DataExportService's logic
        without worrying about JSON parsing, YAML formatting, etc.
        """
        factory = MockExporterFactory()
        service = DataExportService(factory)

        # Test the service logic
        users = [{"name": "Bob"}, {"name": "Alice"}]
        service.export_user_report(users)

        # We can inspect what data was passed to the exporter
        # without dealing with format-specific details
        assert factory.created_exporter.last_data["users"] == users

    def test_mock_works_alongside_real_factories(self):
        """Test that mock factories work the same way as real ones.

        This demonstrates polymorphism: MockExporterFactory follows
        the same interface as JSONExporterFactory and YamlExporterFactory.
        """
        factories = [
            JSONExporterFactory(),
            YamlExporterFactory(),
            MockExporterFactory(),  # Mock works just like the real ones!
        ]

        for factory in factories:
            service = DataExportService(factory)
            users = [{"name": "Test"}]
            report = service.export_user_report(users)

            # All work the same way
            assert isinstance(report, str)
            assert len(report) > 0
