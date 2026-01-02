from advanced.decorators import singleton


def test_singleton() -> None:
    @singleton
    class Demo:
        instance_count = 0

        def __init__(self, a: int = 0):
            self.a = a
            Demo.instance_count += 1

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

    assert Demo.instance_count == 4


def test_singleton_hasattr_check() -> None:
    @singleton
    class TestClass:
        pass

    instance1 = TestClass()

    assert hasattr(TestClass, "_TestClass__singleton") or hasattr(
        TestClass,
        "__singleton",
    )

    instance2 = TestClass()

    assert instance1 is instance2
