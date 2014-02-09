#load "visualiser.fs"

open System
open System.IO
open Visualiser
open Checked

let horizontalBlur windowSize (image:int[]) =
    image
    |> Array.map float
    |> Seq.ofArray
    |> Seq.windowed windowSize
    |> Seq.map Array.average
    |> Seq.map int
    |> Array.ofSeq

(******* 1. GETTING SOME DATA *******)
let dataLines = File.ReadAllLines(__SOURCE_DIRECTORY__ + """\trainingsample.csv""")

(******* 3. CLEANING UP HEADERS *******)
let dataNoHeader = dataLines.[1..]

(******* 2. EXTRACTING COLUMNS *******)
let dataValues = dataNoHeader |> Array.map (fun line -> line.Split(','))
 
(******* 4. CONVERTING FROM STRINGS TO INTS *******)
let dataNumbers = dataValues |> Array.map (Array.map (int)) 

(******* 5. CONVERTING ARRAYS TO RECORDS *******)
type DigitRecord = { Label:int; Pixels:int[] }
let dataRecords = 
    dataNumbers 
    |> Array.map (fun record -> {Label = record.[0]; Pixels = record.[1..]})
    |> Array.map (fun record -> {record with Pixels =record.Pixels |> horizontalBlur 4})

(******* 6. LET'S SEE SOME DIGITS! *******)
//dataRecords.[..3] |> Array.iter (fun digit -> draw (digit.Label.ToString()) digit.Pixels)

(******* 7. TRAINING vs VALIDATION DATA *******)
let trainingData = dataRecords.[..1599]
let validationData = dataRecords.[1600..]

(******* 8. COMPUTING DISTANCES *******)
let distance (testDigit:int[]) (knownDigit:int[]) = 
    Array.map2 (fun x y -> int64 ((x-y) * (x-y))) testDigit knownDigit
    |> Array.sum
    |> int

(******* 9. WRITING THE CLASSIFIER FUNCTION *******)

// use the nearest example
let classify (unknown:int[]) =
    let nearestNeighbour = 
        trainingData
        |> Array.minBy (fun trainingDigit -> distance trainingDigit.Pixels unknown)
    
    nearestNeighbour.Label

// take a vote from the k nearest examples
let classify_nearest k (unknown:int[]) =
    trainingData
    |> Array.sortBy (fun trainingDigit -> distance trainingDigit.Pixels unknown)
    |> Seq.take k
    |> Seq.groupBy (fun digit -> digit.Label )
    |> Seq.maxBy (fun (label, digits) -> digits |> Seq.length)
    |> fst

// take all training data into account, but weight score by distance
let classify_weighted (unknown:int[]) =
    trainingData
    |> Seq.groupBy (fun digit -> digit.Label )
    |> Seq.map (fun (label, group) -> label, group |> Seq.sumBy (fun digit -> 
        let dist = 1.0 / float (distance digit.Pixels unknown)
        dist**16.0)) // best from 16 - presumably this is the same as k=1
    |> Seq.maxBy snd
    |> fst

(******* 10. SEE THE CLASSIFIER IN ACTION *******)
//validationData.[..20]
//|> Array.iter (fun digit -> printfn "Actual: %d, Predicted: %d" digit.Label (classify digit.Pixels))

(******* 11. EVALUATING THE MODEL AGAINST VALIDATION DATA *******)
validationData
|> Array.averageBy (fun digit -> if classify_weighted digit.Pixels = digit.Label then 1.0 else 0.0)
|> (fun result -> printfn "Correct: %f%%" (result * 100.0))
