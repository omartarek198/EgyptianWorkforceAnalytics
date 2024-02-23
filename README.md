"# EgyptianWorkforceAnalytics" 


Issue in the dataset:  
1- Cannot load it with the Arabic timestamp , fix: dropping the timestamp column 
2- Headers have extra spaces, for example : "Years of Experiences ", fix : trimming 
3- Years of Experience have a lot of issues because it was a recorded in plain text.
Fixes:
 -Convert to Months of Experience and multiplied numeric values by 12
 -Converted Non-Numeric columns to numeric by a series of steps: 
   * Removed "Years", "Year" etc
   * Removed Symbols such as > < ~ etc
     so far the %of NAN in MonthsOfExperience was equal to 12.4%
   * 
