import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;
  let consoleStub;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  beforeEach(() => {
    queue.testMode.clear();
    consoleStub = sinon.stub(console, 'log');
  });

  afterEach(() => {
    consoleStub.restore();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-an-array', queue))
      .to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const list = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(list, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    const [job1, job2] = queue.testMode.jobs;

    expect(job1.type).to.equal('push_notification_code_3');
    expect(job2.type).to.equal('push_notification_code_3');

    expect(job1.data).to.deep.equal(list[0]);
    expect(job2.data).to.deep.equal(list[1]);

    expect(consoleStub.called).to.equal(true);
    const createdLogs = consoleStub.getCalls()
      .map(c => c.args.join(' '))
      .filter(msg => msg.startsWith('Notification job created:'));
    expect(createdLogs.length).to.equal(2);
  });

  it('logs progress / completed / failed handlers are attached', () => {
    const list = [
      { phoneNumber: '000', message: 'x' },
    ];

    createPushNotificationsJobs(list, queue);

    const job = queue.testMode.jobs[0];

    job.emit('progress', 50);
    job.emit('complete');
    job.emit('failed', new Error('Boom'));

    const msgs = consoleStub.getCalls().map(c => c.args.join(' '));

    expect(msgs.some(m => m.includes('Notification job created:'))).to.equal(true);
    expect(msgs.some(m => m.includes('50% complete'))).to.equal(true);
    expect(msgs.some(m => m.includes('completed'))).to.equal(true);
    expect(msgs.some(m => m.includes('failed:'))).to.equal(true);
  });
});
