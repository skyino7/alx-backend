import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) =>
    console.log('Redis client not connected to the server', err)
);

client.on('connect', () =>
    console.log('Redis client connected to the server')
);

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
    const value = await getAsync(schoolName);
    console.log(value);
};

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  })();
