<?php
ini_set('memory_limit', '1024M'); 
require 'Visualizer.php';

// 1. READING THE DATA

$dataLines = file(__DIR__ . '/trainingsample.csv');

// 2. CLEANING UP HEADERS

$dataNoHeader = array_slice($dataLines, 1);

// 3. EXTRACTING COLUMNS

$dataValues = array_map(
    function ($dataLine) {
        return explode(',', $dataLine);
    },
    $dataNoHeader
);

// 4. CONVERTING FROM STRINGS TO INTS

$dataNumbers = array_map(
    function ($stringArray) {
        return array_map('intval', $stringArray);
    },
    $dataValues
);

// 5. CONVERTING ARRAYS TO RECORDS

class DigitalRecord
{
    public $Label;
    public $Pixels = [];

    public function __construct($Label, $Pixels)
    {
        $this->Label  = $Label;
        $this->Pixels = $Pixels;
    }
}

$dataRecords = array_map(
    function ($numberRow) {
        return new DigitalRecord(array_shift($numberRow), $numberRow);
    },
    $dataNumbers
);

// 6. LET'S SEE SOME DIGITS!

foreach (array_slice($dataRecords, 0, 3) as $record) {
    Visualiser::Draw($record->Label, $record->Pixels);
}

// 7. TRAINING vs VALIDATION DATA

$trainingData   = array_slice($dataRecords, 0, 1600);
$validationData = array_slice($dataRecords, 1600);

// 8. COMPUTING DISTANCES

function calculateDistance($testDigit, $knownDigit)
{
    $pixels   = count($testDigit);
    $distance = 0;
    for ($i = 0; $i < $pixels; $i++) {
        // $distance += abs($testDigit[$i] - $knownDigit[$i]); // Simple
        $distance += pow($testDigit[$i] - $knownDigit[$i], 2); // Euclidian
    }

    // return $distance; // Simple
    return sqrt($distance); // Euclidian
}

// 9. WRITING THE CLASSIFIER FUNCTION

function classify($trainingData, $unknownPixels)
{
    $neighbors = [];
    foreach ($trainingData as $i => $knownDigit) {
        $neighbors[$i] = calculateDistance($unknownPixels, $knownDigit->Pixels);
    }

    asort($neighbors);

    return $trainingData[key($neighbors)]->Label;
}

// 10. SEE THE CLASSIFIER IN ACTION

$predicted = classify($trainingData, $validationData[0]->Pixels);

// 11. EVALUATING THE MODEL AGAINST VALIDATION DATA

$processed = $matched = $accuracy = 0;
foreach ($validationData as $i => $record) {
    $processed++;

    $actual    = $record->Label;
    $predicted = classify($trainingData, $record->Pixels);

    if ($actual == $predicted) {
        $matched++;
    }

    $accuracy = round(($matched / $processed) * 100, 2);

    //Visualiser::Draw("$actual == $predicted ?" , $record->Pixels);
    echo "Actual: $actual, Predicted: $predicted, Accuracy: $accuracy %", PHP_EOL;
}