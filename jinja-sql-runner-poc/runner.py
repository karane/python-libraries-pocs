import argparse
import psycopg2
import psycopg2.extras
from jinja2 import Environment, FileSystemLoader
import yaml
import os
from tabulate import tabulate

def load_vars(vars_file):
    if vars_file and os.path.exists(vars_file):
        with open(vars_file, "r") as f:
            return yaml.safe_load(f)
    return {}

def render_template(template_path, context):
    template_dir = os.path.dirname(template_path)
    template_name = os.path.basename(template_path)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    print("Loaded variables:", context)

    return template.render(**context)

def run_query(sql, db_config):
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)

    try:
        rows = cur.fetchall()
    except psycopg2.ProgrammingError:
        rows = []

    conn.commit()
    conn.close()
    return rows

def main():
    parser = argparse.ArgumentParser(description="Jinja SQL Runner")
    parser.add_argument("--template", required=True, help="Path to .sql.j2 file")
    parser.add_argument("--vars", help="YAML file with vars")
    args = parser.parse_args()

    # 1. Load variables
    variables = load_vars(args.vars)

    # 2. Render SQL
    sql = render_template(args.template, variables)
    print("\n-- Rendered SQL --------------------\n")
    print(sql)
    print("\n------------------------------------\n")

    # 3. Postgres config
    db_config = {
        "dbname": "testdb",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": 5432,
    }

    # 4. Execute query
    # rows = run_query(sql, db_config)

    # 5. Print result table
    # if rows:
    #     headers = rows[0].keys()
    #     table = [list(r.values()) for r in rows]
    #     print(tabulate(table, headers=headers, tablefmt="psql"))
    # else:
    #     print("(No rows returned)")

if __name__ == "__main__":
    main()
