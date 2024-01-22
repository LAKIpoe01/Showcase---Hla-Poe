
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Hangman {
    private String kirjain;
    private List<Character> arvatut;
    private int jäljellä;

    public Hangman(WordList wordList, int jäljellä) {
        List<String> wordListData = wordList.giveWords();
        Random random = new Random();
        int randomIndex = random.nextInt(wordListData.size());
        kirjain = wordListData.get(randomIndex);
        arvatut = new ArrayList<>();
        this.jäljellä = jäljellä;
    }

    public boolean guess(Character c) {
        Character lower = Character.toLowerCase(c);
        if (kirjain.contains(lower.toString())) {
            if (!arvatut.contains(lower)) {
            arvatut.add(c);
            }
            return true;
        }
        else if (arvatut.contains(Character.toLowerCase(c))) {
            return false;
        } else {
            jäljellä--;
            return false;
        }
    }

    public List<Character> guesses() {
        return arvatut;
    }

    public int guessesLeft() {
        return Math.max(0, jäljellä);
    }

    public String word() {
        return kirjain;
    }

    public boolean theEnd() {
        if (jäljellä == 0) {
            return true;
        }
        for (char c : kirjain.toCharArray()) {
            if (!arvatut.contains(c)) {
                return false;
            }
        }
        return true;
    }
}