"""
 Program Purpose: To calculate & determine the total units sold, highest sales, customer reviews of Ceria Florist.
 Programmer: MUHAMMAD SYUKRI BIN MHD YUSOF (AM2307013981)
 Date: 8 March 2024
"""

# Define sample data for 20 flowers
product_names = ["Begonia", "Sunflower", "Daisy", "Lily", "Tulips",
                 "Orchid", "Zinnia", "Lilac", "Anemone", "Daffodil",
                 "Gerbera", "Chrysanthemum", "Transvaal daisy", "Pansy", "Poppy",
                 "Snapdragon", "Rose", "Amaryllis", "Marigold", "Iris"]

units_sold = [100, 200, 150, 160, 250,
              180, 220, 110, 80,190,
              75, 210, 90, 75, 240,
              175, 270, 105, 85, 230]

customer_reviews = [2.2, 3.8, 4.5, 4.0, 3.5,
                    4.2, 3.9, 4.0, 4.3, 2.8,
                    2.5, 3.6, 4.3, 3.3, 4.4,
                    2.9, 4.6, 3.7, 4.7, 3.1]

# Task 1: Total Units Sold Calculation
total_units_sold = sum(units_sold)

# Task 2: Highest Sales Identification
max_units_sold = max(units_sold)
flower_with_highest_sales = product_names[units_sold.index(max_units_sold)]

# Task 3: Above-Average Customer Reviews Identification
above_average_reviews = [product_names[i] for i in range(len(product_names)) if customer_reviews[i] > 3]

# Task 4: Average Customer Review Score Calculation
average_review_score = sum(customer_reviews) / len(customer_reviews)

# Task 5: Below-Average Sales Identification
average_units_sold = sum(units_sold) / len(units_sold)
below_average_sales = [{'product_name': product_names[i], 'units_sold': units_sold[i], 'customer_review': customer_reviews[i]}
                        for i in range(len(product_names)) if units_sold[i] < average_units_sold]

print("Welcome to Ceria Florist sales & reviews analysist.")
print() #blank line
print("Total units sold:", total_units_sold)
print() #blank line
print("Flower with the highest sales:", flower_with_highest_sales)
print() #blank line
print("Flowers with above-average customer reviews:", above_average_reviews)
print() #blank line
print("Average customer review score:", average_review_score)
print() #blank line
print("Flowers with below-average sales as per below:")
for flower in below_average_sales:
    print("Product Name:", flower['product_name'])
    print("Units Sold:", flower['units_sold'])
    print("Customer Review:", flower['customer_review'])
    print()
