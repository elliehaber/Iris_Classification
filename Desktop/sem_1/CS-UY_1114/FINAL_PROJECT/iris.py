#Ellie Haber
#CS-UY 1114
#26 November 2018
# Final project

import math
import turtle

def create_table(file_name):
    """
    sig: str -> tuple(list(float), list(float), list(str))
    Given a file name, read the file into a tuple containing
    two lists of type float and one list of type string.
    The features of the dataset should be of type float
    and the label should be of type string. 
    """
    iris_file = open(file_name, 'r')

    petal_len = []
    petal_wid = []
    iris_type = []
    data = (petal_len, petal_wid, iris_type)
    for line in iris_file:
        info = line.split(',')
        for s in info:
            if s == info[0]:
                petal_len.append(s)
            elif s == info[1]:
                petal_wid.append(s)
            else:
                iris_type.append(s.rstrip())
    return data

def print_range_max_min(data):
    """
    sig: tuple(list(float), list(float)) -> NoneType
    Print the max, min and range of both features in the dataset.
    """
    max_feature = 0
    min_feature = 1000
    i = 1
    for lst in data:
        for num in lst:
            if float(num) > float(max_feature):
                max_feature = num
            if float(num) < float(min_feature):
                min_feature = num

        range_feature = float(max_feature) - float(min_feature)
        print("Feature", i, "- min: ", min_feature, "max:", max_feature, \
              "range: ", range_feature)
        max_feature = 0
        min_feature = 1000
        i+=1
        
    
            
def find_mean(feature):
    """
    sig: list(float) -> float
    Return the mean of the feature.
    """
    sum_feature = 0
    count = 0
    for num in feature:
        sum_feature += float(num)
        count +=1

    mean_feature = sum_feature/count

    return mean_feature
        

    

def find_std_dev(feature, mean):
    """
    sig: list(float), float -> float
    Return the standard deviation of the feature. 
    """
    numerator = 0
    total = len(feature)
    for num in feature:
        numerator += math.pow(float(num)-mean, 2) #diff between num and mean squared for each value in list
    std_dev = math.sqrt(numerator/total)
    return std_dev
        

def normalize_data(data):
    """
    sig: tuple(list(float), list(float), list(str)) -> NoneType
    Print the mean and standard deviation for each feature.
    Normalize the features in the dataset by
    rescaling all the values in a particular feature
    in terms of a mean of 0 and a standard deviation of 1.
    Print the mean and the standard deviation for each feature, now normalized.
    After normalization, each of your features should display a mean of 0
    or very close to 0 and a standard deviation of 1 or very close to 1. 
    """
    
    norm_data = []
    i = 1
    data = data[:2] #sets data to only the two float lists (features)
    for lst in data:
        feat_mean = find_mean(lst)
        feat_std_dev = find_std_dev(lst, feat_mean)
        
        print("Feature", i, "- mean:", feat_mean, "std dev: ", feat_std_dev)

        for num in lst:
            norm_data.append((float(num) - feat_mean)/feat_std_dev)

        #normalized data    
        feat_mean = find_mean(norm_data)
        feat_std_dev = find_std_dev(norm_data, feat_mean)
        print("Feature", i, "after normalization - mean:", feat_mean, \
              "std dev: ", feat_std_dev)
        i+=1
        lst[:] = norm_data
        
        norm_data = []


def make_predictions(train_set, test_set):
    """
    sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)) -> list(str)
    For each observation in the test set, you'll need to check all of
    the observations in the training set to see which is the `nearest neighbor.'
    The function should make a call to the function find_dist.
    Accumulate a list of predicted iris types for each of the test set
    observations. Return this prediction list.
    """
    test_coor = []
    train_coor = []


    test_dist = []
    nearest = 100000000
    dist = 0
    label = ''
    predictions = []
    
    for i in range(len(test_set[0])):
        test_coor.append((test_set[0][i], test_set[1][i])) #coordinate list containing tuples for test

    for j in range(len(train_set[0])):
        train_coor.append((train_set[0][j], train_set[1][j])) #coordinate list containing tuples for train

    for point in range(len(test_coor)):
        for coord in range(len(train_coor)):
            x1, y1 = train_coor[coord][0], train_coor[coord][1]
            x2, y2 = test_coor[point][0], test_coor[point][1]

            dist = find_dist(x1, y1, x2, y2) #calls find_dist to determine distance between coordinates
            if dist < nearest:
                nearest = dist     #iterates loop to find closest data points
                label = train_set[2][coord]
        predictions.append(label)
        nearest = 1000000
        
    return predictions
                
        

