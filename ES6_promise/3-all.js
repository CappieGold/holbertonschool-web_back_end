import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResult, userResult]) => {
      // Extract data from both promises
      const { body } = photoResult;
      const { firstName, lastName } = userResult;
      // Log the combined result
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => {
      // Log an error message if any of the promises reject
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
