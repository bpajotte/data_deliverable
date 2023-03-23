import pandas

# source for data: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip
# data readme: https://github.com/stanford-policylab/opp/blob/master/data_readme.md#statewide-ma

# pull data into pandas 
csv_stanford = pandas.read_csv("data/crime_data/openpolicingstanfordedu/ma-state-patrol.csv")
nrows_stanford, ncols_stanford = csv_stanford.shape
print("there are " + str(nrows_stanford) + " rows and " + str(ncols_stanford) + " cols in raw csv_stanford")
# filter by boston
csv_stanford = csv_stanford[csv_stanford['location'] == "BOSTON"]
nrows_stanford, ncols_stanford = csv_stanford.shape
print("there are " + str(nrows_stanford) + " rows and " + str(ncols_stanford) + " cols in filtered csv_stanford")


crime_reports_2015 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2015.csv")
nrows_cr_15, ncols_cr_15 = crime_reports_2015.shape
print("there are " + str(nrows_cr_15) + " rows and " + str(ncols_cr_15) + " cols in crime_reports_2015")

crime_reports_2016 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2016.csv")
nrows_cr_16, ncols_cr_16 = crime_reports_2016.shape
print("there are " + str(nrows_cr_16) + " rows and " + str(ncols_cr_16) + " cols in crime_reports_2016")

crime_reports_2017 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2017.csv")
nrows_cr_17, ncols_cr_17 = crime_reports_2017.shape
print("there are " + str(nrows_cr_17) + " rows and " + str(ncols_cr_17) + " cols in crime_reports_2017")

crime_reports_2018 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2018.csv")
nrows_cr_18, ncols_cr_18 = crime_reports_2018.shape
print("there are " + str(nrows_cr_18) + " rows and " + str(ncols_cr_18) + " cols in crime_reports_2018")

crime_reports_2019 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2019.csv")
nrows_cr_19, ncols_cr_19 = crime_reports_2019.shape
print("there are " + str(nrows_cr_19) + " rows and " + str(ncols_cr_19) + " cols in crime_reports_2019")

crime_reports_2020 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2020.csv")
nrows_cr_20, ncols_cr_20 = crime_reports_2020.shape
print("there are " + str(nrows_cr_20) + " rows and " + str(ncols_cr_20) + " cols in crime_reports_2020")

crime_reports_2021 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2021.csv")
nrows_cr_21, ncols_cr_21 = crime_reports_2021.shape
print("there are " + str(nrows_cr_21) + " rows and " + str(ncols_cr_21) + " cols in crime_reports_2021")

crime_reports_2022 = pandas.read_csv("data/crime_data/databostongov-crime-incident-reports-august-2015-to-date-source-new-system/crime incident reports - 2022.csv")
nrows_cr_22, ncols_cr_22 = crime_reports_2022.shape
print("there are " + str(nrows_cr_22) + " rows and " + str(ncols_cr_22) + " cols in crime_reports_2022")