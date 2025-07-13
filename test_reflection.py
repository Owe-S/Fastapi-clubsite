from database import Base, engine
from sqlalchemy import text

# Test reflection: list all reflected tables and raw query

def main():
    # List reflected tables
    print("Reflekterte tabeller:", list(Base.classes.keys()))

    # Use raw SQL to fetch sample rows from Activities
    query = text("SELECT TOP 5 activityID, activityName, date_start FROM Activities")
    with engine.connect() as conn:
        result = conn.execute(query).mappings().all()
        print("\nEksempler fra Activities:")
        for row in result:
            print(f"ID={row['activityID']}, Name={row['activityName']}, Start={row['date_start']}")

if __name__ == '__main__':
    main()
