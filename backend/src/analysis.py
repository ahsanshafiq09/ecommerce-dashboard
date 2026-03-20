def total_revenue(df):
    return df["Revenue"].sum()

def revenue_by_category(df):
    return df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

def top_customers(df):
    return df.groupby("User_ID")["Revenue"].sum().sort_values(ascending=False).head(10)

def highest_revenue_month(df):
    df["Month"] = df["Purchase_Date"].dt.to_period("M")
    monthly = df.groupby("Month")["Revenue"].sum()
    return monthly.idxmax(), monthly.max()
