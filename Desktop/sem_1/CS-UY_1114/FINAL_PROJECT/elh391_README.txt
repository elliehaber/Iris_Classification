Name: Ellie Haber
NetID: elh391
Section: EXL2

State of Assignment:

I have completed the Iris classification project.


The project follows the guidelines of the example functions given.

The create_table function accurately reads in the train_data and test_data files and and puts the 
file data into a tuple consisting of two float lists for the petal width and length data and a string
list for the names of the flowers.

The print_range_max_min function accurately finds the max, min, and range of the petal
width and petal length list.

The find_mean function accurately determines the mean of the feature passed to the
function as a parameter.

The find_std_dev function accurately finds the standard deviation of a feature using
the mean calculated in the find_mean function

The normalize_data function accurately prints the mean and standard deviation of the dataset sent to the 
Function as a parameter. It then normalizes each individual feature and finds the normalized mean and 
Standard deviation. 

The make_predictions function accurately calls on the find_dist function to determine each test_data coordinate's "nearest neighbor", in order to determine the type of iris by finding an iris from the training set with the Most similar features, or nearest distance. 

The find_dist function is called in the make_predictions function to determine the
distance between the training data and test data, and an if statement helps to determine
the training data closest to the test data, and that label (iris name) is added to a
list which should get returned.

The find_error function returns the error percentage of the make_predictions function by comparing the actual Iris types of each of the test_data irises and comparing them to the predictions made. 

The plot_data function calls on the draw_axes function, which uses turtle to draw the x and y axes of the 
coordinate graph. plot_data then plots coordinates representing all of the training data and predictions. 
Predictions are represented by squares and training data is represented by circles. Each iris type is a 
different color and incorrect predictions are their own color. 

The draw_key function calls on the train_key and predictions_key functions to draw a key for the graph. 
The train_key function outputs the portion of the key representing the training data and the predictions_key
function outputs the portion of the key representing the predictions.


 
