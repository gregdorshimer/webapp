// TODO call getPuzzle() when btn is clicked

var puzzle = ''
var solution = ''

async function checkAnswers(id) {
  // TODO send http post to django api endpoint
  // TODO return response (either bool or [] or [rows/columns that are wrong])

  answers = ''

  for (let i = 0; i < 81; i++) {
    let id = "c" + i.toString();
    if (id.getAttribute("value")) {
      answers += id.getAttribute("value");
    } else if (id.innerText) {
      answers += id.innerText;
    } else {
      answers += "0";
    }
  }

  // TODO

}


function readAnswers() {
  // TODO read answers from the board and return as a string
}



function displayPuzzle(puzzle) {
  for (let i = 0; i < 81; i++) {
    let id = "c" + i;
    let element = document.getElementById(id);
    if (puzzle[i] != 0) {
      element.setAttribute("class", "f");
      element.setAttribute("readonly", true);
      element.setAttribute("value", "" + puzzle[i]);
      element.removeAttribute("maxlength");
      element.innerText = "";
    }
    else {
      element.setAttribute("class", "e");
      element.removeAttribute("readonly");
      element.setAttribute("value", "");
      element.removeAttribute("value");
      element.setAttribute("maxlength", "1");
      element.innerText = "";
    }
  }
}


  /*
  url = "https://youdosudoku.com/api/"

  // query API, catch errors
  try {
    const response = await fetch(url, {
      method: "POST",
      mode: 'no-cors',
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        difficulty: "easy",
        solution: true,
        array: false
      })});
    if (!response.ok) {
      console.error("response not ok: " + response.status);
    }
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.error(error);
  } */



function buttonClick(button) {
  console.log('buttonClick(' + button + ')');


  // puzzle = /* await? */ getPuzzle(button);
  var testPuzzle = "000000300010003780040100260400308020000204610002590400564000900001000000387002000";
  displayPuzzle(testPuzzle);

  // set correct Btn to disabled, enable other buttons
  switch(button) {
  case "easy":
    easyBtn.disabled = true;
    mediumBtn.disabled = false;
    hardBtn.disabled = false;
    break;
  case "medium":
    easyBtn.disabled = false;
    mediumBtn.disabled = true;
    hardBtn.disabled = false;
    break;
  case "hard":
    easyBtn.disabled = false;
    mediumBtn.disabled = false;
    hardBtn.disabled = true;
  }
}