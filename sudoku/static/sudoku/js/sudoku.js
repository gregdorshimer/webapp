const testPuzzle = "000000300010003780040100260400308020000204610002590400564000900001000000387002000";

// pulls answers from the board and returns as a string with zeros for unfilled spaces
function getAnswers() {
  answers = '';

  $(".cell-text").each(function() {
    if ($(this).attr("value")) {
      answers += $(this).attr("value");
    } else if ($(this).text()) {
      answers += $(this).text();
    } else {
      answers += "0";
    }
  });

  return answers;
}

// sends the answers that are filled to the django web endpoint to check for correctness, and changes display according
// to response
async function submit() {
  var answers = getAnswers();

  // TODO send http post to django api endpoint
  // TODO return response (either bool or [] or [rows/columns that are wrong])
  var response = "";
  alertCorrect();
  /*
  if (response.correct) {
    alertCorrect();
  } else {
    alertIncorrect(response.rows, response.columns);
  } */
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
  $(".cell").removeClass("cell-correct");
  $(".cell").removeClass("cell-incorrect");
  $(".cell").addClass("cell-normal");

  for (let i = 0; i < 81; i++) {
    let id = "c" + i;
    let element = $("#" + id);
    if (puzzle[i] != 0) {
      element.removeClass("e");
      element.addClass("f");
      element.attr("readonly", "");
      element.attr("value", puzzle[i]);
      element.removeAttr("maxlength");
      element.text("");
    }
    else {
      element.removeClass("f");
      element.addClass("e");
      element.removeAttr("readonly");
      element.removeAttr("value");
      element.attr("maxlength", "1");
      element.text("");
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