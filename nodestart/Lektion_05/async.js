// async/await Grundprinzip

function awsCall(){
  return new Promise( resolve => {
    setTimeout(() => {
      resolve('resolved');
    }, 2000);
  });
}

async function lambda() {
  console.log('calling');
  const result = awsCall(function(message) {
    console.log(message);
  });
  console.log('called');
  console.log(result);
}

lambda();

