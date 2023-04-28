# Manhattan Residential Property Sales
Note: All property sales in Manhattan from April 2022 - March 2023. 
Source: NYC Open Data. 

## Files:
- Raw data from NYC Open Data: rollingsales_manhattan.csv
- Cleaned data: manhattan_sales_cleaned_2023.csv
- EDA notebook: manhattan_sales_EDA.ipynb
- Data downloaded from NYC Open Data: https://www.nyc.gov/site/finance/taxes/property-rolling-sales-data.page
- Glossary from NYC Open Data: https://www.nyc.gov/assets/finance/downloads/pdf/07pdf/glossary_rsf071607.pdf
- NYC Building Class Definitions: https://www.nyc.gov/assets/finance/jump/hlpbldgcode.html

## Objectives
- Do exploratory data analysis on property data from NYC Open Data
- Create visualizations on data examining factors that influence sale price
- Build a web app using Streamlit and Render

## Data Source
`neighborhood` Neighborhood of NYC the property is located in \
`building_class_category` Description of the building class at present \
`building_class_at_present` Current building class per NYC government \
`address` Street address of the property \
`apartment_number` Apartment number of the property, if any \
`zip_code` Zip code of the property \
`residential_units` Number of residential units, if larger than a unit \
`commercial_units` Number of commercial units, if any \
`total_units` Total number of units \
`land_square_feet` Size of land in square feet \ 
`gross_square_feet` Size of building in square feet \
`year_built` Year built in YYYY format \
`building_class_at_time_of_sale` Building class at time of sale per NYC government \
`sale_price` Sale price in $US dollars \
`sale_date` Date of sale \
`unit_price` Sale price / total units \
`sqft_price` Sale price / gross square footage \

## Summary
I cleaned the data from NYC Open Data, removing unecessary rows and columns including: 
- all non-residential records (we only want to analyze residential properties)
- all sales below $10,000 (assumed to be gifts)
- columns unecessary for analysis of factors influencing sale price and extra/miscellaneous columns 
- created columns for unit price, square foot price
- renamed columns, changed data types of columns where necessary
After implementing these changes, I saved a clean version to use for streamlit. 

For EDA, I took a look at 
- the distribution of sale price in each residential category (shown as histograms)
- average prices in each neighborhood in both unit and square foot terms
- the relationship between building size (gross sqft) and total sale price
- the relationship between building age and sale price
- ranges of pricing for buildings in each neighborhood
- trends of sale prices over the year

Sale prices over the year did not show any particularly interesting trends. Neither did the building vintage and sale price. There was a positive relationship between building size and sale price as shown in a scatterplot. 

## Next Steps
This project is mainly focused on the mechanics of creating a web application and only includes initial EDA. Further analysis on factors influencing sale price may delver further into:
- Location, using neighborhood or zip code as a proxy 
- Deeper analysis within building types (i.e. walk-ups) to compare pricing differentials on an apples-apples basis 
- Extend the dataset further back in time to create time series analysis on property prices over the last market cycle
- Analyze how neighborhoods changed over time, looking at pricing and building classifications    