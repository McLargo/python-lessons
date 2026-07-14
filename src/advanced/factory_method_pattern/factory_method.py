"""Factory method pattern example in Python.

This module demonstrates the Factory Method pattern through a data export
system. The key is that the DataExportService class can work with ANY factory
that implements

Avoid usage when you know the concrete class you need to or the object to create
is simple.
"""

import json
from abc import ABC, abstractmethod
from typing import Optional

import yaml


class Exporter(ABC):
    """Abstract base class for data exporters.

    This defines the common interface that all exporters must implement.
    The Factory Method pattern allows us to work with this interface
    without knowing the concrete type.
    """

    @abstractmethod
    def export(self, data: dict) -> str:
        """Export the data in a specific format.

        Args:
            data: The data to be exported.

        Returns:
            The exported data as a string.
        """
        pass


class JSONExporter(Exporter):
    """Concrete exporter for JSON format.

    This exporter can be configured with indentation preferences.
    """

    def __init__(self, indent: Optional[int] = 4) -> None:
        """Initialize the JSON exporter with an optional indentation level.

        Args:
            indent: The number of spaces to use for indentation
            in the JSON output. If None, the output will be compact.
            Defaults to 4.
        """
        self.indent = indent

    def export(self, data: dict) -> str:
        """Export the data in JSON format.

        Args:
            data: The data to be exported.

        Returns:
            JSON formatted string.

        """
        return json.dumps(data, indent=self.indent)


class YamlExporter(Exporter):
    """Concrete exporter for YAML format.

    This exporter can be configured with flow style preferences.
    """

    def __init__(self, default_flow_style: Optional[bool] = False) -> None:
        """Initialize the YAML exporter with an optional flow style.

        Args:
            default_flow_style: If True, the output will be in default inline
            style.
            If False, the output will be in block style (multiline).
            Defaults to False.
        """
        self.default_flow_style = default_flow_style

    def export(self, data: dict) -> str:
        """Export the data in YAML format.

        Args:
            data: The data to be exported.

        Returns:
            YAML formatted string.

        """
        return yaml.dump(data, default_flow_style=self.default_flow_style)


class ExporterFactory(ABC):
    """Abstract base class for exporter factories.

    This is the "Creator" in the Factory Method pattern. It defines
    the factory method that subclasses must implement.

    The key insight: code that receives an ExporterFactory doesn't
    know or care which concrete exporter will be created. This
    enables dependency injection and makes code more flexible.
    """

    @abstractmethod
    def create_exporter(self) -> Exporter:
        """Create an exporter instance.

        Returns:
            An instance of a concrete exporter.
        """
        pass


class JSONExporterFactory(ExporterFactory):
    """Concrete factory for creating JSON exporters.

    This factory encapsulates the creation logic for JSON exporters,
    including their configuration.
    """

    def __init__(self, indent: Optional[int] = 4) -> None:
        """Initialize the JSON exporter factory.

        Args:
            indent: The number of spaces to use for indentation
            in the JSON output. If None, the output will be compact.
            Defaults to 4.
        """
        self.indent = indent

    def create_exporter(self) -> Exporter:
        """Create a JSON exporter with the configured indentation.

        Returns:
            An instance of JSONExporter.

        """
        return JSONExporter(indent=self.indent)


class YamlExporterFactory(ExporterFactory):
    """Concrete factory for creating YAML exporters.

    This factory encapsulates the creation logic for YAML exporters,
    including their configuration.
    """

    def __init__(self, default_flow_style: Optional[bool] = False) -> None:
        """Initialize the YAML exporter factory with an optional flow style.

        Args:
            default_flow_style: If True, the output will be in default inline
            style.
            If False, the output will be in block style (multiline).
            Defaults to False.
        """
        self.default_flow_style = default_flow_style

    def create_exporter(self) -> Exporter:
        """Create a YAML exporter with the configured flow style.

        Returns:
            An instance of YamlExporter.

        """
        return YamlExporter(default_flow_style=self.default_flow_style)


class DataExportService:
    """Service that exports data using a factory pattern.

    This class demonstrates the key value of the Factory Method pattern:
    it receives a factory but doesn't know which concrete factory it is.
    This enables dependency injection, making the code flexible and testable.

    The service can work with ANY factory that implements ExporterFactory,
    making it easy to:
    - Change export formats without modifying this code
    - Add new exporters without modifying this code
    - Test with mock factories
    """

    def __init__(self, factory: ExporterFactory):
        """Initialize the data export service with a factory.

        Args:
            factory: The factory to use for creating exporters.
                This is dependency injection - we don't know the concrete type!
        """
        self.factory = factory

    def export_user_report(self, users: list[dict]) -> str:
        """Export a user report using the provided factory.

        Notice: This method has NO IDEA which format will be used!
        The factory determines the concrete exporter type.

        Args:
            users: List of user dictionaries to export.

        Returns:
            The exported data as a string in the format determined
            by the factory.

        """
        exporter = self.factory.create_exporter()
        return exporter.export({"users": users})
