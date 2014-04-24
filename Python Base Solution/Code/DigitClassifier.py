import sys
import os
import math

def Main():
    
    """Framework code for tutorial creating a digit classifier using K-Nearest-Neighbours.
    Ported to Python from Grant Crofton's C# version - http://goo.gl/q6Qouw - by Alex Garland.
    I've tried to avoid code that won't work in Python 2 but have only tested in v3.
    """

    #   ******* 0. GETTING TO KNOW YOUR DATA *******

    # First let's have a look at "trainingsample.csv".  Understand the format, 
    # so you know what you're working with.
    # Each line has the digit (0-9), then 784 numbers representing pixels, with
    # greyscale values from 0-255


    #   ******* 1. READING THE DATA *******

    # First let's read the contents of "trainingsample.csv" into an array, one element per line
    dataLines = open(os.path.join(os.getcwd(), os.pardir, "data", "trainingsample.csv")).readlines()
    

    #   ******* 2. CLEANING UP HEADERS *******

    # Did you notice that the file has a header? We want to get rid of it.
    dataNoHeader = dataLines[1:]    


    #   ******* 3. EXTRACTING COLUMNS *******

    # Each line of the file is a comma-separated list of numbers.
    # Break each line of the file into an array of strings.
    dataValues = [line.split(',') for line in dataNoHeader]

    
    #   ******* 4. CONVERTING FROM STRINGS TO INTS *******

    # In C# we would now have an array containing arrays of strings,
    # and would need to transform it into an array of arrays of integers.
    # Python does not use static types - we could just go ahead and see what happens
    # when we try and use the elements as integers later in our code.
    # However, if we want to ensure at this stage that each element is an integer
    # - throwing an error if not - we can do something like this
    # (type coercion within a nested list comprehension):    
    dataNumbers = [[int(element) for element in line] for line in dataValues]




###     TODO - pretty much everything from here on down needs further rework as of 24/4/2014    ###

    #   ******* 5. CONVERTING ARRAYS TO CLASSES *******/

    # Rather than dealing with a raw array of ints,
    # for convenience let's store these into an array of something a bit more structured.
    # A class called 'DigitRecord' has been started for your convenience - let's use that.

##            #region 5. Hints
##            // myCollection.Select again!
##            // To create a new instance of a class, new MyClass { Property1 = "hi", Property2 = [1,2,3] }
##            // Methods like Skip(), Take() and First() could come in handy.
##            // myCollection.ToArray() might also be useful.
##            #endregion

    # [ YOUR CODE GOES HERE! ]

##            #region 5. Example Solution(s)
##            //var dataRecords = dataNumbers.Select( items => 
##            //    new DigitRecord { Label = items.First(), Pixels = items.Skip(1).ToArray() }
##            //    ).ToArray(); // Making it an array at this stage can speed things up a fair bit
##            #endregion


    #   ******* 6. LET'S SEE SOME DIGITS! *******
 
    # Now we have things structured sensibly, if you want, you can have a look at some digits.
    # There's a Visualiser class, which has a draw function that can be called like so:
    # Visualiser.Draw( "title", digit.Pixels);
    # Note: just draw one at a time, unless you want to spend the next 10 minutes closing 1000 windows!

##    region 6. Example Solution(s)
##            //foreach (var item in dataRecords.Take(1)) {
##            //    Visualiser.Draw(item.Label.ToString(), item.Pixels);
##            //}
##            #endregion


