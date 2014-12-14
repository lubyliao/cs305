package Deck;

import java.util.*;

/**
 A strategy is a function wrapped in an interface.
We need to do this only because we cannot directly store a function as an attribute of a Java object.
But we can store a function wrapped in an interface.
*/

public interface Strategy {

    /** <code>function</code> represents a policy of getting a card from a deck.
	<code>Bound</code> is the number of cards in the deck.  <code>function(bound)</code>
	returns the index of the card to be drawn.  <code>Bound</code> corresponds
	to the deck top, and 0 the deck bottom.
    */
    int function(int bound);	
}

/**
 A <code>Deck</code> instance starts its existence with a deck of 52 cards.

The state of a <code>Deck</code> instance consists of three things:
<ol>
<li> the deck,
<li> the number of cards left, and 
<li> the strategy function (wrapped in an interface) using which to draw the next card.
</ol>
*/

public class Deck {
    Strategy function_wrapper;
    int num;
    List<Integer> cards;

    /** Creates a deck of 52 cards with the strategy specified in the function <code>wrapper</code> argument.
     */
    public Deck(Strategy wrapper) {
	this.function_wrapper = wrapper;
	this.num = 52;
	this.cards = new ArrayList<Integer>();
	for(int i = 0; i < num; i++) {
	    cards.add(i);
	}	
    }
	
    /** Draws and returns a card from the deck using the stored strategy. 
     */
    public int draw() {
	
	// removes the card according to the strategy
	int index = function_wrapper.function(num); // Here lies the essential difference between Python and Java
	// In Python, we simply say function(num)
	// In Java, we need to add an extra layer of indirection: function_wrapper.function(num)
	int card = cards.get(index);
	// updates the deck
	num--;
	for(int i = index; i < num; i++) {
	    cards.set(i, cards.get(i+1));
	}
	return card;
    }
}
