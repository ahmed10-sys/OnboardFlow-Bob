"""
OnboardFlow — static HTML generator.
Reads a repo_blueprint.json file and renders it into a self-contained
architecture tour page using template.html.

Usage:
    python visualizer.py [--blueprint path/to/blueprint.json]
                         [--template path/to/template.html]
                         [--output  path/to/output.html]
"""

import argparse
import json
import sys
from pathlib import Path


def load_blueprint(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render(blueprint: dict, template: str) -> str:
    # Placeholder — rendering logic goes here.
    return template


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an OnboardFlow architecture tour page.")
    parser.add_argument(
        "--blueprint",
        type=Path,
        default=Path("fixtures/callbridge.json"),
        help="Path to the repo_blueprint.json file (default: fixtures/callbridge.json)",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("template.html"),
        help="Path to the HTML template file (default: template.html)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/architecture_tour.html"),
        help="Destination path for the generated HTML (default: output/architecture_tour.html)",
    )
    args = parser.parse_args()

    if not args.blueprint.exists():
        print(f"ERROR: blueprint not found: {args.blueprint}", file=sys.stderr)
        sys.exit(1)
    if not args.template.exists():
        print(f"ERROR: template not found: {args.template}", file=sys.stderr)
        sys.exit(1)

    blueprint = load_blueprint(args.blueprint)
    template = load_template(args.template)
    html = render(blueprint, template)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Generated: {args.output}")


if __name__ == "__main__":
    main()
