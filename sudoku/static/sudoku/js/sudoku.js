// TODO on-type into the calls, reset CSS to remove red highlighting for wrong columns and rows

async function getPuzzle(difficulty) {
  try {
    const response = await fetch('game/?difficulty=' + difficulty);
    if (!response.ok) {
      throw new Error('Response status: ' + response.status);
    } else {
      const json = await response.json();
      return json;
    }
  } catch (error) {
    console.error(error.message);
  }
}

function getStartingGame() {  answers = '';
  answers = '';

  $(".cell-text").each(function() {
    if ($(this).attr("value")) {
      answers += $(this).attr("value");
    } else {
      answers += "0";
    }
  });

  return answers;
}


// pulls answers from the board and returns as a string with zeros for unfilled spaces
function getAnswers() {
  answers = '';

  $(".cell-text").each(function() {
    if ($(this).attr("value")) {
      answers += $(this).attr("value");
    } else if ($(this).val()) {
      answers += $(this).val();
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

  try {
    const response = await fetch('game/', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        answers: answers,
      }),
    });
    if (!response.ok) {
      throw new Error('Response status: ' + response.status);
    } else {
      const json = await response.json();
      console.log(json);
      if (json['correct']) {
        alertCorrect();
      } else {
        alertIncorrect(json.rows, json.columns);
      }
    }
  } catch (error) {
    console.error(error.message);
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
    $(".r" + rows[row]).removeClass("cell-normal");
    $(".r" + rows[row]).removeClass("cell-correct");
    $(".r" + rows[row]).addClass("cell-incorrect");
  }
  for (column in columns) {
    console.log('row:' + rows[row]);
    $(".c" + columns[column]).removeClass("cell-normal");
    $(".c" + columns[column]).removeClass("cell-correct");
    $(".c" + columns[column]).addClass("cell-incorrect");
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

async function buttonClick(button) {
  const puzzle = await getPuzzle(button);

  displayPuzzle(puzzle.puzzle);

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