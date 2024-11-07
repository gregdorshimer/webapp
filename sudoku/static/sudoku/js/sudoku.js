// TODO call getPuzzle() when page is loaded
// TODO hook up buttons to buttonClick(button)
// TODO change IDs of HTML elements

async function getPuzzle() {
  url = "https://youdosudoku.com/api/"

  // query API, catch errors
  try {
    const response = await fetch(url);
    if (!response.ok) {
      displayBadResponse(response);
      throw new Error('Response status: ' + response.status);
    }
    const json = await response.json();
    console.log(json);
    displayWord(json);
  } catch (error) {
    displayError(error);
    console.error(error.message);
  }
}

function displayWord(json) {
  console.log('displayWord()');
  // TODO
  /*
  word.innerText = json.word
  phonetic.innerText = json.phonetic
  partOfSpeech0.innerText = json.meanings[0].partOfSpeech
  def0.innerText = json.meanings[0].definitions[0].definition
  */
}

function displayBadResponse(response) {
  console.log('displayBadResponse()');
  // TODO
}

function displayError(error) {
  console.log('displayError()');
  // TODO
}

function buttonClick(button) {
  // TODO set given button to disabled
  // TODO set other buttons to not disabled
  // TODO call getPuzzle()
}