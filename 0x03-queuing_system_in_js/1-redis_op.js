import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Handle connection success
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

// Function to set a new school
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

// Function to display the value of a school
const displaySchoolValue = async (schoolName) => {
  const value = await client.get(schoolName);
  console.log(value);
};

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
