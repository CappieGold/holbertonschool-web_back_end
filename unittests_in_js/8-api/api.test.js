const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(url, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(res && res.statusCode).to.equal(200);
        done();
      } catch (e) { done(e); }
    });
  });

  it('Correct result?', (done) => {
    request.get(url, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(body).to.equal('Welcome to the payment system');
        done();
      } catch (e) { done(e); }
    });
  });

  it('Other? (Content-Type)', (done) => {
    request.get(url, (err, res, body) => {
      try {
        expect(err).to.equal(null);
        expect(res.headers['content-type']).to.match(/^text\/html/);
        done();
      } catch (e) { done(e); }
    });
  });
});
