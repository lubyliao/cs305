import java.io.*;

// The client code borrowed from Thomas Berry contains three sample
// strategies and code that tests decks using each strategy.

public class Deck_client {
	
	public static void main(String[] args) {
		
		// Testing code for each of the three strategies
		System.out.println("Dealing a hand of 5 cards using half:");
		Deck deck_half = new Deck(new Half());
		for(int i = 0; i < 5; i++) {
			System.out.println(deck_half.draw());
		}

		System.out.println("Dealing a hand of 5 cards using top:");
		Deck deck_top = new Deck(new Top());
		for(int i = 0; i < 5; i++) {
			System.out.println(deck_top.draw());
		}

		System.out.println("dealing a hand of 5 cards using bottom:");
		Deck deck_bottom = new Deck(new Bottom());
		for(int i = 0; i < 5; i++) {
			System.out.println(deck_bottom.draw());
		}
	}
}

// Three strategies to use with deck objects
class Half implements Strategy {
	public int function(int NumCardsInTheDeck) {
		return NumCardsInTheDeck/2;
	}
}

class Bottom implements Strategy {
	public int function(int NumCardsInTheDeck) {
		return 0;
	}
}

class Top implements Strategy {
	public int function(int NumCardsInTheDeck) {
		return NumCardsInTheDeck-1;
	}
}