def find_dist(x1, y1, x2, y2):
    """
    sig: float, float, float, float -> float
    Return the Euclidean distance between two points (x1, y1), (x2, y2).
    """
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    
    x_diff = math.pow(x2-x1, 2) #difference between x coordinates, squared
    y_diff = math.pow(y2-y1, 2) #difference between y coordinates, squared

    dist = math.sqrt(x_diff + y_diff)
    return dist
        
def find_error(test_data, pred_lst):
    """
    sig: tuple(list(float), list(float), list(str)) -> float
    Check the prediction list against the actual labels for
    the test set to determine how many errors were made.
    Return a percentage of how many observations in the
    test set were predicted incorrectly. 
    """
    correct = 0
    i = 0
    total = len(pred_lst)
    test_data = test_data[2]

    for label in test_data:
        if label == pred_lst[i]: #compares each iris type in the test data
            correct+=1           #to the pedicted type of irisny
        i+=1

    percent_incorr = (1- (correct/total))*100

    return percent_incorr
    

def plot_data(train_data, test_data, pred_lst):
    """
    sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)), list(str)
        -> NoneType
    Plot the results using the turtle module. Set the turtle window size to 500 x 500.
    Draw the x and y axes in the window. Label the axes "petal width" and "petal length". 
    Plot each observation from your training set on the plane, using a circle shape
    and a different color for each type of iris. Use the value of the first feature
    for the x-coordinate and the value of the second feature for the y-coordinate.
    Use a dot size of 10. Recall that the features have been normalized to have a mean
    of 0 and a standard deviation of 1. You will need to `stretch' your features across
    the axes to make the best use of the 500 x 500 window. Ensure that none of your
    points are plotted off screen. Also plot each correct prediction from your test
    set in the corresponding color. Use a square to indicate that the value is a prediction.
    Plot the incorrect predictions that were made for the test set in red, also using a
    square to indicate that it was a prediction. Include a key in the upper left
    corner of the plot as shown in the sample plot. The function will make a call
    to the function draw_key in order to accomplish this task. 
    """

    #creates skeleton graph
    iris_graph = turtle.Screen()
    iris_graph.title("Iris Classification")
    iris_graph.screensize(500,500)
    draw_axes(500,500) #calls on function to draw Cartesian graph
    
    iris = turtle.Turtle()

    #initializing variables
    lst_tup = []
    x = 0
    y = 0
    
    h = 0

    train_name = train_data[2] #list of iris names from training datsa
    test_name = test_data[2] #list of names from test data

    

    #plots test data
    for name in test_name:
        if name == pred_lst[h]:   #only plots correct predictions
            if name == 'Iris-setosa':   #determines coord color based on name
                iris.color("dark magenta")
            elif name == 'Iris-virginica':
                iris.color("dark orange")
            else:
                iris.color("steel blue")
        
        else:
            iris.color("maroon")   #incorrect prediction
        x = test_data[0][h]  #x coordinate is petal length from test data
        y = test_data[1][h]  #y coordinate is petal width from test data
        iris.speed(0)        #both points correspond to the correct name in list
        iris.ht()
        iris.penup()
        iris.goto(200* float(x), 215* float(y))
        iris.pendown()
        iris.shape('square')   #square shaped point represents predictions
        iris.turtlesize(.5)
        iris.stamp()
        h+=1 
            
  

    #plots training data
    h = 0    
        
    for name in train_name:     
        if name == 'Iris-setosa':     #determines correct colors for coord
            iris.color("dark magenta")   
        elif name == 'Iris-virginica':
            iris.color("dark orange")
        else:
            iris.color("steel blue")
        
        x = train_data[0][h] #x coord is petal length for training data
        y = train_data[1][h] #y coord is petal width for training data
        iris.speed(0)
        iris.ht()
        iris.penup()
        iris.goto(200* float(x), 215* float(y))
        iris.pendown()
        iris.dot(10)    #dot for training data coordinates
        h+=1

    draw_key() #calls function to draw key for graph

      
  
        
    
    
