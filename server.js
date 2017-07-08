const express = require('express');
const bodyParser = require('body-parser');
const PythonShell = require('python-shell');

const app = express();
const router = express.Router();

app.use(express.static(__dirname + '/View'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function(req, res) {
  res.sendFile('/index.html');
})

app.post('/input', function(req, res) {
  //Get input from req
  //Make call to python
  //Recieve output
  //Send back with res.send()


})

app.listen(3000, function() {
  console.log('Listening on port 3000');
})