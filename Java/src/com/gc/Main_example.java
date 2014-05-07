package com.gc;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main_example {

    // Here is an example solution, in case you get stuck.  I don't know Java, so it probably sucks.
    // It's also not tested well, so may have off-by-one errors and such.

    public static void main(String[] args) throws IOException {

        /******* 1. READING THE DATA *******/
        String currentDir = System.getProperty("user.dir"); // Think this location depends on how you start the app
        List<String> dataLines = Files.readAllLines(Paths.get(currentDir + "\\trainingsample.csv"), Charset.defaultCharset());

        /******* 2. CLEANING UP HEADERS *******/
        List<String> dataNoHeader = dataLines.subList(1, dataLines.size());

        /******* 3. EXTRACTING COLUMNS *******/
        List<String[]> dataValues = new ArrayList<>();

        for (String dataRow : dataNoHeader) {
            dataValues.add(dataRow.split(","));
        }

        /******* 4. CONVERTING FROM STRINGS TO INTS *******/
        List<int[]> dataNumbers = new ArrayList<>();

        for (String[] dataValueRow : dataValues) {
            int[] numberArray = new int[dataValueRow.length];
            for (int index = 0; index < dataValueRow.length; index++) {
                numberArray[index] = Integer.parseInt(dataValueRow[index]);
            }

            dataNumbers.add(numberArray);
        }

        /******* 5. CONVERTING ARRAYS TO CLASSES *******/
        List<DigitRecord> dataRecords = new ArrayList<>();

        for (int[] dataNumberRow : dataNumbers) {
            dataRecords.add(new DigitRecord(dataNumberRow[0], Arrays.copyOfRange(dataNumberRow, 1, dataNumberRow.length)));
        }

        /******* 6. LET'S SEE SOME DIGITS! *******/

        /******* 7. TRAINING vs VALIDATION DATA *******/
        List<DigitRecord> trainingData = dataRecords.subList(0, 1599);
        List<DigitRecord> validationData = dataRecords.subList(1600, 1999);

        /******* 8. COMPUTING DISTANCES *******/

        /******* 9. WRITING THE CLASSIFIER FUNCTION *******/

        /******* 10. SEE THE CLASSIFIER IN ACTION *******/
        for (DigitRecord digit : validationData.subList(0, 10)) {
            System.out.println("Actual Digit: " + digit.getLabel() + " Predicted: " + classify(trainingData, digit.getPixels()));
        }

        /******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******/
        int sum = 0;
        for (DigitRecord digit : validationData) {
            if (digit.getLabel() == classify(trainingData, digit.getPixels())) {
                sum++;
            }
        }

        System.out.println("Percent correct: " + (double) sum / validationData.size() * 100);

    }

    private static int calculateDistance(int[] testDigit, int[] knownDigit) {
        int testSum = 0;
        for (int pixelDensity : testDigit)
            testSum += pixelDensity;

        int knownSum = 0;
        for (int pixelDensity : knownDigit)
            knownSum += pixelDensity;

        return Math.abs(testSum - knownSum);

//        int sum = 0;
//        for (int index = 0; index < testDigit.length; index++) {
//            int distance = testDigit[index] - knownDigit[index];
//            sum += distance * distance; // euclidean distance
//        }
//
//        return sum;
    }

    private static int classify(List<DigitRecord> trainingData, int[] unknownDigit) {
        int lowestDistanceIndex = -1;
        int lowestDistance = Integer.MAX_VALUE;

        for (int index = 0; index < trainingData.size(); index++) {
            int distance = calculateDistance(unknownDigit, trainingData.get(index).getPixels());
            if (distance < lowestDistance) {
                lowestDistance = distance;
                lowestDistanceIndex = index;
            }
        }

        return trainingData.get(lowestDistanceIndex).getLabel();
    }

    static class DigitRecord {
        private int _label;
        private int[] _pixels;

        DigitRecord(int label, int[] pixels) {
            _label = label;
            _pixels = pixels;
        }

        public int getLabel() {
            return _label;
        }

        public int[] getPixels() {
            return _pixels;
        }
    }
}