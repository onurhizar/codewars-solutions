// Stop gninnipS My sdroW! @ 
public class SpinWords {
  public String spinWords(String sentence) {
    String[] words = sentence.split(" ");
  
    for (int i=0; i<words.length; i++){
        String word = words[i];
        if (word.length() < 5) continue;

        String tempWord = "";
        for (int j=word.length()-1; j >= 0 ; j--){
            tempWord += word.charAt(j);
        }
        words[i] = tempWord;
    }

    return String.join(" ", words);
  }
}
