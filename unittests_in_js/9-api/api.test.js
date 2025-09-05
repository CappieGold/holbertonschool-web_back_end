const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const base = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(`${base}`, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        done();
      } catch (e) { done(e); }
    });
  });

  it('Correct result?', (done) => {
    request.get(`${base}`, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(body).to.equal('Welcome to the payment system');
        done();
      } catch (e) { done(e); }
    });
  });

  it('Content-Type is text/html', (done) => {
    request.get(`${base}`, (err, res) => {
      try {
        expect(err).to.equal(null);
        expect(res.headers['content-type']).to.match(/^text\/html/);
        done();
      } catch (e) { done(e); }
    });
  });
});

describe('Cart page', () => {
  const base = 'http://localhost:7865';

  it('Correct status code when :id is a number', (done) => {
    request.get(`${base}/cart/12`, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        done();
      } catch (e) { done(e); }
    });
  });

  it('Correct body for a numeric :id', (done) => {
    request.get(`${base}/cart/12`, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      } catch (e) { done(e); }
    });
  });

  it('404 when :id is NOT a number', (done) => {
    request.get(`${base}/cart/hello`, (err, res, body) => {
      try {
        expect(res.statusCode).to.equal(404);
        done();
      } catch (e) { done(e); }
    });
  });

  it('404 for mixed value 12a', (done) => {
    request.get(`${base}/cart/12a`, (err, res) => {
      try {
        expect(res.statusCode).to.equal(404);
        done();
      } catch (e) { done(e); }
    });
  });

  it('404 for decimal 1.2', (done) => {
    request.get(`${base}/cart/1.2`, (err, res) => {
      try {
        expect(res.statusCode).to.equal(404);
        done();
      } catch (e) { done(e); }
    });
  });
});
