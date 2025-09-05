const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('additionne deux entiers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('arrondit b quand b >= .5', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5); // 1 + 4
  });

  it('arrondit a quand a < .5 (vers le bas)', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5); // 1 + 4
  });

  it('arrondit a à .5 (vers le haut)', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6); // 2 + 4
  });

  it('arrondit b juste en dessous de .5', () => {
    assert.strictEqual(calculateNumber(10, 2.49), 12); // 10 + 2
  });

  it('arrondit b exactement à .5', () => {
    assert.strictEqual(calculateNumber(10, 2.5), 13); // 10 + 3
  });

  it('arrondit les deux quand les deux ont des décimales', () => {
    assert.strictEqual(calculateNumber(2.5, 2.5), 6); // 3 + 3
  });

  it('gère zéro et décimales', () => {
    assert.strictEqual(calculateNumber(0, 0.5), 1);
  });

  it('gère de grands nombres', () => {
    assert.strictEqual(calculateNumber(1000.4, 999.6), 2000); // 1000 + 1000
  });

  it('gère des négatifs (arrondi JS: -1.5 -> -1)', () => {
    assert.strictEqual(calculateNumber(-1.5, -3.5), -4); // -1 + -3
  });

  it('mélange négatif et positif', () => {
    assert.strictEqual(calculateNumber(-1.2, 3.7), 3); // -1 + 4
  });

  it('cas limite autour de .4999 et .5000', () => {
    assert.strictEqual(calculateNumber(1.499999999999, 0), 1);
    assert.strictEqual(calculateNumber(1.500000000001, 0), 2);
  });
});
