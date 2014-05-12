<?php

ini_set('memory_limit', '1024M'); // Increse memory limit

require 'Visualizer.php';  // This is included in the tutorial code as an additional module,

/**
 * Framework code for tutorial creating a digit classifier using K-Nearest-Neighbours.
 * Ported to PHP from Grant Crofton's C# version by Alfonsas Cirtautas - twitter @acirtautas
 */

// Follow the steps below to implement your digit classifier.
// If you need a bit of help, check out the hints.
// If you need even more, have a peek at the example solutions.  (But don't let anyone see you!)

// The first few steps have been implemented for you, so you can get onto the interesting part!

/******* 0. GETTING TO KNOW YOUR DATA *******/

// First let's have a look at "trainingsample.csv". Understand the format,
// so you know what you're working with.
// Each line has the digit (0-9), then 784 numbers representing pixels, with
// greyscale values from 0-255

/******* 1. READING THE DATA *******/

// First let's read the contents of "trainingsample.csv" into an array, one element per line

$dataLines = file(__DIR__.'/trainingsample.csv');

/******* 2. CLEANING UP HEADERS *******/

// Did you notice that the file has a header? We want to get rid of it.

$dataNoHeader = array_slice($dataLines, 1);

/******* 3. EXTRACTING COLUMNS *******/

// Each line of the file is a comma-separated list of numbers.
// Break each line of the file into an array of strings.

$dataValues = array_map( function ($dataLine) { return explode(',', $dataLine); }, $dataNoHeader);

/******* 4. CONVERTING FROM STRINGS TO INTS *******/

// Now that we have an array containing arrays of strings,
// and the headers are gone, we need to transform it into an array of arrays of integers.

$dataNumbers = array_map( function ($stringArray) { return array_map('intval', $stringArray); }, $dataValues);

/******* 5. CONVERTING ARRAYS TO CLASSES *******/

// Rather than dealing with a raw array of ints,
// for convenience let's store these into an array of something a bit more structured.
// A class called 'DigitRecord' has been started for your convenience - let's use that.

// [ YOUR CODE GOES HERE! ]

/******* 6. LET'S SEE SOME DIGITS! *******/

// Now we have things structured sensibly, if you want, you can have a look at some digits.
// There's a Visualiser class, which has a draw function that can be called like so:
// Visualiser::Draw( "title", $digit->Pixels);

/******* 7. TRAINING vs VALIDATION DATA *******/

// How will we see if our algorithm works?  We need to take our known character data and split
// it into 'training data' and the 'validation set'.
// Let's keep say 1600 records for training and 400 for validation.

// [ YOUR CODE GOES HERE! ]

/******* 8. COMPUTING DISTANCES *******/

// We need to compute the distance between two images, so we can see what the 'closest' ones are.
// Go and implement the calculateDistance() function below.  We'll use it in the next step.

/******* 9. WRITING THE CLASSIFIER FUNCTION *******/

// We are now ready to write the classifier!
// Go and implement the classify() function below. We'll use it in the next step.

/******* 10. SEE THE CLASSIFIER IN ACTION *******/

// Now that we have a classifier, let's see it in action.
// For each example in the validation set, we can use the classifier to predict
// the digit.  Let's take, say, the first 20 classifications and see if it seems to be working
// by writing the actual and predicted values to the console.

// [ YOUR CODE GOES HERE! ]

/******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******/

// Let's judge with a little more accuracy how good our classifier is.
// Let's classify all of the validation records, and work out the % correctly predicted.

// [ YOUR CODE GOES HERE! ]

// If this is going too slowly (e.g. no results within a couple of minutes),
// you might want to try to make your distance calculation faster

// CONGRATULATIONS!  Hopefully, you have a working digit classifier.
// Want to make it better?  See some suggestions below..

/******* 12. NEXT STEPS *******/
// Once you have something working, there are many things you can try to do:
// - Try higher values of k (more neighbours)
// - Improve the distance calculation (
//     compare each pixel,
//     euclidian distance (distance of each pixel squared),
//     distance of each pixel to other powers)
// - Try other things to improve the score (e.g.
//     blur the images,
//     downsize the images)
// - Make it faster (you can use a StopWatch to see how long things take)
// - Submit your classifier to Kaggle (http://www.kaggle.com/competitions)

// There are many more hours of machine learning fun to be had, even for this simple problem.
// Enjoy!

/**
 * @param int[] $testDigit
 * @param int[] $knownDigit
 *
 * @return int
 */
function calculateDistance( $testDigit, $knownDigit) {
    // To implement later - wait for Step 8!

    // Determine the 'distance' between two digits.
    // This can be as complex or simple as you like.
    // Why not start simple, and once you've got everything working, see if you
    // can make it better/faster?

    // [ YOUR CODE GOES HERE! ]

    return 0;
}

/**
 * @param DigitRecord[] $trainingData
 * @param int[]         $unknownPixels
 *
 * @return int
 */
function classify ($trainingData, $unknownPixels) {
    // To implement later - wait for Step 9!

    // The classifier should search for the 'closest' example in our training data,
    // and use that as the predicted classification of the unknown image.
    // Which is the closest?  calculateDistance() should tell us!

    // This is where the 'k' of KNN comes in - k defines how many of the closest training data
    // records we use to predict the unknown digit.  For now, let's just use the closest example,
    // to keep things simple (so k=1).

    // [ YOUR CODE GOES HERE! ]

    return 0;
}

class DigitRecord {
    // To implement later - wait for Step 5!

    // You'll want a property for the class (often called the 'Label'), and one for the Pixels.

    // [ YOUR CODE GOES HERE! ]
}
