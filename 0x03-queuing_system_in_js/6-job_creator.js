const kue = require('kue');

const queue = kue.createQueue();
const obj = {
  phoneNumber: '+254712345678',
  message: 'I love coding',
}

const job = queue.create('push_notification_code', obj);

job.save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'))
.on('failed', () => console.log('Notification job failed'));
