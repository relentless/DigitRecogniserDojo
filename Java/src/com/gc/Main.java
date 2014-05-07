package com.gc;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    // Follow the steps below to implement your digit classifier.
    // If you need a bit of help, check out the hints.
    // If you need even more, have a peek at the example solutions.  (But don't let anyone see you!)

    // The first few steps have been implemented for you, so you can get onto the interesting part!

    public static void main(String[] args) throws IOException {

        /******* 0. GETTING TO KNOW YOUR DATA *******/

        // First let's have a look at "trainingsample.csv".  Understand the format,
        // so you know what you're working with.
        // Each line has the digit (0-9), then 784 numbers representing pixels, with
        // greyscale values from 0-255

        /******* 1. READING THE DATA *******/

        // First let's read the contents of "trainingsample.csv" into an array, one element per line
        String currentDir = System.getProperty("user.dir");
        List<String> dataLines = Files.readAllLines(Paths.get(currentDir + "\\trainingsample.csv"), Charset.defaultCharset());

        /******* 2. CLEANING UP HEADERS *******/

        // Did you notice that the file has a header? We want to get rid of it.
        List<String> dataNoHeader = dataLines.subList(1, dataLines.size());

        /******* 3. EXTRACTING COLUMNS *******/

        // Each line of the file is a comma-separated list of numbers.
        // Break each line of the file into an array of strings.
        List<String[]> dataValues = new ArrayList<>();

        for (String dataRow : dataNoHeader) {
            dataValues.add(dataRow.split(","));
        }

        /******* 4. CONVERTING FROM STRINGS TO INTS *******/

        // Now that we have an array containing arrays of strings,
        // and the headers are gone, we need to transform it into an array of arrays of integers.

        List<int[]> dataNumbers = new ArrayList<int[]>();

        for (String[] dataValueRow : dataValues) {
            int[] numberArray = new int[dataValueRow.length];
            for (int index = 0; index < dataValueRow.length; index++) {
                numberArray[index] = Integer.parseInt(dataValueRow[index]);
            }

            dataNumbers.add(numberArray);
        }

        /******* 5. CONVERTING ARRAYS TO CLASSES *******/

        // Rather than dealing with a raw array of ints,
        // for convenience let's store these into an array of something a bit more structured.
        // A class called 'DigitRecord' has been started for your convenience - let's use that.

        List<DigitRecord> dataRecords = new ArrayList<>();

        // [ YOUR CODE GOES HERE! ]

        /******* 6. LET'S SEE SOME DIGITS! *******/

        // Unfortunately I haven't made a digit visualiser for Java, so you won't be able to see the hand-drawn digits.
        // Onto step 7!

        /******* 7. TRAINING vs VALIDATION DATA *******/

        // How will we see if our algorithm works?  We need to take our known character data and split
        // it into 'training data' and the 'validation set'.
        // Let's keep say 1600 records for training and 400 for validation.

        // [ YOUR CODE GOES HERE! ]

        /******* 8. COMPUTING DISTANCES *******/

        // We need to compute the distance between two images, so we can see what the 'closest' ones are.
        // Go and implement the calculateDistance() method below.  We'll use it in the next step.

        /******* 9. WRITING THE CLASSIFIER FUNCTION *******/

        // We are now ready to write the classifier!
        // Go and implement the classify() method below. We'll use it in the next step.

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

        System.out.println("Percent correct: ??");
    }

    private static int calculateDistance(int[] testDigit, int[] knownDigit) {
        // To implement at Step 8!

        // Determine the 'distance' between two digits.
        // This can be as complex or simple as you like.
        // Why not start simple, and once you've got everything working, see if you
        // can make it better/faster?

        // [ YOUR CODE GOES HERE! ]

        return -1;
    }

    private static int classify(List<DigitRecord> trainingData, int[] unknownDigit) {
        // To implement at Step 9!

        // The classifier should search for the 'closest' example in our training data,
        // and use that as the predicted classification of the unknown image.
        // Which is the closest?  calculateDistance() should tell us!

        // This is where the 'k' of KNN comes in - k defines how many of the closest training data
        // records we use to predict the unknown digit.  For now, let's just use the closest example,
        // to keep things simple (so k=1).

        // [ YOUR CODE GOES HERE! ]

        return -1;
    }

    static class DigitRecord {
        // To implement at Step 5!

        // You'll want a property for the class (often called the 'Label'), and one for the Pixels.

        // [ YOUR CODE GOES HERE! ]
    }
}