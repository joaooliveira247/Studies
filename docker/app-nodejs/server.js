// file: app-nodejs/server.js

const http = require('node:http');
const hostname = '0.0.0.0';
const exposed_host = "127.0.0.1";
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Node docker preview container');
});

server.listen(port, hostname, () => {
    console.log(`Server em execução em http://${exposed_host}:${port}/`);
});
