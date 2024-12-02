import subprocess
from pathlib import Path


def main() -> None:
    print("starting app in development mode")
    curr_dir = Path(__file__).resolve().parent.absolute()
    script = curr_dir / "run.sh"
    try:
        subprocess.run(["sh", script], check=True)
    except KeyboardInterrupt:
        return
