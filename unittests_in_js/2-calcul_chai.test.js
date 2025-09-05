const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber(type, a, b) — Chai expect', () => {
  describe('SUM', () => {
    it('additionne deux entiers', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });

    it('arrondit et additionne (1.4 + 4.5 -> 1 + 5)', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('arrondit .5 vers le haut des deux côtés', () => {
      expect(calculateNumber('SUM', 2.5, 2.5)).to.equal(6); // 3 + 3
    });

    it('négatifs et arrondis', () => {
      expect(calculateNumber('SUM', -1.2, 3.7)).to.equal(3); // -1 + 4
    });
  });

  describe('SUBTRACT', () => {
    it('soustrait deux entiers', () => {
      expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    });

    it('arrondit puis soustrait (1.4 - 4.5 -> 1 - 5)', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('arrondi autour de .5', () => {
      expect(calculateNumber('SUBTRACT', 10, 2.49)).to.equal(8); // 10 - 2
      expect(calculateNumber('SUBTRACT', 10, 2.5)).to.equal(7);  // 10 - 3
    });

    it('négatifs', () => {
      expect(calculateNumber('SUBTRACT', -1.5, -3.5)).to.equal(2); // -1 - (-3)
    });
  });

  describe('DIVIDE', () => {
    it('arrondit puis divise (1.4 / 4.5 -> 1 / 5)', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('division par zéro après arrondi -> "Error"', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');   // 0
      expect(calculateNumber('DIVIDE', 2.4, 0.2)).to.equal('Error'); // 0.2 -> 0
    });

    it('b = 0.5 arrondi à 1 (pas "Error")', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0.5)).to.equal(1); // 1 / 1
    });

    it('signes', () => {
      expect(calculateNumber('DIVIDE', -1.4, 4.5)).to.equal(-0.2); // -1 / 5
      expect(calculateNumber('DIVIDE', -1.6, -0.6)).to.equal(2);   // -2 / -1
    });
  });

  describe('Erreurs', () => {
    it('type invalide -> throw', () => {
      expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw('Invalid type');
    });
  });
});
