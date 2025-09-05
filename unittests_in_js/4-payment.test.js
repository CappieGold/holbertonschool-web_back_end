const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi (with stub)', () => {
  let calcStub;
  let logSpy;

  beforeEach(() => {
    calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    calcStub.restore();
    logSpy.restore();
  });

  it('stub Utils.calculateNumber to return 10 and verify call args & log', () => {
    sendPaymentRequestToApi(100, 20);

    expect(calcStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    expect(logSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});
