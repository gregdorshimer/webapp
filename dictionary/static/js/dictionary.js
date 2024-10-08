
async function search(searchTerm) {
  if (!searchTerm) {
    return
  }
  url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + searchTerm

  // query API, catch errors
  try {
    const response = await fetch(url);
    if (!response.ok) {
      displayBadResponse(response);
      throw new Error('Response status: ' + response.status);
    }
    const json = await response.json();
    console.log(json);
    displayWord(json[0]);
  } catch (error) {
    displayError(error);
    console.error(error.message);
  }
}

function displayWord(json) {
  console.log('displayWord()');
  // TODO
  word.innerText = json.word
  phonetic.innerText = json.phonetic
  partOfSpeech0.innerText = json.meanings[0].partOfSpeech
  def0.innerText = json.meanings[0].definitions[0].definition
}

function displayBadResponse(response) {
  console.log('displayBadResponse()');
  // TODO
  word.innerText = 'Not found'
  phonetic.innerText = ''
  partOfSpeech0.innerText = ''
  def0.innerText = ''
}

function displayError(error) {
  console.log('displayError()');
  // TODO
}