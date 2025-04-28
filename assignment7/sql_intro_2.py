import pandas as pd
import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    sql_statement = """SELECT li.line_item_id, li.quantity, li.product_id AS line_item_product_id, p.product_id AS product_id, p.product_name, p.price
    FROM customers c 
    JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id 
    JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    # print(df.head(5))

    df['total'] = df['quantity'] * df['price']
    print(df.head(5))

    aggregated_df = df.groupby('line_item_id').agg(
        count=('line_item_id', 'count'),
        total_sum=('total', 'sum'),
        product_name=('product_name', 'first')
    ).reset_index()
    print(aggregated_df.head(5))
    
    sorted_df = aggregated_df.sort_values(by = 'product_name', ascending = False)
    print(sorted_df)
    
    sorted_df.to_csv( 'order_summary.csv', index=False)

    print(f"Data has been written")