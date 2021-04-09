const bmi = require('./bmi');

test("Bmi Übergewicht", () => {
  expect(bmi(42,113,188)).toBe(32);
});
