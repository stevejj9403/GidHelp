import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open("amazon.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Initialize empty lists to store the extracted data
product_names = []
product_prices = []
product_reviews = []

# Find all div elements with the specified class
product_divs = soup.find_all("div", class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1k579acibq3g12dxe3xrr3x1qq s-latency-cf-section puis-card-border")

# Loop through the div elements and extract the desired information
for div in product_divs:
    # Extract Product Name
    product_name = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    if product_name:
        product_names.append(product_name.text.strip())
    else:
        product_names.append("")

    # Extract Product Price
    product_price = div.find("span", class_="a-price-whole")
    if product_price:
        product_prices.append(product_price.text.strip())
    else:
        product_prices.append("")

    # Extract Product Reviews
    product_reviews_span = div.find("span", class_="a-size-base")
    if product_reviews_span:
        product_reviews.append(product_reviews_span.text.strip())
    else:
        product_reviews.append("")

# Create a DataFrame to store the extracted data
data = {
    "Product_Name": product_names,
    "Product_Price": product_prices,
    "Product_Reviews": product_reviews
}
df = pd.DataFrame(data)

# Write the data to an Excel file
df.to_excel("amazon_products.xlsx", index=False, engine="openpyxl")
