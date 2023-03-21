import pandas

# source for data: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip
# data readme: https://github.com/stanford-policylab/opp/blob/master/data_readme.md#statewide-ma

# pull data into pandas
checkbook_2015 = pandas.read_csv("checkbook-explorer-fy15.csv")
nrows_stanford, ncols_stanford = checkbook_2015.shape
print("there are " + str(nrows_stanford) + " rows and " + str(ncols_stanford) + " cols in raw checkbook_2015")
# filter by boston
checkbook_2015 = checkbook_2015[checkbook_2015['dept_name'] == "Police Department"]
nrows_stanford, ncols_stanford = checkbook_2015.shape
print("there are " + str(nrows_stanford) + " rows and " + str(ncols_stanford) + " cols in filtered checkbook_2015")

