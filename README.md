# price-prediction
### Approach
	1.	Data Loading & Merging:
	    •	Both CSVs are loaded using pandas.
	    •	They are merged on sku to combine product and sales info.
	2.	Rule-Based Pricing Engine:
	    •	Each product is processed row-wise using .apply() and a function that evaluates pricing rules in order of precedence.
	3.	Rules Applied:
	    •	Rule 1: If stock < 20 and quantity_sold > 30, increase price by 15%.
	    •	Rule 2: If stock > 200 and quantity_sold == 0, decrease price by 30%.
	    •	Rule 3: If stock > 100 and quantity_sold < 20, decrease price by 10%.
	    •	Rule 4: Ensure the final price is at least 20% above the cost price.
	    •	If not, reset it to cost_price * 1.2.
	    •	Round final price to 2 decimal places.
	4.	Formatting & Export:
	    •	Both old and new prices are formatted with "INR" units.
	    •	Output is saved to updated_prices.csv.
