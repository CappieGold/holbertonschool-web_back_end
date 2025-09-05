const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('résout avec l’objet attendu quand success=true (utilise done)', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        try {
          expect(res).to.deep.equal({ data: 'Successful response from the API' });
          done();
        } catch (err) {
          done(err);
        }
      })
      .catch(done);
  });
});
