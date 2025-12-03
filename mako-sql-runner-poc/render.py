#!/usr/bin/env python3
import argparse
import json
from mako.template import Template


def main():
    parser = argparse.ArgumentParser(description="Render a Mako template with variables")

    parser.add_argument(
        "--template",
        required=True,
        help="Path to the Mako template file (e.g. query.sql.mako)"
    )

    parser.add_argument(
        "--vars",
        required=False,
        default="{}",
        help="JSON string with variables to pass (e.g. '{\"roles\": [\"admin\"], \"limit\": 10}')"
    )

    args = parser.parse_args()

    # Load the template
    with open(args.template) as f:
        template_content = f.read()

    template = Template(template_content)

    # Parse variables from JSON
    try:
        variables = json.loads(args.vars)
    except json.JSONDecodeError as e:
        print("Invalid JSON in --vars")
        print(e)
        return

    # Render
    output = template.render(**variables)

    print(output)


if __name__ == "__main__":
    main()
