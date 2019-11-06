Name: Ellie Haber
NetID: elh391
Section: EXL2

State of Assignment:

The Iris project is not yet completed, as I have not yet completed the graph representing
the data analysis of my program.

I have completed the create_table function, the
print_range_max_min function, the find_mean and find_std_dev functions, the
normalize_data function, the find_error function, and am currently still modifying my
make_predictions function.

As of right now, the make_predictions function upon running it results in IDLE freezing
and I am still attempting to determine the cause of this error.

The project follows the guidelines of the example functions given.

The create_table function accurately reads in files and and puts the file data into
a tuple consisting of two float lists for the petal width and length data and a string
list for the names of the flowers.

The print_range_max_min function accurately finds the max, min, and range of the petal
width and petal length list.

The find_mean function accurately determines the mean of the feature passed to the
function as a parameter

The find_std_dev function accurately finds the standard deviation of a feature using
the mean calculated in the find_mean function

The normalize data function appears to work, both the mean and standard deviation
calculated seem to be close to the respective normal values of mean: 0 and std dev: 1,
however, I am still troubleshooting this portion of my program.

The make_predictions function appears to have all the necessary components to properly
run, however, it causes IDLE to freeze when it is run. I am still looking into this
issue. In it, I created two lists, for the test data and training data respectively,
to contain tuples with the petal width and length representing coordinates.

The find_dist function is called in the make_predictions function to determine the
distance between the training data and test data, and an if statement helps to determine
the training data closest to the test data, and that label (iris name) is added to a
list which should get returned.

The find_error function should return the percent of incorrect predictions, however
I haven't yet been able to run it due to the complications with the make_predictions
function.