def draw_axes(window_len, window_wid):
    """
    sig: (int, int) -> NoneType
    Draw the x and y axes of the graph to fill a 500x500 window
    and label each axis 
    """

    # x-axis
    iris = turtle.Turtle()
    iris.ht()
    iris.speed(0)
    iris.penup()
    iris.backward(500)
    iris.pendown()
    iris.forward(1000)


    iris.penup()
    iris.backward(120)
    iris.left(90)
    iris.forward(10)
    iris.right(90)
    iris.pendown()
    iris.write('petal length', font = ('Soho', 14)) #displays x-axis label


    iris.penup()
    iris.goto(0,0)


    # y-axis
    iris.left(90)
    iris.forward(500)
    iris.pendown()
    iris.backward(1000)

    iris.penup()
    iris.forward(70)
    iris.right(90)
    iris.forward(10)
    iris.pendown()
    iris.write('petal width', font = ('Soho', 14)) #displays y-axis label


    
def draw_key():
    """
    sig: () -> NoneType
    Draw the legend for the plot indicating which group is shown by each color/shape combination.  
    """

    train_key() #calls function to draw key for training data coordinates
    predictions_key() #calls function to draw key for prediction coordinates

    

def predictions_key():
    """
    sig: () -> NoneType
    Draw the legend for the predictions group of the plot indicating which
    group is shown by each color
    """
    iris = turtle.Turtle()
    iris.speed(0)
    iris.ht()

    #initial x and y coordinates for symbol
    x_shape = -400
    y_shape = 315

    #initial x and y coordinates for iris type/prediction v. training status
    x_name = -380
    y_name = 307


    for i in range(4):
        iris.penup()
        iris.goto(x_shape, y_shape)
        iris.pendown()
        if i == 0:
            iris.color('dark magenta')     #determines color 
        elif i == 1:
            iris.color('steel blue')
        elif i == 2:
            iris.color('dark orange')
        else:
            iris.color('maroon')
        iris.shape('square')               #square for predictions
        iris.turtlesize(.5)
        iris.stamp()
        iris.penup()
        iris.goto(x_name, y_name)
        iris.color('black')
        iris.pendown()

        if i == 0:
            iris.write("predicted Iris-setosa", font = ('Soho', 14))
        elif i == 1:
            iris.write("predicted Iris-versicolor", font = ('Soho', 14))
        elif i == 2:
            iris.write("predicted Iris-virginica", font = ('Soho', 14))
        else:
            iris.write("predicted Incorrectly", font = ('Soho', 14))
        
        y_shape -= 30 #decrements both y values to create properly aligned key
        y_name -= 30  #with each iteration of the for loop
   
    
    
def train_key():
    """
    sig: () -> NoneType
    Draw the legend for the training group of the plot indicating which
    group is shown by each color 
    """
    iris = turtle.Turtle()
    iris.speed(0)
    iris.ht()

    #initial x and y coordinates for symbol
    x_shape = -400 
    y_shape = 400

    #initial x and y coordinates for iris name/predictions v. training status
    x_name = -380
    y_name = 392

    for i in range(3):
        iris.penup()
        iris.goto(x_shape, y_shape)
        iris.pendown
        if i == 0:
            iris.color('dark magenta')   #determines coord color
        elif i == 1:
            iris.color('steel blue')
        else:
            iris.color('dark orange')
        iris.dot(10)
        iris.penup()
        iris.goto(x_name, y_name)
        iris.color('black')
        iris.pendown()

        if i == 0:
            iris.write("Iris-setosa", font = ('Soho', 14))
        elif i == 1:
            iris.write("Iris-versicolor", font = ('Soho', 14))
        else:
            iris.write("Iris-virginica", font = ('Soho', 14))
    
        y_shape -=30 #decrements y coordinates as loop progresses
        y_name -=30  #properly lists training items in key
        

def main():
    """
    sig: () -> NoneType
    The main body of the program. It will use the other
    functions to load the data, process the training set,
    analyze the test set, and display its conclusions.
    """
    train_data = create_table("iris_train.csv")
    print_range_max_min(train_data[:2])
    print()
    normalize_data(train_data)
    test_data = create_table("iris_test.csv")
    print()
    normalize_data(test_data)
    pred_lst = make_predictions(train_data, test_data)
    error = find_error(test_data, pred_lst)
    print()
    print("The error percentage is: ", error)
    plot_data(train_data, test_data, pred_lst)
main()

