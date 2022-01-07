import uuid
import datetime


class Person(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.age = kwargs["age"]

    @property
    def display(self):
        return f"{self.name} ({self.age})"


class Driver(Person):
    min_age_allowed = 18
    novel_years = 2
    motorbike_licence = "A"
    car_licence = "B"
    truck_licence = "C"
    no_licence = "Z"

    def __init__(self, *args, **kwargs):
        super(Driver, self).__init__(*args, **kwargs)
        self.driving_id = uuid.uuid4().hex
        self.valid_from = kwargs.get("valid_from")
        self.driving_licence = kwargs.get("driving_licence", self.no_licence)
        self.driving_id = None
        if self.driving_licence != self.no_licence:
            self.driving_id = uuid.uuid4().hex

    @classmethod
    def driver(cls, name, age, driving_licence, valid_from):
        return cls(
            name=name, age=age, driving_licence=driving_licence, valid_from=valid_from
        )

    @classmethod
    def teenager(cls, name, age):
        return cls(name=name, age=age, driving_licence=cls.no_licence)

    @property
    def can_get_driving_licence(self):
        return self.age > self.min_age_allowed

    @property
    def is_novel(self):
        if not self.valid_from:
            return False
        days = 365 * self.novel_years
        return self.valid_from > datetime.datetime.now() - datetime.timedelta(days=days)

    @property
    def show_full_licence(self):
        return f"{self.display} - {self.driving_id} (type {self.driving_licence})"


class USADriver(Driver):
    min_age_allowed = 16


class SpainDriver(Driver):
    novel_years = 1


if __name__ == "__main__":
    days = 30 * 15
    experience = datetime.datetime.now() - datetime.timedelta(days=days)
    javi_usa = USADriver.driver("Javi", 32, Driver.motorbike_licence, experience)
    print(javi_usa.show_full_licence)
    print("User can drive? %s" % javi_usa.can_get_driving_licence)
    print("User is novel? %s" % javi_usa.is_novel)

    javi_spain = SpainDriver.driver("Javi", 32, Driver.car_licence, experience)

    print(javi_spain.show_full_licence)
    print("User can drive? %s" % javi_spain.can_get_driving_licence)
    print("User is novel? %s" % javi_spain.is_novel)

    usa_teenager = USADriver.teenager("Teenager", 17)
    print(usa_teenager.show_full_licence)
    print("User can drive? %s" % usa_teenager.can_get_driving_licence)
    print("User is novel? %s" % usa_teenager.is_novel)

    spain_teenager = SpainDriver.teenager("Teenager", 17)
    print(spain_teenager.show_full_licence)
    print("User can drive? %s" % spain_teenager.can_get_driving_licence)
    print("User is novel? %s" % spain_teenager.is_novel)
