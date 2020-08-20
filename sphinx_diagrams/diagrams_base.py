import re
from typing import List

from diagrams import Diagram


class DiagramsBase:
    title = None

    def __init__(self, argv: List[str]):
        default_filename = self.__class__.__name__
        default_filename = re.sub(r"(?<!^)(?=[A-Z])", "-", default_filename).lower()

        self.filename = argv[1] if len(argv) >= 2 else f"{default_filename}"
        self.show = argv[2].lower() in {"True", "true"} if len(argv) >= 3 else True
        self.extra_args = argv[3] if len(argv) >= 4 else ""

    def render(self):
        title = (
            self.filename.replace("_", " ").replace("-", " ").title()
            if not self.title
            else self.title
        )
        with Diagram(title, show=self.show, filename=self.filename):
            self.define()

    def define(self):
        raise NotImplemented
