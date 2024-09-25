#!/usr/bin/node
import { createClient, print } from 'redis';
import { promisify } from 'util';
const client = createClient()
client.on('error', err => console.log('Redis Client Error', err))
    .connect();


client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, print);
}


async function displaySchoolValue(schoolName) {
    const GET = promisify(client.GET).bind(client);
    try {
        const value = await GET(schoolName);
        console.log(value);
    } catch (error) {
        console.log(error.toString());
    }
}

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
