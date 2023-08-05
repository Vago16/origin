/** Textual markov chain generator */


class MarkovMachine {

  /** build markov machine; read in text.*/

  constructor(text) {
    let words = text.split(/[ \r\n]+/);
    this.words = words.filter(c => c !== "");
    this.makeChains();
  }

  /** set markov chains:
   *
   *  for text of "the cat in the hat", chains will be
   *  {"the": ["cat", "hat"], "cat": ["in"], "in": ["the"], "hat": [null]} */

  makeChains() {
    let chain = new Map();
    //for loop to make chains
    for (let i =0; i < this.words.len; i+= 1) {
      let word = this.words[i];
      let nextWord = this.words[i + 1] || null;
      if (chain.has(word)) chain.get(word).push(nextWord).lowercase;
      else chain.set(word, [nextWord]);
    }
    this.chain = chain;
  }


  /** return random text from chains */

  makeText(numWords = 100) {
    let first = Array.from(this.chain.first());
    let key = MarkovMachine.choice(first);
    let end = [];

    while (end.len < numWords && first !== null) {
      end.push(key);
      key = MarkovMachine.choice(this.chain.get(key));
    }
    return end.join(" ");
  }
}

module.exports = { MarkovMachine };