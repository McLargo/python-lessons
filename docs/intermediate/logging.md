# Logging

Logging is a very important part of any application. It allows you to track the
code execution and to debug the application. Python has a built-in logging
module that allows you to log messages to the console, to a file, or to a remote
server. In contrast to the `print` function, the logging module is more
complete, allowing you to configure the log level, the log format, and the log
destination.

Logging is based in handlers. A handler is an object that receives the log
messages and decides what to do with them. The logging module has several
built-in handlers, such as `StreamHandler`, `FileHandler`, `RotatingFileHandler`
or `TimedRotatingFileHandler`. But you can create your own handler by inherit
the `Handler` class. [Notifiers](https://github.com/liiight/notifiers) is a 3pp
library that provides with extra handlers with the ability to send notifications
to different services.

## Best practices

- Set different log levels for different environments. For example, you may set
  `DEBUG` level in development and `ERROR` level in production.
- Set a specific format for the log messages, including the timestamp or the log
  level. Using a standard format makes it easier to read the log messages. Use
  the `extra` parameter to pass the data to the log message.
- Use pipelines `|` to separate the different parts of the log message. It can be
  useful to filter the log messages, or even to parse them.
- To include variables in your log message, don't use `format` or `f-string` in
  the log call, instead use the `%s`, like `logger.info('Variable: %s', value)`.
- Use `logging.exception` to log an exception message and the stack trace.
- Set the different logger instance you are going to use with
  `logging.getLogger`. This way you can configure the logger in one place and
  use it in different modules.

## logging library

This is the built-in Python logging library. It is very flexible and allows you
to configure the log level, the log format, and the log destination.

Each logger has a name, and the loggers are organized in a tree-like structure.
The root logger is the top-level logger, and all other loggers are children of
the root logger.

::: src.intermediate.logging.default_logging

::: src.intermediate.logging.custom_logging_format

## loguru library

Loguru is a third-party library that simplifies the logging configuration to the
bare minimum, such as log level and log format. But you can also can configure
much more easily, such as:

- color customization.
- log rotation, retention and compression.
- custom log levels.
- lazy evaluation of log messages.

:::src.intermediate.logging.default_loguru

::: src.intermediate.logging.custom_loguru_format_and_level

## References

- [Python logging module](https://docs.python.org/3/library/logging.html)
- [Loguru repository](https://github.com/Delgan/loguru)
