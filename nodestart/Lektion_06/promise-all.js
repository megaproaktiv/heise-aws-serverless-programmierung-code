// Asynchron Promises einsammeln
const promise1 = Promise.resolve("EC2 Istanzen");
const promise2 = new Promise((resolve, reject) => {
    setTimeout(resolve, 2000, 'S3 Buckets');
  });
  ;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 1000, 'StepFunctions');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
  console.log(values);
});

