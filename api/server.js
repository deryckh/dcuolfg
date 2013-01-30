var http = require('http');

var sample_data = {
    'name': 'FooBar Data',
    'date': 'Some date data here'
};

http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/json'});
  response.end(JSON.stringify(sample_data));
}).listen(8077, '127.0.0.1');

console.log('Server running at http://127.0.0.1:8077/');
