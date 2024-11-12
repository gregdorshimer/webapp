// TODO refactor to use jQuery

var puzzle = ''
var solution = ''

const testPuzzle = "000000300010003780040100260400308020000204610002590400564000900001000000387002000";

// pulls answers from the board and returns as a string with zeros for unfilled spaces
function getAnswers() {
  answers = ''

  for (let i = 0; i < 81; i++) {
    let id = "c" + i.toString();
    if (document.getElementById(id).getAttribute("value")) {
      answers += document.getElementById(id).getAttribute("value");
    } else if (id.innerText) {
      answers += document.getElementById(id).innerText;
    } else {
      answers += "0";
    }
  }

  return answers;
}

// sends the answers that are filled to the django web endpoint to check for correctness, and changes display according
// to response
async function submit() {
  var answers = getAnswers();

  // TODO send http post to django api endpoint
  // TODO return response (either bool or [] or [rows/columns that are wrong])
  var response = "";
  if (response.correct) {
    alertCorrect();
  } else {
    alertIncorrect(response.rows, response.columns);
  }
}

function alertCorrect() {
  $(".cell").removeClass("cell-normal");
  $(".cell").removeClass("cell-incorrect");
  $(".cell").addClass("cell-correct");

  // TODO uncomment when ready
  // alert("Puzzle completed!");

  easyBtn.disabled = false;
  mediumBtn.disabled = false;
  hardBtn.disabled = false;
}

function alertIncorrect(rows, columns) {
  for (row in rows) {
    $("." + rows[row]).removeClass("cell-normal");
    $("." + rows[row]).removeClass("cell-correct");
    $("." + rows[row]).addClass("cell-incorrect");
  }
  for (column in columns) {
    $("." + columns[column]).removeClass("cell-normal");
    $("." + columns[column]).removeClass("cell-correct");
    $("." + columns[column]).addClass("cell-incorrect");
  }

  // TODO uncomment when ready
  // alert("Check these spaces!");
}

function displayPuzzle(puzzle) {
  for (let i = 0; i < 81; i++) {
    let id = "c" + i;
    let element = document.getElementById(id);
    if (puzzle[i] != 0) {
      element.setAttribute("class", "cell-text f");
      element.setAttribute("readonly", true);
      element.setAttribute("value", "" + puzzle[i]);
      element.removeAttribute("maxlength");
      element.innerText = "";
    }
    else {
      element.setAttribute("class", "cell-text e");
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


  // TODO: enable below once implemented
  // puzzle = /* await? */ getPuzzle(button);
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