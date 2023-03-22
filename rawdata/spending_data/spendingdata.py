import pandas

# source for data: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip
# data readme: https://github.com/stanford-policylab/opp/blob/master/data_readme.md#statewide-ma

# pull data into pandas

checkbook_2015 = pandas.read_csv("checkbook-explorer-fy15.csv")
nrows_stanford_15, ncols_stanford_15 = checkbook_2015.shape
print("there are " + str(nrows_stanford_15) + " rows and " + str(ncols_stanford_15) + " cols in raw checkbook_2015")
# filter by boston
checkbook_2015 = checkbook_2015[checkbook_2015['dept_name'] == "Police Department"]
nrows_stanford_15, ncols_stanford_15 = checkbook_2015.shape
print("there are " + str(nrows_stanford_15) + " rows and " + str(ncols_stanford_15) + " cols in filtered checkbook_2015")

checkbook_2016 = pandas.read_csv("checkbook-explorer-fy16.csv")
nrows_stanford_16, ncols_stanford_16 = checkbook_2016.shape
print("there are " + str(nrows_stanford_16) + " rows and " + str(ncols_stanford_16) + " cols in raw checkbook_2016")
# filter by boston
checkbook_2016 = checkbook_2016[checkbook_2016['dept_name'] == "Police Department"]
nrows_stanford_16, ncols_stanford_16 = checkbook_2016.shape
print("there are " + str(nrows_stanford_16) + " rows and " + str(ncols_stanford_16) + " cols in filtered checkbook_2016")

checkbook_2017 = pandas.read_csv("checkbook-explorer-fy17.csv")
nrows_stanford_17, ncols_stanford_17 = checkbook_2017.shape
print("there are " + str(nrows_stanford_17) + " rows and " + str(ncols_stanford_17) + " cols in raw checkbook_2017")
# filter by boston
checkbook_2017 = checkbook_2017[checkbook_2017['dept_name'] == "Police Department"]
nrows_stanford_17, ncols_stanford_17 = checkbook_2017.shape
print("there are " + str(nrows_stanford_17) + " rows and " + str(ncols_stanford_17) + " cols in filtered checkbook_2017")

checkbook_2018 = pandas.read_csv("checkbook-explorer-fy18.csv")
nrows_stanford_18, ncols_stanford_18 = checkbook_2018.shape
print("there are " + str(nrows_stanford_18) + " rows and " + str(ncols_stanford_18) + " cols in raw checkbook_2018")
# filter by boston
checkbook_2018 = checkbook_2018[checkbook_2018['dept_name'] == "Police Department"]
nrows_stanford_18, ncols_stanford_18 = checkbook_2018.shape
print("there are " + str(nrows_stanford_18) + " rows and " + str(ncols_stanford_18) + " cols in filtered checkbook_2018")

checkbook_2019 = pandas.read_csv("checkbook-explorer-fy19.csv")
nrows_stanford_19, ncols_stanford_19 = checkbook_2019.shape
print("there are " + str(nrows_stanford_19) + " rows and " + str(ncols_stanford_19) + " cols in raw checkbook_2019")
# filter by boston
checkbook_2019 = checkbook_2019[checkbook_2019['dept_name'] == "Police Department"]
nrows_stanford_19, ncols_stanford_19 = checkbook_2019.shape
print("there are " + str(nrows_stanford_19) + " rows and " + str(ncols_stanford_19) + " cols in filtered checkbook_2019")

checkbook_2020 = pandas.read_csv("checkbook-explorer-fy20.csv")
nrows_stanford_20, ncols_stanford_20 = checkbook_2020.shape
print("there are " + str(nrows_stanford_20) + " rows and " + str(ncols_stanford_20) + " cols in raw checkbook_2020")
# filter by boston
checkbook_2020 = checkbook_2020[checkbook_2020['dept_name'] == "Police Department"]
nrows_stanford_20, ncols_stanford_20 = checkbook_2020.shape
print("there are " + str(nrows_stanford_20) + " rows and " + str(ncols_stanford_20) + " cols in filtered checkbook_2020")

checkbook_2021 = pandas.read_csv("checkbook_explorerfy21.csv", encoding = "ISO-8859-1")
nrows_stanford_21, ncols_stanford_21 = checkbook_2021.shape
print("there are " + str(nrows_stanford_21) + " rows and " + str(ncols_stanford_21) + " cols in raw checkbook_2021")
# filter by boston
checkbook_2021 = checkbook_2021[checkbook_2021['Dept_Name'] == "Police Department"]
nrows_stanford_21, ncols_stanford_21 = checkbook_2021.shape
print("there are " + str(nrows_stanford_21) + " rows and " + str(ncols_stanford_21) + " cols in filtered checkbook_2021")

checkbook_2022 = pandas.read_csv("checkbook_explorerfy22.csv", encoding = "ISO-8859-1")
nrows_stanford_22, ncols_stanford_22 = checkbook_2022.shape
print("there are " + str(nrows_stanford_22) + " rows and " + str(ncols_stanford_22) + " cols in raw checkbook_2022")
# filter by boston
checkbook_2022 = checkbook_2022[checkbook_2022['Dept_Name'] == "Police Department"]
nrows_stanford_22, ncols_stanford_22 = checkbook_2022.shape
print("there are " + str(nrows_stanford_22) + " rows and " + str(ncols_stanford_22) + " cols in filtered checkbook_2022")
