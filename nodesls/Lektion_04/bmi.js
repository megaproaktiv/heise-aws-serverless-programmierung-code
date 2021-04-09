function bmi(age, weight, height) {
  height_m = height/100;
  bmi = weight / (height_m * height_m);
  bmi = Math.round(bmi);
  return bmi;
}
module.exports = bmi;