##            /******* 7. TRAINING vs VALIDATION DATA *******/
##
##            // How will we see if our algorithm works?  We need to take our known character data and split
##            // it into 'training data' and the 'validation set'.
##            // Let's keep say 1600 records for training and 400 for validation.
##
##            #region 7. Hints
##            // Take() and Skip() should come in handy again
##            #endregion
##
##            // [ YOUR CODE GOES HERE! ]
##
##            #region 7. Example Solution(s)
##            //var trainingData = dataRecords.Take(1600);
##            //var validationData = dataRecords.Skip(1600);
##            #endregion
##
##            /******* 8. COMPUTING DISTANCES *******/
##
##            // We need to compute the distance between two images, so we cann see what the 'closest' ones are.
##            // Go and implement the calculateDistance() method below.  We'll use it in the next step.
##
##            /******* 9. WRITING THE CLASSIFIER FUNCTION *******/
##
##            // We are now ready to write the classifier!
##            // Go and implement the classify() method below. We'll use it in the next step.
##
##            /******* 10. SEE THE CLASSIFIER IN ACTION *******/
##
##            // Now that we have a classifier, let's see it in action.
##            // For each example in the validation set, we can use the classifier to predict
##            // the digit.  Let's take, say, the first 20 classifications and see if it seems to be working
##            // by writing the actual and preicted values to the console.
##
##            // [ YOUR CODE GOES HERE! ]
##
##            #region 10. Example Solution(s)
##            //validationData
##            //    .Take(20)
##            //    .ToList()
##            //    .ForEach(validationDigit =>
##            //        Console.WriteLine("Actual: {0}, Predicted: {1}", validationDigit.Label, classify(trainingData, validationDigit.Pixels)));
##            #endregion
##
##            /******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******/
##
##            // Let's judge with a little more accuracy how good our classifier is. 
##            // Let's classify all of the validation records, and work out the % correctly predicted.
##
##            // [ YOUR CODE GOES HERE! ]
##
##            #region 11. Example Solution(s)
##            //var fractionCorrect = validationData.Average(validationDigit =>
##            //    classify(trainingData, validationDigit.Pixels) == validationDigit.Label ? 1.0 : 0.0);
##
##            //Console.WriteLine("Percent correct: {0}%", fractionCorrect * 100);
##            #endregion


        

    # CONGRATULATIONS!  Hopefully, you have a working digit classifier.
    # Want to make it better?  See some suggestions below..

    #   ******* 12. NEXT STEPS *******
    # Once you have something working, there are many things you can try to do:
    #   - Try higher values of k (more neighbours)
    #   - Improve the distance calculation (
    #       compare each pixel, 
    #       euclidian distance (distance of each pixel squared), 
    #       distance of each pixel to other powers)
    #   - Try other things to improve the score (e.g.
    #       blur the images, 
    #       downsize the images)
    #   - Make it faster (you can use a StopWatch to see how long things take)
    #   - Submit your classifier to Kaggle (http://www.kaggle.com/competitions)

    # There are many more hours of machine learning fun to be had, even for this simple problem.
    # Enjoy!

def calculateDistance (testDigit, knownDigit):

    # To implement later - wait for Step 8!

    # Determine the 'distance' between two digits.
    # This can be as complex or simple as you like.
    # Why not start simple, and once you've got everything working, see if you
    # can make it better/faster?

    # Suggestions, in order of complexity:
    # Return a hard-coded number
    # Sum the pixels of each and use the different between the sums
    # Compare each pixel and add up the differences
    # Use Euclidean distance (each pixel difference^2), or some other power

    # [ YOUR CODE GOES HERE! ]

    int(0)     # return value - replace 0 with the result of your calculation

    # Scroll down to bottom of the file for example solution - difference between all pixels added together



def classify (trainingData, unknownPixels):

     # To implement later - wait for Step 9!


     # The classifier should search for the 'closest' example in our training data,
     # and use that as the predicted classification of the unknown image.
     # Which is the closest?  calculateDistance() should tell us!


     # This is where the 'k' of KNN comes in - k defines how many of the closest training data
     # records we use to predict the unknown digit.  For now, let's just use the closest example,
     # to keep things simple (so k=1).

    # TODO - we have a C# hint "myCollection.OrderBy() takes a lambda which can be used to get the collection sorted how we like"
    # We could do with a Python equivalent.

    # [ YOUR CODE GOES HERE! ]


    0   # return value - replace 0 with the result of your calculation



# class DigitRecord:
    # To implement later - wait for Step 5!

    # You'll want a data attribute for the class (often called the 'Label'), and one for the Pixels.

    # [ YOUR CODE GOES HERE! ]
    




# Standard Python boilerplate;
# This line executes the main method when this file is called directly (rather than as a library).
if __name__ == '__main__':
    Main()




#   ******* EXAMPLE SOLUTIONS *******

#   calculateDistance function - difference between all pixels added together
#   math.fabs(sum(testDigit) - sum(knownDigit)


##            #region 9. Example Solution(s)
##            //var nearestNeighbour =
##            //    trainingData
##            //        .OrderBy(trainingDigit => calculateDistance(trainingDigit.Pixels, unknownPixels))
##            //        .First();
##
##
##            //return nearestNeighbour.Label;
##            #endregion
##        }
##    }
