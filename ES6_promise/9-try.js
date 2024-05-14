function guardrail(mathFunction) {
  const queue = [];
  try {
    // Attempt to execute the mathFunction and push the result to the queue
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // If an error occurs, push the error message to the queue
    queue.push(`Error: ${error.message}`);
  } finally {
    // Regardless of the outcome, push this message to the queue
    queue.push('Guardrail was processed');
  }
  return queue;
}

export default guardrail;
