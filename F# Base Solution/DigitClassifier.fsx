#load "Visualiser.fs"

open System
open System.IO
open Visualiser

// Follow the steps below to implement your digit classifier.
// If you need a bit of help, check out the hints.
// If you need even more, have a peek at the example solutions.  (But don't let anyone see you!)

// The first few steps have been implemented for you, so you can get onto the interesting part!

(******* 0. GETTING TO KNOW YOUR DATA *******)
 
// First let's have a look at "trainingsample.csv".  Understand the format, 
// so you know what you're working with.
// Each line has the digit (0-9), then 784 numbers representing pixels, with
// greyscale values from 0-255

(******* 1. READING THE DATA *******)
 
// First let's read the contents of "trainingsample.csv" into an array, one line per element

// 1. F# Reminder
// Highlight lines and Alt+Enter to run them in FSI

let dataLines = File.ReadAllLines(__SOURCE_DIRECTORY__ + """\trainingsample.csv""")

(******* 2. CLEANING UP HEADERS *******)
 
// Did you notice that the file has a header? We want to get rid of it.

// 2. F# Reminder
// You access an array element using myArray.[0]
// You can get slices of arrays like myArray.[10..20], myArray.[10..] or myArray.[..20]

let dataNoHeader = dataLines.[1..]

(******* 3. EXTRACTING COLUMNS *******)
 
// Break each line of the file into an array of string,
// separating by commas

// 3. F# Reminder
// |> pipes something into a function, e.g. [1;2;3] |> List.rev
// Array.map applies a function to each element of an array, e.g. Array.map (fun s -> s.Length)

let dataValues = dataNoHeader |> Array.map (fun line -> line.Split(','))
 
(******* 4. CONVERTING FROM STRINGS TO INTS *******)
 
// Now that we have an array containing arrays of strings,and the headers are gone, 
// we need to transform it into an array of arrays of integers.

// 4. F# Reminder
// Array.map (int) is the same as Array.map (fun item -> (int)item)

let dataNumbers = dataValues |> Array.map (Array.map (int)) 
 
(******* 5. CONVERTING ARRAYS TO RECORDS *******)
 
// Rather than dealing with a raw array of ints,
// for convenience let's store these as an array of Records

// 5. F# Reminder
// You declare a record like this
// type Example = { Name:string; Age:int }
// and instantiate one like this (no need to mention the type explicitly):
// let example = { Name = "Tim"; Age = 10 } 

// 5. [ YOUR CODE GOES HERE! ]

// 5. Hints
// --------------------------------------------------------------------------------------------------------------------------------------------> A type like this may be useful: { Label:int; Pixels:int[] }

(******* 6. LET'S SEE SOME DIGITS! *******)
 
// Now we have things structured sensibly, if you want, you can have a look at some digits.
// There's a Visualiser module, which you hopefully opened earlier, which has a draw function
// that can be called like so:
// draw "title" digit.Pixels
// Note: just draw one at a time, unless you want to spend the next 10 minutes closing 1000 windows!

// 6. Hints
// --------------------------------------------------------------------------------------------------------------------------------------------> draw (dataRecords.[0].Label.ToString()) dataRecords.[0].Pixels

(******* 7. TRAINING vs VALIDATION DATA *******)

// How will we see if our algorithm works?  We need to take our known character data and split
// it into 'training data' and the 'validation set'.
// Let's keep say 1600 records for training and 400 for validation.
// Array splitting should come in handy again

// 7. [ YOUR CODE GOES HERE! ]

(******* 8. COMPUTING DISTANCES *******)
 
// We need to compute the distance between images, and maybe put it in a function like
// distance (digit1:int[]) (digit2:int[]) = 42
// How do we implement this?  Up to you.  Add up all the pixels, compare each pixel, use euclidian distance..
// Do something simple for now, you can come back to this later.
 
// 8. F# Reminder
// Array.sum does what it says on the tin
// Array.map2 is like Array.map, but you can operate on two arrays at a time
// e.g Array.map2 (fun element1 element2 -> element1 + element2) array1 array2
// Use the abs function to get an absolute value

// 8. [ YOUR CODE GOES HERE! ]

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

// 9. F# Reminder
// Array.minBy can be used to find the lowest item in an array, based on the passed function
// You can access the training data from your classify function (a closure)
 
// 9. [ YOUR CODE GOES HERE! ]
 
(******* 10. SEE THE CLASSIFIER IN ACTION *******)
 
// Now that we have a classifier, let's see it in action.
// For each example in the validation set, we can use the classifier to predict
// the digit.  Let's take, say, the first 20 classifications and see if it seems to be working
// by writing the actual and preicted values to the console.

// 10. F# Reminder
// printfn writes output, e.g.
// printfn "A string: %s A number: %d" "hi" 5

// 10. [ YOUR CODE GOES HERE! ]

(******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******)
 
// Let's judge with a little more accuracy how good our classifier is. 
// Let's classify all of the validation records, and work out the % correctly predicted.
 
// 11. [ YOUR CODE GOES HERE! ]

// 11. Hints
// --------------------------------------------------------------------------------------------------------------------------------------------> A quick way to find a percentage: Array.averageBy, returning 1 for correct and 0 for incorrect classification (then * by 100)

// CONGRATULATIONS!  Hopefully, you have a working digit classifier.
// Want to make it better?  See some suggestions below..

(******* 12. Next Steps ********)
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