function argumentsLength() {
  return arguments.length;
}

// Example 1
const result1 = argumentsLength(5);
console.log(result1); // Output: 1

// Example 2
const result2 = argumentsLength({}, null, "3");
console.log(result2); // Output: 3
