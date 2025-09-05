const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi (hooks + single spy)', () => {
  let logSpy;

  beforeEach(() => {
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    logSpy.restore();
  });

  it('logs once "The total is: 120" for (100, 20)', () => {
    sendPaymentRequestToApi(100, 20);

    expect(logSpy.calledOnce).to.be.true;
    expect(logSpy.calledWithExactly('The total is: 120')).to.be.true;
  });

  it('logs once "The total is: 20" for (10, 10)', () => {
    sendPaymentRequestToApi(10, 10);

    expect(logSpy.calledOnce).to.be.true;
    expect(logSpy.calledWithExactly('The total is: 20')).to.be.true;
  });
});
