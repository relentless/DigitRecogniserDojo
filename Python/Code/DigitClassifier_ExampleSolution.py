import os
import Visualiser
import math
import time

def Main():
    
    """Framework code for tutorial creating a digit classifier using K-Nearest-Neighbours.
    Ported to Python from Grant Crofton's C# version - http://goo.gl/q6Qouw - by Alex Garland.
    I've tried to avoid code that won't work in Python 2 but have only tested in v3.
    """

    #       ************    Worked example solution     ************


    #   ******* 1. READING THE DATA *******
    dataLines = open(os.path.join(os.getcwd(), os.pardir, "Data", "trainingsample.csv")).readlines()
    
    #   ******* 2. CLEANING UP HEADERS *******
    dataNoHeader = dataLines[1:]    

    #   ******* 3. EXTRACTING COLUMNS *******
    dataValues = [line.split(',') for line in dataNoHeader]

    
    #   ******* 4. CONVERTING FROM STRINGS TO INTS *******
    # (type coercion within a nested list comprehension)
    dataNumbers = [[int(element) for element in line] for line in dataValues]


    #   ******* 5. CONVERTING ARRAYS TO CLASSES *******/
    # Rather than dealing with a raw array of ints, let's store these into a 'DigitRecord' class.
    dataRecords =[DigitRecord(line[0], line[1:]) for line in dataNumbers]


    #   ******* 6. LET'S SEE SOME DIGITS! *******
    # Run for the top 5...
    for digit in dataRecords[:5]:
        Visualiser.Draw("Displaying: {0:d}".format(digit.Label), digit.Pixels)

    #   ******* 7. TRAINING vs VALIDATION DATA *******
    trainingData = dataRecords[:1600]
    validationData = dataRecords[1600:]


    #   ******* 8. COMPUTING DISTANCES *******
    # (See below for calculateDistance function)
    #   ******* 9. WRITING THE CLASSIFIER FUNCTION *******
    # (See below for classifier function)


    #   ******* 10. SEE THE CLASSIFIER IN ACTION *******
    numberToValidate = 10  # So we can limit the number it runs
    for validationRecord in validationData[:numberToValidate]:
        print("Actual: {0}, Predicted: {1}".format(validationRecord.Label, classify(trainingData, validationRecord.Pixels)))


    #   ******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******
    # Validate all records and calculate the hit rate - running within a timer so it can be optimised if you want
    
    startTime = time.time()

    fractionCorrect = sum([1.0 if (classify(trainingData, validationRecord.Pixels) == validationRecord.Label) else 0.0
                              for validationRecord in validationData]) / len(validationData)

    print("Percentage correct: {0}%".format(fractionCorrect * 100))
    print("Completed in {:0.2f} seconds".format(time.time() - startTime))

    #   *******     OUTPUT      *******
    #   Percentage correct: 88.75%
    #   Completed in 458.67 seconds     (Intel 987 (1.5GHz))
    #   Completed in 203.33 seconds     (Intel T4400 (2.2GHz))

    # So - the hit rate is respectable, but even at this level of complexity it takes a decent amount of time to run.
    # Can it be optimised?


def calculateDistance (testPixels, knownPixels):
    
    # "Sum the pixels of each and use the different between the sums"
    # return math.fabs(sum(testPixels) - sum(knownPixels))
    # Gets almost no correct matches so let's move on and use the next one:
    # "Compare each pixel and add up the differences"
    return sum([math.fabs(pixelPair[0] - pixelPair[1]) for pixelPair in zip(testPixels, knownPixels)])

    
def classify (trainingData, unknownPixels):

    # Take unknown pixels and find the single (K=1) nearest neighbour based on the calculateDistance function
    return sorted(trainingData, key = lambda trainingRecord: calculateDistance(unknownPixels, trainingRecord.Pixels))[0].Label

    # If we wanted to add an additional parameter K and take that number of nearest neighbours we could do something like:
    # neighbours = [record.Label for record in sorted(trainingData, key = lambda trainingRecord: calculateDistance(unknownPixels, trainingRecord.Pixels))[:K]]
    # and then do some further processing to classify based on those K items - i.e. probably most common label value.

class DigitRecord:
    
    def __init__ (self, DigitLabel, DigitPixels):
        self.Label = DigitLabel
        self.Pixels = DigitPixels




if __name__ == '__main__':
    Main()
