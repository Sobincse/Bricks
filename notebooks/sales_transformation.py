
# Databricks notebook source

print("Sales transformation started")

# Sample sales data
sales = [
    (1, "Laptop", 1200),
    (2, "Mouse", 50),
    (3, "Keyboard", 100)
]

columns = ["id", "product", "amount"]

df = spark.createDataFrame(sales, columns)

display(df)

print("Sales transformation completed")
