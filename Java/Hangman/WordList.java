
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class WordList {
    private List<String> words;

    public WordList(String filename) {
        words = new ArrayList<>();
        loadWordsFromFile(filename);
    }

    private void loadWordsFromFile(String filename) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String word = line.toLowerCase();
                words.add(word);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<String> giveWords() {
        return words;
    }

    public WordList theWordsOfLength(int length) {
        WordList wordList = new WordList("");
        for (String word : words) {
            if (word.length() == length) {
                wordList.words.add(word);
            }
        }
        return wordList;
    }

    public WordList theWordsWithCharacters(String someString) {
        WordList wordList = new WordList("");
        for (String word : words) {
            if (word.length() == someString.length()) {
                boolean matches = true;
                for (int i = 0; i < word.length(); i++) {
                    char c = someString.charAt(i);
                    if (c != '_' && c != word.charAt(i)) {
                        matches = false;
                        break;
                    }
                }
                if (matches) {
                    wordList.words.add(word);
                }
            }
        }
        return wordList;
    }
}