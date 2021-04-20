import pandas as pd 
import csv
import statistics

df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
height_median=statistics.median(height_list)
height_mode=statistics.mode(height_list)

weight_mean=statistics.mean(weight_list)
weight_median=statistics.median(weight_list)
weight_mode=statistics.mode(weight_list)

print("mean of height is {}".format(height_mean))
print("median of height is {}".format(height_median))
print("mode of height is {}".format(height_mode))

print("mean of weight is {}".format(weight_mean))
print("median of weight is {}".format(weight_median))
print("mode of weight is {}".format(weight_mode))

height_std_deviation=statistics.stdev(height_list)

#specifying ranges for first second and third standard deviation
height_first_std_deviation_start,height_first_std_deviation_end=height_mean-height_std_deviation,height_mean+height_std_deviation
height_second_std_deviation_start,height_second_std_deviation_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_std_deviation_start,height_third_std_deviation_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)

height_list_of_data_within_1_std_deviation=[result for result in height_list if result>height_first_std_deviation_start and result<height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation=[result for result in height_list if result>height_second_std_deviation_start and result<height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation=[result for result in height_list if result>height_third_std_deviation_start and result<height_third_std_deviation_end]

print("standard deviation of this data is {}".format(height_std_deviation))
print("{}% of data lies within one standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data lies within two standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data lies within three standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

weight_std_deviation=statistics.stdev(weight_list)

#specifying ranges for first second and third standard deviation
weight_first_std_deviation_start,weight_first_std_deviation_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_second_std_deviation_start,weight_second_std_deviation_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start,weight_third_std_deviation_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)

weight_list_of_data_within_1_std_deviation=[result for result in weight_list if result>weight_first_std_deviation_start and result<weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation=[result for result in weight_list if result>weight_second_std_deviation_start and result<weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation=[result for result in weight_list if result>weight_third_std_deviation_start and result<weight_third_std_deviation_end]

print("standard deviation of this data is {}".format(weight_std_deviation))
print("{}% of data lies within one standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data lies within two standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data lies within three standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))