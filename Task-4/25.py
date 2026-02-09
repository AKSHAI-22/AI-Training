sales = {
    "Electronics": [1200, 2500, 1800],
    "Clothing": [800, 600, 900],
    "Groceries": [400, 300, 500, 200],
    "Books": [700, 650]
}

total_sales={}
for c, amounts in sales.items():
    total_sales[c] = sum(amounts)
print("Total sales per category:", total_sales)
top_category = max(total_sales, key=total_sales.get)
print("Category with highest revenue:", top_category)
print("Revenue:", total_sales[top_category])
