class MainWindow:
    def __init__(self):
        self.title = "Main Application Window"
        self.init_ui()

    def init_ui(self):
        print(f"{self.title} initialized after successful login.")

if __name__ == '__main__':
    main_window = MainWindow()