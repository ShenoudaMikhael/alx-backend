#!/usr/bin/node
import { createQueue } from 'kue';

const queue = createQueue();
const jobData = { phoneNumber: '+123456789', message: 'Hello World' };

const job = queue
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', (result) => { /* eslint-disable-line no-unused-vars */
  console.log('Notification job completed');
});

job.on('failed', (err) => { /* eslint-disable-line no-unused-vars */
  console.log('Notification job failed');
});
