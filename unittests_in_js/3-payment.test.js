const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  let calcSpy;
  let logSpy;

  beforeEach(() => {
    calcSpy = sinon.spy(Utils, 'calculateNumber');
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    calcSpy.restore();
    logSpy.restore();
  });

  it('utilise Utils.calculateNumber("SUM", 100, 20) et log le total', () => {
    sendPaymentRequestToApi(100, 20);

    expect(calcSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    expect(logSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
  });
});
