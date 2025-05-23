#!/usr/bin/env python3
"""
This module provides utilities for handling
and protecting sensitive data in logs and databases.
"""
import re
import logging
import mysql.connector
import os

from mysql.connector import connection
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")
"""
List of personally identifiable information (PII) field names to redact.

These field names correspond to keys expected in log messages, and their values
will be replaced by a redaction string when passed through a RedactingFormatter
"""


class RedactingFormatter(logging.Formatter):
    """
    Formatter for log records that redacts sensitive fields.

    This class extends the default `logging.Formatter` to automatically
    obfuscate sensitive information in log messages before they are output.
    It uses a custom `filter_datum` function to replace specified fields
    with a redaction string.

    Attributes:
        REDACTION (str): The string used to replace sensitive data.
        FORMAT (str): The log message format.
        SEPARATOR (str): Character used to separate fields in the log message.
        fields (List[str]): List of field names to redact from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize a RedactingFormatter instance.

        Args:
            fields (List[str]): A list of field names whose values
                                should be redacted from the log message.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified log record, redacting sensitive fields.

        This method modifies the log record message by replacing the values
        of specified fields with the redaction string before formatting.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted and redacted log message.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Replace the values of specified fields in the message with
    the redaction string.

    Args:
        fields: List of field names to obfuscate.
        redaction: The string to replace the field values with.
        message: The original log message.
        separator: The separator between fields (e.g., ';').

    Returns:
        str: The log message with sensitive fields obfuscated.
    """
    # Iterate over each field that needs to be redacted
    for field in fields:
        # Construct a regex pattern to match 'field=value' up to the next
        # separator. The pattern uses a non-greedy match '.*?' to capture
        # the field's value until it encounters the separator character
        pattern = fr'{field}=.*?(?={separator})'
        # Replace the matched substring with 'field=redaction'
        # This substitutes the actual value with the redaction string
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data with sensitive field redaction.

    This logger is intended to output log messages while ensuring that
    personally identifiable information (PII) is obfuscated using a
    RedactingFormatter. The logger outputs to the standard stream and is
    configured to not propagate messages to parent loggers.

    Returns:
        logging.Logger: A logger instance named "user_data" with INFO level
                        and a redacting formatter applied.
    """
    # Get (or create) a logger object named 'user_data'
    logger = logging.getLogger("user_data")
    # Set the logger's threshold level to INFO (will handle INFO and above)
    logger.setLevel(logging.INFO)
    # Prevent the logger from passing messages to the root logger
    logger.propagate = False
    # Create a stream handler to output logs to standard output (console)
    handler = logging.StreamHandler()
    # Set a custom formatter on the handler that redacts sensitive PII fields
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # Attach the handler to the logger
    logger.addHandler(handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """
    Establish a connection to the MySQL database using environment variables.

    The connection parameters are retrieved from the following variables:
        - PERSONAL_DATA_DB_USERNAME: the database username (default: "root")
        - PERSONAL_DATA_DB_PASSWORD: the database password (default: "")
        - PERSONAL_DATA_DB_HOST: the database host (default: "localhost")
        - PERSONAL_DATA_DB_NAME: the name of the database (required)

    Returns:
        MySQLConnection: A connection object to the specified MySQL database.

    Raises:
        mysql.connector.Error: If the connection to the database fails.
        TypeError: If the database name is not set in the environment.
    """
    # Read environment variables.
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database.
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    """
    Main entry point for retrieving and logging user data with PII redaction.

    This function connects to a MySQL database using credentials defined in
    environment variables, retrieves all records from the "users" table,
    and logs each row after redacting personally identifiable information (PII)
    using a RedactingFormatter.

    Steps:
        1. Connect to the database using `get_db`.
        2. Retrieve all rows from the "users" table.
        3. Extract column names from the cursor description.
        4. Format each row into a key=value string.
        5. Redact sensitive fields listed in `PII_FIELDS`.
        6. Log the redacted message using the configured logger.
        7. Clean up by closing the cursor and database connection.
    """

    # Establish a connection to the MySQL database using environment variables
    db = get_db()
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()
    # Execute a SQL query to select all rows from the 'users' table
    cursor.execute("SELECT * FROM users;")
    # Retrieve the column names from the cursor description metadata
    fields: List[str] = [desc[0] for desc in cursor.description]
    # Initialize the logger configured to redact PII fields
    logger = get_logger()
    # Iterate over each row retrieved from the 'users' table
    for row in cursor:
        # Create a dictionary mapping column names to their respective values
        # for the current row
        row_dict = dict(zip(fields, row))
        # Construct a log message by joining key=value pairs separated by '; '
        log_message = "; ".join(
            [f"{key}={value}" for key, value in row_dict.items()])
        # Redact sensitive information (PII fields) in the log message
        filtered_message = filter_datum(PII_FIELDS, "***", log_message, "; ")
        # Log the redacted message at INFO level
        logger.info(filtered_message)
    # Close the cursor to release database resources
    cursor.close()
    # Close the database connection cleanly
    db.close()


if __name__ == "__main__":
    main()
