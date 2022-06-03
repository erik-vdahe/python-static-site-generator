from pathlib import Path

class Site:
    """Site class."""

    def __init__(self, source: str, dest: str):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        """Create a directory in the named path."""
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents = True, exist_ok = True)

    def build(self):
        self.dest.mkdir(parents = True, exist_ok = True)
        for path in self.source.rglob('*'):
            if path.is_dir():
                self.create_dir(path)