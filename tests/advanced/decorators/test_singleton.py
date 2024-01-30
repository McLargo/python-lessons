from src.advanced.decorators import singleton


# Set decorated class to test
@singleton
class Demo:
    def __init__(self, a: int = 0):
        self.a = a


def test_singleton() -> None:
    demo1 = Demo()
    assert demo1.a == 0

    demo2 = Demo(10)
    assert demo1.a == 10
    assert demo2.a == 10
    assert demo1 is demo2

    demo3 = Demo(a=100)
    assert demo1.a == 100
    assert demo2.a == 100
    assert demo3.a == 100

    assert demo1 is demo2 is demo3

    demo4 = Demo()
    assert demo1.a == 0
    assert demo2.a == 0
    assert demo3.a == 0
    assert demo4.a == 0

    assert demo1 is demo2 is demo3 is demo4
