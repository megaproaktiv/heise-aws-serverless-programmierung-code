const bmi=require('./bmi');

// Handler
exports.handler = async function(event, context) {

  age = event.age;
  weight= event.weight;
  height= event.height;
  return bmi(age, weight, height);
}
