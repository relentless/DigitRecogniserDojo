case class Picture(pixels: List[Int]) {

  def distance(other: Picture): Long = {
    def square(n: Int) = n * n
    pixels.zip(other.pixels).map { case (p1, p2) => square(p1 - p2) }.sum
  }

}

case class LabelledExample(label: String, picture: Picture)

case class Classifier(trainingExamples: List[LabelledExample], k: Int) {

  def classify(picture: Picture): String = {
    val kClosest = findClosestExamples(picture)
    majorityVote(kClosest)
  }

  private def findClosestExamples(picture: Picture): List[LabelledExample] = {
    case class DistanceAndExample(distance: Long, example: LabelledExample)
    def decorate(example: LabelledExample) =
      DistanceAndExample(example.picture.distance(picture), example)
    trainingExamples.map(decorate).sortBy(_.distance).map(_.example).take(k)
  }

  /**
   * Pick the most frequently voted label amongst the given examples.
   */
  private def majorityVote(examples: List[LabelledExample]): String = {
    val examplesGroupedByLabel = examples.groupBy(_.label).toList
    val (winningLabel, numberOfVotes) =
      examplesGroupedByLabel.sortBy { case (label, examples) => examples.size }.last
    winningLabel
  }

}

object DataParser {

  import scala.io.Source

  def getExamplesFromFile(filename: String): List[LabelledExample] =
    Source.fromFile(filename).getLines.toList.tail.map(parseDataLine)

  private def parseDataLine(line: String): LabelledExample = {
    val label :: pixelStrings = line.split(",").toList
    val pixels = pixelStrings.map(_.toInt)
    LabelledExample(label, Picture(pixels))
  }

}

object KNearestNeighbourImageClassification extends App {

  val (trainingExamples, validationExamples) =
    DataParser.getExamplesFromFile("trainingsample.csv").splitAt(900)

  /**
   * @return fraction of the given examples correctly classified by the classifier.
   */
  def scoreClassifier(classifier: Classifier, examples: List[LabelledExample]): Double = {
    def isCorrectlyClassified(example: LabelledExample) =
      classifier.classify(example.picture) == example.label
    examples.count(isCorrectlyClassified).toDouble / examples.size
  }

  for (k <- 1 to 10) {
    val classifier = Classifier(trainingExamples, k)
    val score = scoreClassifier(classifier, validationExamples)
    println("k = " + k + ", classifier accuracy on validation set = " + score + "%")
  }

}