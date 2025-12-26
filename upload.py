import psycopg2

conn = psycopg2.connect(
    host="scraper-server-grad-project.postgres.database.azure.com",
    database="scraped_data",
    user="omar2776",
    password="REMOVED_SECRET!",
    port=5432,
    sslmode="require"
)

cur = conn.cursor()

cur.execute(
    """
    INSERT INTO public.test (name)
    VALUES (%s);
    """,
    ("Omar",)
)

conn.commit()

cur.execute(
    """
    SELECT * FROM public.test;
    """,
)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
