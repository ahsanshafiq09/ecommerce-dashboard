from flask import Flask, jsonify
from flask_cors import CORS

from src.load_data import load_data
from src.clean_data import clean_data
from src.analysis import total_revenue, revenue_by_category, top_customers, highest_revenue_month

app = Flask(__name__)
CORS(app)

@app.route("/data", methods=["GET"])
def get_data():
    df = load_data("data/ecommerce.csv")
    df = clean_data(df)

    month, revenue = highest_revenue_month(df)
    category_data = revenue_by_category(df)

    return jsonify({
        "totalRevenue": float(total_revenue(df)),
        "topCategory": category_data.idxmax(),
        "topCustomer": str(top_customers(df).idxmax()),
        "highestMonth": str(month),
        "categories": list(category_data.index),
        "categoryRevenue": list(category_data.values)
    })

if __name__ == "__main__":
    app.run(debug=True)
