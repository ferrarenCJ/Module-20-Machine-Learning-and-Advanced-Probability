# Discussion 20.1: Use Cases of Linear Regression

## Use Case 1: Imputation of Missing Data

Linear regression can be used to estimate missing values when a strong relationship exists between variables. In the example dataset, the value of x₂ is missing for one observation. A linear regression model could be trained using the complete rows, with x₀ and x₁ serving as predictor variables and x₂ as the target variable. Once the relationship is learned, the model can predict the missing value and replace the null entry.

This approach is most effective when the variables exhibit a strong linear relationship. If the relationship is weak, a simpler imputation strategy such as the mean or median may be more appropriate.

---

## Use Case 2: Predictive Model for House Prices

Linear regression is commonly used to predict continuous numerical values such as housing prices. In the real estate example, features such as the number of rooms, number of bathrooms, square footage, pool, deck, and total quality can be used to predict a home's price.

After training the model, the predicted price can be compared against the market price to identify potentially underpriced or overpriced properties. A model like this could help real estate firms make investment decisions and identify opportunities for clients.

The features I would expect to have the greatest impact on price are square footage, total quality, number of bathrooms, and number of rooms because they directly influence the value and desirability of the property.

---

## Use Case 3: Brooklyn Housing Market

For this analysis, I used the **Brooklyn Borough** dataset from the New York City Rolling Sales Data repository.

### Handling Missing Values

The dataset contains several fields with missing values, which must be addressed before training a machine learning model.

My approach would be:

1. Remove records with missing sale prices because the sale price is the target variable being predicted.
2. Use median imputation for numerical variables such as:
   - Gross Square Feet
   - Land Square Feet
   - Year Built
3. Create an "Unknown" category for missing categorical values where appropriate.
4. Use regression-based imputation only for highly correlated fields where reliable predictions can be made.

This strategy preserves as much information as possible while minimizing the introduction of bias.

### Features Selected for the Model

The features I would use to build a housing price prediction model include:

- Neighborhood
- Building Class Category
- Residential Units
- Commercial Units
- Total Units
- Land Square Feet
- Gross Square Feet
- Year Built
- Tax Class

### Justification

I selected these features because they capture the most important drivers of real estate value:

- Location influences desirability and market demand.
- Square footage measures property size and usable space.
- Building class reflects the property's intended use and characteristics.
- Number of units impacts investment and income potential.
- Year built can indicate property condition and modernization level.
- Tax class often reflects property type and market value.

For handling missing data, I prefer a combination of removal and imputation rather than dropping all incomplete records. Removing too many records may significantly reduce training data, while thoughtful imputation retains valuable information and improves model performance.

By selecting features that are highly related to property value and carefully managing missing data, a linear regression model can provide accurate sale price predictions and help identify potentially undervalued properties in the Brooklyn housing market.

## Reference

New York City Department of Finance. *Rolling Sales Data*. Retrieved from:
https://www.nyc.gov/site/finance/property/property-rolling-sales-data.page