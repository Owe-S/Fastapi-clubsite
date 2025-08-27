import os
import csv
from textwrap import indent

# 1) List all tables you've already defined manually so they’re skipped:
DONE = {
    "Activities",
    "Activities_DateTime",
    "Activities_List",
    "SiteUser",
    "Siteusers",            # ← add this exact table name
    "Images",
    "Images_Categories",
    "News_Articles",
    "Courses",
    "Courses_Hio",
    "Course_Guide_Hole",
    "Course_Guide_Images",
    "Course_Guide_Sponsors",
    "Admin_Areas",
    "Admin_User_PwdTemp",
}

# 2) Map SQL types → SQLAlchemy types (expand as needed)
TYPE_MAP = {
    "int": "Integer",
    "varchar": "String",
    "bit": "Boolean",
    "tinyint": "SmallInteger",
    "smalldatetime": "DateTime",
    "datetime": "DateTime",
    "date": "Date",
    "decimal": "DECIMAL",
    "float": "Float",
    "-1": "Text",
    # … add more from your schema …
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TSV_PATH = os.path.join(BASE_DIR, "_Old", "dbo_alle_pr_Klient_database_full.txt")
MODELS_PATH = os.path.join(BASE_DIR, "models.py")
SCHEMAS_PATH = os.path.join(BASE_DIR, "schemas.py")

START_MD = "# -- AUTO GENERATED MODELS START"
END_MD = "# -- AUTO GENERATED MODELS END"
START_SC = "# -- AUTO GENERATED SCHEMAS START"
END_SC = "# -- AUTO GENERATED SCHEMAS END"

def load_tsv():
    tables = {}
    with open(TSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            tbl = row["TABLE_NAME"]
            if tbl in DONE:
                continue
            tables.setdefault(tbl, []).append(row)
    return tables

def gen_stubs(tables):
    models = []
    schemas = []

    for tbl, cols in tables.items():
        # Build class name
        name = "".join(w.title() for w in tbl.lower().split("_"))

        # --- MODEL stub ---
        models.append(f"class {name}(Base):")
        models.append(f"    __tablename__ = \"{tbl}\"")
        for c in cols:
            col       = c["COLUMN_NAME"]
            sqlt      = TYPE_MAP.get(c["DATA_TYPE"], "String")
            maxl      = c["CHARACTER_MAXIMUM_LENGTH"]
            # only parameterize String with numeric length
            arg       = f"{sqlt}({maxl})" if sqlt == "String" and maxl and maxl.isdigit() else sqlt
            nullable  = ", nullable=True" if c["IS_NULLABLE"] == "YES" else ""
            # mark first column (ordinal 1) as primary key
            is_pk     = ", primary_key=True" if int(c["ORDINAL_POSITION"]) == 1 else ""
            models.append(f"    {col} = Column({arg}{is_pk}{nullable})")
        models.append("")  # blank line

        # --- SCHEMA stub ---
        schemas.append(f"class {name}Base(BaseModel):")
        for c in cols:
            col_name = c["COLUMN_NAME"]
            typ = "Optional[str]" if TYPE_MAP.get(c["DATA_TYPE"], "String") in ("String", "Text") else "Optional[int]"
            schemas.append(f"    {col_name}: {typ} = None")
        schemas.append(f"class {name}In({name}Base):")
        schemas.append("    pass")
        schemas.append(f"class {name}Out({name}Base):")
        pk = cols[0]["COLUMN_NAME"]
        schemas.append(f"    {pk}: int")
        schemas.append("")  # blank line

    return models, schemas

def splice_file(path, start_marker, end_marker, new_lines):
    with open(path, encoding="utf-8") as f:
        out = []
        skipping=False
        for l in f:
            if l.strip() == start_marker:
                out.append(l)
                out.extend(line+"\n" for line in new_lines)
                skipping=True
                continue
            if l.strip() == end_marker:
                out.append(l)
                skipping=False
                continue
            if not skipping:
                out.append(l)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)

if __name__=="__main__":
    tbls = load_tsv()
    md, sc = gen_stubs(tbls)
    splice_file(MODELS_PATH, START_MD, END_MD, md)
    splice_file(SCHEMAS_PATH, START_SC, END_SC, sc)
    print("✅ Injected", len(md), "model lines and", len(sc), "schema lines.")