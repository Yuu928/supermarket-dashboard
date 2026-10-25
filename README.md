# Supermarket Sales Dashboard

## 1. Who it is for and what decision it supports
This dashboard is for a regional sales manager at a supermarket chain. It supports the decision of which product line and which city to focus promotions on next month.

## 2. What I show and why
- Three headline numbers (total sales, number of orders, average rating) so the manager sees the overall picture in one glance.
- A bar chart of sales by product line, because the manager needs to see which lines bring in the most revenue.
- A bar chart of sales by city, because the manager needs to compare branches.
- A city and product-line filter so the manager can zoom into one region.

## 3. What I cut and why
- I removed the raw table by default because a manager should not scroll through 1,000 rows.
- I did not add a time-series chart because the dataset covers only three months and the trend is not the main question.

## 4. How often the data should be refreshed
The data should be refreshed weekly. Sales decisions are made weekly, and a daily refresh would add noise without changing the decision.
