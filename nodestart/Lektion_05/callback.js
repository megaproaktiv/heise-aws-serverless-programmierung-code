// Callback Grundprinzip
function awsCall(callback) {
    setTimeout(() => {
        callback("Fertig!");
      }, 2000);
}

console.log("calling");

awsCall(function(message) {
    console.log(message);
});
console.log("called");