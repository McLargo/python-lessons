import logging

from intermediate.logging import CustomFilter


def test_filter_logging(caplog):
    # add CustomFilter to logger
    logger = logging.getLogger("intermediate.logging.custom_logging")
    logger.addFilter(CustomFilter())

    # log with sensitive information in extra gets masked
    data_user = {
        "username": "user1",
        "email": "user@example.com",
        "password": "secret_password",
        "tries": 3,
    }
    logger.info("User logger.", extra=data_user)

    assert len(caplog.records) == 1
    assert caplog.records[0].message == "User logger."
    assert caplog.records[0].username == "user1"
    assert caplog.records[0].email == "****@example.com"
    assert caplog.records[0].password == "***************"
    assert caplog.records[0].tries == 3

    # log with sensitive information as args does not get masked
    logger.info(
        "Email %s and password %s",
        "user@example.com",
        "Supersecret_password",
    )
    assert len(caplog.records) == 2
    expected_msg = "Email user@example.com and password Supersecret_password"
    assert caplog.records[1].getMessage() == expected_msg
