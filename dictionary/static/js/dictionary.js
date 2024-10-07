

function search(searchTerm) {
  alert("Hello from a static file! Value: " + searchTerm);

  url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + searchTerm

  alert('url: ' + url);
  // query API
  // catch errors

  // fetch: make API call
  // Note: network error when this block is used inside a function.
  // works when listed outside the function
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error("Network response was not ok")
      }
      return response.json();
    })
    .then(data => {
      console.log('Data: ', data);
    })
    .catch(error => {
      console.error('My super error: ', error.message);
    });

  //

}


/**


  // trigger async function
  // log response or catch error of fetch promise
  fetchAsync(url)
    .then(
    function(response) {
        if (response.status !== 200) {
            console.log('Error:' + response.status)
        }

        response.json().then(function(data) {
          console.log(data);
        });
    }
    )
    .catch(function(err) {
      console.log('My fetch error:' + err);
    })

  // display not found, or data

}

// https://gist.github.com/msmfsd/fca50ab095b795eb39739e8c4357a808
// async function
async function fetchAsync (url) {
  // await response of fetch call
  let response = await fetch(url);
  console.log(url)
  // only proceed once promise is resolved
  let data = await response.json();
  // only proceed once second promise is resolved
  return data;
}

// trigger async function
// log response or catch error of fetch promise

*/
