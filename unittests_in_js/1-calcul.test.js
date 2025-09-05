const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber(type, a, b)', () => {
  describe('SUM', () => {
    it('additionne deux entiers', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });
    it('arrondit et additionne (1.4 + 4.5 -> 1 + 5)', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('arrondit les deux (.5 monte)', () => {
      assert.strictEqual(calculateNumber('SUM', 2.5, 2.5), 6); // 3 + 3
    });
    it('négatifs et arrondis', () => {
      assert.strictEqual(calculateNumber('SUM', -1.2, 3.7), 3); // -1 + 4
    });
  });

  describe('SUBTRACT', () => {
    it('soustrait deux entiers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 5, 3), 2);
    });
    it('arrondit puis soustrait (1.4 - 4.5 -> 1 - 5)', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('arrondit autour de .5', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 10, 2.49), 8); // 10 - 2
      assert.strictEqual(calculateNumber('SUBTRACT', 10, 2.5), 7);  // 10 - 3
    });
    it('négatifs', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.5, -3.5), 2); // -1 - (-3)
    });
  });

  describe('DIVIDE', () => {
    it('arrondit puis divise (1.4 / 4.5 -> 1 / 5)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('division par zéro après arrondi -> "Error"', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');   // 0 -> 0
      assert.strictEqual(calculateNumber('DIVIDE', 2.4, 0.2), 'Error'); // 0.2 -> 0
    });
    it('b = 0.5 arrondi à 1, donc pas "Error"', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.5), 1); // 1 / 1
    });
    it('signes (résultat négatif/positif)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', -1.4, 4.5), -0.2); // -1 / 5
      assert.strictEqual(calculateNumber('DIVIDE', -1.6, -0.6), 2);   // -2 / -1
    });
  });
});
