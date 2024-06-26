class Example:
    def __init__(self):
        pass

    def on_click(self, x, y):
        print(f"Clicked at ({x}, {y})")

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

example = Example()
example.callback("on_", "click", 10, 20)  # 输出: Clicked at (10, 20)