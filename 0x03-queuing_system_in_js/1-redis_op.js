#!/usr/bin/node
import { createClient, print } from 'redis';

const client = createClient()
client.on('error', err => console.log('Redis Client Error', err))
    .connect();


client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.GET(schoolName, (err, value) => {
        console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');