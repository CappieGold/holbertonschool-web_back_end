const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const base = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(base, (err, res) => {
      try {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        done();
      } catch (e) { done(e); }
    });
  });

  it('Correct result?', (done) => {
    request.get(base, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(body).to.equal('Welcome to the payment system');
        done();
      } catch (e) { done(e); }
    });
  });
});

describe('Cart page', () => {
  const base = 'http://localhost:7865';

  it('200 for numeric id', (done) => {
    request.get(`${base}/cart/12`, (err, res) => {
      try {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        done();
      } catch (e) { done(e); }
    });
  });

  it('Body for numeric id', (done) => {
    request.get(`${base}/cart/12`, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      } catch (e) { done(e); }
    });
  });

  it('404 for non-numeric id', (done) => {
    request.get(`${base}/cart/hello`, (err, res) => {
      try {
        expect(res.statusCode).to.equal(404);
        done();
      } catch (e) { done(e); }
    });
  });
});

describe('GET /available_payments', () => {
  const url = 'http://localhost:7865/available_payments';

  it('returns 200 and expected JSON (deep equal)', (done) => {
    request.get({ url, json: true }, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        expect(body).to.deep.equal({
          payment_methods: { credit_cards: true, paypal: false },
        });
        done();
      } catch (e) { done(e); }
    });
  });
});

describe('POST /login', () => {
  const url = 'http://localhost:7865/login';

  it('returns Welcome <userName>', (done) => {
    request.post({ url, json: { userName: 'Betty' } }, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      } catch (e) { done(e); }
    });
  });
});
