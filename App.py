import os.path
import sys

from Controller import Controller


class App:
    def __init__(self, db):
        Controller(db).main()


if __name__ == "__main__":
    db_name = None
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            db_name = sys.argv[1]
    App(db_name)
