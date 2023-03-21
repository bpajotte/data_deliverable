import pandas

# source for data: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip, MA State Patrol
# filepath = 

csv = pandas.read_csv("ma_statewide_2020_04_01.csv")
nrows, ncols = csv.shape
print("there are " + str(nrows) + " rows and " + str(ncols) + " cols in raw csv")

filtered_data = csv[csv['location'] == "BOSTON"]
nrows, ncols = filtered_data.shape
print("there are " + str(nrows) + " rows and " + str(ncols) + " cols in filtered data")