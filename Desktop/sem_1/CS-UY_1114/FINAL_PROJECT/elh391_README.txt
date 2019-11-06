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

I strayed from the starter code by creating the draw_axes function, the train_key function, and the 
predictions_key function. I created these functions to improve the readability of my code by breaking down the
problems I needed to solve into simpler steps. 

I took artistic liberties in my graph by changing the colors used in my graph and adding a window title.

A feature I would have liked to implement is to find more than just one nearest neighbor in my algorithm, since
this could help reduce the error percentage of it. It also would have been interesting to try to create an 
algorithm predicting iris type with possibly more features than just petal measurements to analyze.

I am satisfied with the result because I feel that I accurately created an algorithm that predicts the iris-type
of an iris given only the measurements of its petals. I was also able to visualize the results of my code 
Through a graph made in turtle, which I feel was well-executed. 

I found normalizing the data to be challenging initially because I could not figure out how to change the 
elements of the data being normalized since it was a tuple and the function had no return value. However, I determined that by changing the elements of the lists within the tuple, I could successfully normalize the data.
The actual algorithm for making predictions about the iris data was actually easier than I anticipated. I am 
Proud of the way I went about creating the make_predictions function, and I'm also proud of how I broke down the process of creating my graph into multiple functions and loops in order to make the code more readable and efficient. 

I would approach the problem differently in the future by writing out my algorithm first before coding anything and ensuring that I had a whole understanding of the problem itself before jumping into the actual coding of it. 

I thought the instructions were very clear and the starter code was very helpful in allowing a large, complex problem to be broken down into a series of simpler problems to solve. 

I found the assignment very interesting and I now want to pursue machine learning in my computer science career. This project has given me insight into the real-world applications of the programming skills I have learned in this class. Moreover, it has introduced me to an area of computer science that I find fascinating and hope to continue pursuing. 