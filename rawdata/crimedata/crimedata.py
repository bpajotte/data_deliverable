import pandas

# source for data: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip
# data readme: https://github.com/stanford-policylab/opp/blob/master/data_readme.md#statewide-ma

# pull data into pandas
csv_stanford = pandas.read_csv("rawdata\crimedata\openpolicingstanfordedu\ma-state-patrol.csv")
nrows_stanford, ncols_stanford = csv_stanford.shape
print("there are " + str(nrows_stanford) + " rows and " + str(ncols_stanford) + " cols in raw csv")
# filter by boston
csv_stanford = csv_stanford[csv_stanford['location'] == "BOSTON"]
nrows_stanford, ncols_stanford = csv_stanford.shape
print("there are " + str(nrows_stanford) + " rows and " + str(ncols_stanford) + " cols in filtered data")

