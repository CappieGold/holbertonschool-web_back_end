function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Asynchronous operations could be placed here
    // For now, we will simply resolve the promise immediately
    resolve('This is a response from the API');
  });
}

export default getResponseFromAPI;
