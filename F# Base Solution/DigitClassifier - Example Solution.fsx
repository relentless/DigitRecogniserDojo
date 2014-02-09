#load "visualiser.fs"

open System
open System.IO
open Visualiser

(******* 1. GETTING SOME DATA *******)
 
// First let's read the contents of "trainingsample.csv" into an array, one line per element

let dataLines = File.ReadAllLines(__SOURCE_DIRECTORY__ + """\trainingsample.csv""")

(******* 2. CLEANING UP HEADERS *******)
 
// Did you notice that the file has a header? We want to get rid of it.

let dataNoHeader = dataLines.[1..]

(******* 3. EXTRACTING COLUMNS *******)
 
// Break each line of the file into an array of string,
// separating by commas

let dataValues = dataNoHeader |> Array.map (fun line -> line.Split(','))
 
(******* 4. CONVERTING FROM STRINGS TO INTS *******)
 
// Now that we have an array containing arrays of strings,
// and the headers are gone, we need to transform it 
// into an array of arrays of integers.
// You might need an Array.map inside an Array.map for this one... :-S

let dataNumbers = dataValues |> Array.map (Array.map (int)) 

(******* 5. CONVERTING ARRAYS TO RECORDS *******)
 
// Rather than dealing with a raw array of ints,
// for convenience let's store these as an array of Records

type DigitRecord = { Label:int; Pixels:int[] }
let dataRecords = dataNumbers |> Array.map (fun record -> {Label = record.[0]; Pixels = record.[1..]}); 

(******* 6. LET'S SEE SOME DIGITS! *******)
 
// Now we have things structured sensibly, if you want, you can have a look at some digits.
// There's a Visualiser module, which you hopefully opened earlier, which has a draw function
// that can be called like so:
// draw "title" digit.Pixels
// Note: just draw one at a time, unless you want to spend the next 10 minutes closing 1000 windows!

dataRecords.[..2] |> Array.iter (fun digit -> draw (digit.Label.ToString()) digit.Pixels)

(******* 7. TRAINING vs VALIDATION DATA *******)

// How will we see if our algorithm works?  We need to take our known character data and split
// it into 'training data' and the 'validation set'.
// Let's keep say 900 records for training and 100 for validation.
// Array splitting should come in handy again

let trainingData = dataRecords.[..1599]
let validationData = dataRecords.[1600..]

(******* 8. COMPUTING DISTANCES *******)
 
// We need to compute the distance between images, and maybe put it in a function like
// distance (digit1:int[]) (digit2:int[]) = 42
// How do we implement this?  Up to you.  Add up all the pixels, compare each pixel, use euclidian distance..
// Do something simple for now, you can come back to this later.
 
let distance (testDigit:int[]) (knownDigit:int[]) = 

// Difference between all pixels added together
    abs ((testDigit |> Array.sum) - (knownDigit |> Array.sum))

(******* 9. WRITING THE CLASSIFIER FUNCTION *******)
 
// We are now ready to write a classifier function!
// The classifier should take a set of pixels (an array of ints) as an input, search for the
// closest example in our sample, and use that as the predicted classification of the unknown
// image.
// Your function will look something like this:
// let classify (unknown:int[]) = 1
// This is where the 'k' of KNN comes in - k defines how many of the closest training data
// records we use to predict the unknown digit.  For now, let's just use the closest example,
// to keep things simple (so k=1).

let classify (unknown:int[]) =
    
// 1 nearest
    let nearestNeighbour = 
        trainingData
        |> Array.minBy (fun trainingDigit -> distance trainingDigit.Pixels unknown)
    
    nearestNeighbour.Label
 
(******* 10. SEE THE CLASSIFIER IN ACTION *******)
 
// Now that we have a classifier, let's see it in action.
// For each example in the validation set, we can use the classifier to predict
// the digit.  Let's take, say, the first 20 classifications and see if it seems to be working
// by writing the actual and preicted values to the console.

validationData.[..20]
|> Array.iter (fun digit -> printfn "Actual: %d, Predicted: %d" digit.Label (classify digit.Pixels))

(******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******)
 
// Let's judge with a little more accuracy how good our classifier is. 
// Let's classify all of the validation records, and work out the % correctly predicted.
 
validationData
|> Array.averageBy (fun digit -> if classify digit.Pixels = digit.Label then 1.0 else 0.0)
|> (fun result -> printfn "Correct: %f%%" (result * 100.0))