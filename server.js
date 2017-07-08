const express = require('express');
const bodyParser = require('body-parser');
const PythonShell = require('python-shell');

const app = express();
const router = express.Router();

app.use(express.static(__dirname + '/View'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function(req, res){
  res.sendFile('/index.html');
})

app.listen(3000, function() {
  console.log('Listening on port 3000');
})