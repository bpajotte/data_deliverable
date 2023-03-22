import pandas

# source for data: https://stacks.checkbok.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip
# data readme: https://github.com/checkbok-policylab/opp/blob/master/data_readme.md#statewide-ma

# pull data into pandas

checkbook_2015 = pandas.read_csv("checkbook-explorer-fy15.csv")
nrows_checkbok_15, ncols_checkbok_15 = checkbook_2015.shape
print("there are " + str(nrows_checkbok_15) + " rows and " + str(ncols_checkbok_15) + " cols in raw checkbook_2015")
# filter by police department
checkbook_2015 = checkbook_2015[checkbook_2015['dept_name'] == "Police Department"]
nrows_checkbok_15, ncols_checkbok_15 = checkbook_2015.shape
print("there are " + str(nrows_checkbok_15) + " rows and " + str(ncols_checkbok_15) + " cols in filtered checkbook_2015")

checkbook_2016 = pandas.read_csv("checkbook-explorer-fy16.csv")
nrows_checkbok_16, ncols_checkbok_16 = checkbook_2016.shape
print("there are " + str(nrows_checkbok_16) + " rows and " + str(ncols_checkbok_16) + " cols in raw checkbook_2016")
# filter by police department
checkbook_2016 = checkbook_2016[checkbook_2016['dept_name'] == "Police Department"]
nrows_checkbok_16, ncols_checkbok_16 = checkbook_2016.shape
print("there are " + str(nrows_checkbok_16) + " rows and " + str(ncols_checkbok_16) + " cols in filtered checkbook_2016")

checkbook_2017 = pandas.read_csv("checkbook-explorer-fy17.csv")
nrows_checkbok_17, ncols_checkbok_17 = checkbook_2017.shape
print("there are " + str(nrows_checkbok_17) + " rows and " + str(ncols_checkbok_17) + " cols in raw checkbook_2017")
# filter by police department
checkbook_2017 = checkbook_2017[checkbook_2017['dept_name'] == "Police Department"]
nrows_checkbok_17, ncols_checkbok_17 = checkbook_2017.shape
print("there are " + str(nrows_checkbok_17) + " rows and " + str(ncols_checkbok_17) + " cols in filtered checkbook_2017")

checkbook_2018 = pandas.read_csv("checkbook-explorer-fy18.csv")
nrows_checkbok_18, ncols_checkbok_18 = checkbook_2018.shape
print("there are " + str(nrows_checkbok_18) + " rows and " + str(ncols_checkbok_18) + " cols in raw checkbook_2018")
# filter by police department
checkbook_2018 = checkbook_2018[checkbook_2018['dept_name'] == "Police Department"]
nrows_checkbok_18, ncols_checkbok_18 = checkbook_2018.shape
print("there are " + str(nrows_checkbok_18) + " rows and " + str(ncols_checkbok_18) + " cols in filtered checkbook_2018")

checkbook_2019 = pandas.read_csv("checkbook-explorer-fy19.csv")
nrows_checkbok_19, ncols_checkbok_19 = checkbook_2019.shape
print("there are " + str(nrows_checkbok_19) + " rows and " + str(ncols_checkbok_19) + " cols in raw checkbook_2019")
# filter by police department
checkbook_2019 = checkbook_2019[checkbook_2019['dept_name'] == "Police Department"]
nrows_checkbok_19, ncols_checkbok_19 = checkbook_2019.shape
print("there are " + str(nrows_checkbok_19) + " rows and " + str(ncols_checkbok_19) + " cols in filtered checkbook_2019")

checkbook_2020 = pandas.read_csv("checkbook-explorer-fy20.csv")
nrows_checkbok_20, ncols_checkbok_20 = checkbook_2020.shape
print("there are " + str(nrows_checkbok_20) + " rows and " + str(ncols_checkbok_20) + " cols in raw checkbook_2020")
# filter by police department
checkbook_2020 = checkbook_2020[checkbook_2020['dept_name'] == "Police Department"]
nrows_checkbok_20, ncols_checkbok_20 = checkbook_2020.shape
print("there are " + str(nrows_checkbok_20) + " rows and " + str(ncols_checkbok_20) + " cols in filtered checkbook_2020")

checkbook_2021 = pandas.read_csv("checkbook_explorerfy21.csv", encoding = "ISO-8859-1")
nrows_checkbok_21, ncols_checkbok_21 = checkbook_2021.shape
print("there are " + str(nrows_checkbok_21) + " rows and " + str(ncols_checkbok_21) + " cols in raw checkbook_2021")
# filter by police department
checkbook_2021 = checkbook_2021[checkbook_2021['Dept_Name'] == "Police Department"]
nrows_checkbok_21, ncols_checkbok_21 = checkbook_2021.shape
print("there are " + str(nrows_checkbok_21) + " rows and " + str(ncols_checkbok_21) + " cols in filtered checkbook_2021")

checkbook_2022 = pandas.read_csv("checkbook_explorerfy22.csv", encoding = "ISO-8859-1")
nrows_checkbok_22, ncols_checkbok_22 = checkbook_2022.shape
print("there are " + str(nrows_checkbok_22) + " rows and " + str(ncols_checkbok_22) + " cols in raw checkbook_2022")

# filter by police department
checkbook_2022 = checkbook_2022[checkbook_2022['Dept_Name'] == "Police Department"]
nrows_checkbok_22, ncols_checkbok_22 = checkbook_2022.shape
print("there are " + str(nrows_checkbok_22) + " rows and " + str(ncols_checkbok_22) + " cols in filtered checkbook_2022")


