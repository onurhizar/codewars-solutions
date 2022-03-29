// Sentence Smash @ https://www.codewars.com/kata/53dc23c68a0c93699800041d
public class SmashWords {
  public static String smash(String... words) {
    return String.join(" ", words);
  }
}


// Sum Arrays @ https://www.codewars.com/kata/53dc54212259ed3d4f00071c
public class SumArray {
  public static double sum(double[] numbers) {
    double sum = 0.0;
    for (double number : numbers){
      sum += number;
    }
    return sum;
  }
}
