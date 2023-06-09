# Data Deliverable

## DATA SPEC
We effectively have two data sets :
1. Government spending by the City of Boston, from the CSV files named 'checkbook_explorer_fyXX'.
2. Crime reports from the City of Boston, from the CSV files named 'crime incident reports - 20XX'.


The first data set, government spending has the following categories:
`voucher`, `voucher_line`, `distribution_line`,`entered`, `month_number`, `fiscal_month`, `month`, `fiscal_year`, `year`, `vendor_name`, `account`, `account_descr`, `dept`, `dept_name`, `c6_digit_org_name`, and `monetary_amount`. 

However, not all of these are relevant. The important categories are:
- `voucher`: an integer that is effectively the key for the transaction. This is in conjunction with the voucher_line field -- some vouchers will have multiple transactions under the same voucher number, but those different transactions will have different voucher_line values. There is not a default value for the voucher number. Similarly, the range is not relevant here - the values in the voucher column tend to be from 2 million to three million, but some are lower or higher than that range, and the value itself is not useful here - they just serve to identify separate transactions. The distribution is thus mostly flat, since there are at most a few transactions on any given voucher. The values are not unique, but in conjunction with the voucher_line field, they are. Should two transactions have the same voucher and voucher_line, they are duplicates. This value is required. We will likely not use this value in analysis, as the specific numbers do not mean anything - the values in the voucher column are effectively IDs for different transactions. This feature does not include any sensitive information.
- `vendor_name`: a string representing who was paid in a given transaction. The default value would be an empty string, but it appears there are no records without a value for vendor_name, which makes sense as every payment should have a recipient. There is no range here. Similarly, we do not have a 'distribution' of values. These values are not unique - there are often multiple payments to the same business or organization. This value will not be used to detect duplicate records. This value is technically not strictly required, but as mentioned earlier, every record has a value as you cannot process a payment without a recipient. We may use this value in the analysis - it might be interesting or relevant to see where money is being spent. The information is mostly the names of businesses or payment processes, and are thus not sensitive. 
- `dept_name`: a string representing which department of government made the payment. The default value would again be an empty string, but similarly every record has a value as someone must be making the payment. There is not a range either - these are strings. Similarly, the distribution is not relevant here, as this is an attribute we are filtering on, so every record in the final data set will have the same value. The values are not unique. We are not using this value to detect duplicate records. This value is not strictly required, but as mentioned earlier, every record has a value. We are not using this value in our analysis, but instead in our cleaning - we have filtered on dept_name to get only transactions made by the police. These department names are not sensitive.
- `monetary_amount`: a float representing the amount paid (to two decimal places) in a given transaction. There is no default value here, as they are monetary amounts. The minimum value here is 0.0 (a bit surprising, as it is unclear how someone could make a free payment) and the maximum value in any year was 2,307,636. The payments do not appear to be distributed according to any particular pattern, although most of them are for comparatively lower values (there are not a lot of multimillion dollar transactions.) These values are not unique, and will not be used to determine duplicates - it is likely there are multiple transactions for the same price. This value is required. This attribute will be used in the analysis heavily - we want to see how much money the police are spending and what they are spending the most on.


The second data set, crime incident reports, has the following fields:
`INCIDENT_NUMBER`, `OFFENSE_CODE`, `OFFENSE_CODE_GROUP`, `OFFENSE_DESCRIPTION`, `DISTRICT`, `REPORTING_AREA`, `SHOOTING`, `OCCURRED_ON_DATE`, `YEAR`, `MONTH`, `DAY_OF_WEEK`, `HOUR`, `UCR_PART`, `STREET`, `Lat`, `Long`, `Location`

The most important categories here are:
- `INCIDENT_NUMBER`: A unique string consisting of I followed by a series of numbers. There is not a default value here, nor is the range particularly relevant -- each incident should have its own incident number. Again, these have a flat distribution, as each incident number should correspond to only one incident. Thus, these values should be unique. If they are not, we will use them to detect duplicates. This is a required value - each incident must have an incident number. We will not really use this value in the analysis, similar to the voucher field discussed earlier - this field is just an ID. This field also does not contain sensitive information. 

The following three attributes of our crime incident reports are very similar, so discussion of how they will be used in the analysis is saved until the end.

- `OFFENSE_CODE`: An integer representing the offense a given crime is considered, as specified in rmsoffensecodes.xlsx. There is not a default value here - each offense code means something. The range here is again not really relevant, as the offense code integer numbers are just references to a type of offense. The distribution of them is similarly not relevant, as we will be filtering later to get just offenses classified as drug related crime. The values are not unique, and we will not use them to detect duplicates - there will be many crimes with the same offense code. This value is required. It also does not contain any sensitive information.
- `OFFENSE_CODE_GROUP`: A string representing the general category of crime a given crime falls into - for example, armed robbery using different types of weapons are different crimes, but in the same group. There is no default value here, and similarly no range as they are strings. The distribution is again not relevant, as we are going to filter to get just crimes in the various groups related to drugs. These values are not unique, nor will they be used to detect duplicates. This value is required. These codes do not contain sensitive information either.
- `OFFENSE_CODE_DESCRIPTION`: A string representing the specific offense committed. These strings are equivalent to the number in OFFENSE_CODE - the value of OFFENSE_CODE_DESCRIPTION for a given record is the offense associated with its OFFENSE_CODE value, translated through rmsoffensecodes.xlsx. There is again no default value, range, or distribution. These values are similarly not unique, and will not be used in regards to duplicates. This value is required. These strings do not contain sensitive information. 

At least one, if not multiple of OFFENSE_CODE, OFFENSE_CODE_GROUP, or OFFENSE_CODE_DESCRIPTION will be used in our analysis. Once we begin our analysis, we will need to isolate just crimes related to drugs. However, it is not immediately clear which of these three will be the best attribute to filter on. Thus, we are keeping all three for now, to keep our options open.

## TECH REPORT
1. How many data points are there in total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? 
    - Aim for a resource of reasonable size. At least 500 records after cleaning and duplicate removal. Account that part of your data should be used for validation of your results only. 
    - Do you think this is enough data to perform your analysis later on?
2. What are the identifying attributes?
3. Where is the data from?
    - How did you collect your data?
      We collected the spending data and crime incident report data directly from https://data.boston.gov/, the official website that houses the City of Boston's open data hub. The state patrol data came from The Stanford Open Policing Project (https://openpolicing.stanford.edu/). 
    - Is the source reputable?
      Both sources are reputable, the data from the Stanford Open Policing Project was collected from public traffic stop data and is heavily documented on the methods used in cleaning and organizing the data. The rest of the data was collected from a government website.
    - How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?
    - Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)
4. How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)
    - How did you check for the cleanliness of your data? What was your threshold reference?
    - Did you implement any mechanism to clean your data? If so, what did you do?
    - Are there missing values? Do these occur in fields that are important for your project's goals?
    - Are there duplicates? Do these occur in fields that are important for your project's goals?
    - How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)
    - Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?
    - Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?
