import { createQueue } from 'kue';

// Function to simulate sending a notification
function sendNotification(phoneNumber, message) {
  // Log the notification details to the console
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Create a Redis-backed job queue
const queue = createQueue();

// Process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  // Destructure job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message);

  // Signal that the job is complete
  done();
});
