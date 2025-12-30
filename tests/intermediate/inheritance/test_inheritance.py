import datetime

from intermediate.inheritance import SpainDriver, UsaDriver


def _generate_date_days_ago(days: int) -> datetime.date:
    return datetime.datetime.now(
        tz=datetime.timezone.utc,
    ).date() - datetime.timedelta(days=days)


def test_usa_driver_not_novel() -> None:
    usa_driver: UsaDriver = UsaDriver(
        license_valid_from=datetime.date(2011, 4, 29),
    )
    assert usa_driver.is_novel() is False
    assert usa_driver.speed_limit() == "70mph"


def test_usa_driver_novel() -> None:
    usa_driver: UsaDriver = UsaDriver(
        license_valid_from=_generate_date_days_ago(days=30),
    )
    assert usa_driver.is_novel() is True
    assert usa_driver.speed_limit() == "70mph"


def test_spain_driver_not_novel() -> None:
    spain_driver: SpainDriver = SpainDriver(
        license_valid_from=datetime.date(2011, 4, 29),
    )
    assert spain_driver.is_novel() is False
    assert spain_driver.speed_limit() == "120km/h"


def test_spain_driver_novel():
    spain_driver: SpainDriver = SpainDriver(
        license_valid_from=_generate_date_days_ago(days=30),
    )
    assert spain_driver.is_novel() is True
    assert spain_driver.speed_limit() == "100km/h"


def test_difference_novel():
    # long time ago, with days in between 1 and 2 years ago
    license_valid_from: datetime.date = _generate_date_days_ago(days=400)
    usa_driver: UsaDriver = UsaDriver(
        license_valid_from=license_valid_from,
    )
    spain_driver: SpainDriver = SpainDriver(
        license_valid_from=license_valid_from,
    )
    # usa driver is novel, spain driver is not
    assert usa_driver.is_novel() is True
    assert spain_driver.is_novel() is False
