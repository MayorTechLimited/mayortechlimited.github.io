import sys
import json
import shutil
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Mover(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toc = set()
        toc = Path(".static")
        try:
            with toc.open("r") as fp:
                self.toc = set(Path(p) for p in json.load(fp))
        except:
            pass

    def dump(self):
        toc = Path(".static")
        with toc.open("w") as fp:
            json.dump(list(str(p) for p in self.toc), fp)

    def on_modified(self, event):
        src = Path(event.src_path)
        if src.is_file():
            self.copy_file(Path(event.src_path))
        self.sync()
        self.dump()

    def copy_file(self, src_path):
        path = self.dist_path(src_path)
        print(f"Copy {src_path} into {path}")
        path.parent.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(src_path, path)
        self.toc.add(src_path.relative_to("static"))

    def remove_file(self, dist_path):
        print(f"Remove {dist_path}")
        dist_path.unlink()
        self.toc.remove(dist_path.relative_to("dist"))

    def sync(self):
        src = set(self.find_files(Path(".") / "static"))
        dist = set(self.find_files(Path(".") / "dist"))

        for new_src in src - dist:
            self.copy_file(Path(".") / "static" / new_src)

        for old_dist in self.toc - src:
            self.remove_file(Path(".") / "dist" / old_dist)

    def find_files(self, dir):
        for dirpath, dirnames, filenames in dir.walk():
            for fn in filenames:
                p = Path(dirpath) / fn
                yield p.relative_to(dir)

    def dist_path(self, src_path):
        static = Path(".") / "static"
        inner_path = Path(src_path).relative_to(static)
        return Path(".") / "dist" / inner_path


if __name__ == "__main__":
    handler = Mover()
    if "--watch" in sys.argv:
        observer = Observer()
        observer.schedule(handler, path="static", recursive=True)
        print("Starting...")
        observer.start()
        try:
            while observer.is_alive():
                observer.join(1)
        finally:
            observer.stop()
            observer.join()
        print("FIN")
    else:
        # TODO: Minify/process the files? Add hash to the filename?
        handler.sync()
