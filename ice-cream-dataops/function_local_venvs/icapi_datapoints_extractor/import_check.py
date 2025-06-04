import sys
from pathlib import Path

# This is necessary to import adjacent modules in the function code.
sys.path.insert(0, str(Path(__file__).parent / "local_code"))

from local_code.handler import handle # noqa: E402


def main() -> None:
    print("Imported function successfully: " + handle.__name__)


if __name__ == "__main__":
    main()

