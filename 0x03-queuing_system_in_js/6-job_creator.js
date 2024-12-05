import { createQueue } from 'kue';

// Create a Redis-backed job queue
const queue = createQueue();

// Job data object representing a notification
const jobData = {
  phoneNumber: '+1234567890', // Example phone number
  message: 'Account verification needed', // Example message
};

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData);

// Event handler for job creation
job.save((err) => {
  if (err) {
    console.error('Error creating job:', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Event handlers for job state tracking
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
