// Import dependencies
const mongoose = require('mongoose');
const express = require('express');
const router = express.Router();

// MongoDB URL from the docker-compose file
const dbHost = 'mongodb://database/pclsearch';

// Connect to mongodb
mongoose.connect(dbHost);

// create mongoose schema
const articleSchema = new mongoose.Schema({
  id: mongoose.Schema.ObjectId,
  title: String,
  url: String,
  xml_headers: String,
  xml_full: String,
  xml_references: String,
  authors: [ {type : mongoose.Schema.ObjectId, ref: 'Author'} ]
});

const authorSchema = new mongoose.Schema({
  id: mongoose.Schema.ObjectId,
  name: String,
  email: String,
  articles: [ {type : mongoose.Schema.ObjectId, ref: 'Article'}]
});


// create mongoose model
const Article = mongoose.model('Article', articleSchema);
const Author = mongoose.model('Author', authorSchema);

/* GET api listing. */
router.get('/', (req, res) => {
		res.send('api works');
});

/* GET all articles. */
router.get('/articles', (req, res) => {
	Article.find({}, (err, users) => {
		if (err) res.status(500).send(error)

		res.status(200).json(users);
	});
});

/* GET one article. */
router.get('/articles/:id', (req, res) => {
	Article.findById(req.params.id, (err, users) => {
		if (err) res.status(500).send(error)

		res.status(200).json(users);
	});
});

/* Create an article. */
router.post('/articles', (req, res) => {
	let article = new Article({
		title: req.body.title,
		url: req.body.url,
        xml_headers: req.body.xml_headers,
        xml_full: req.body.xml_full,
        xml_references: req.body.xml_references,
	});

	article.save(error => {
		if (error) res.status(500).send(error);

		res.status(201).json({
			message: 'Article created successfully'
		});
	});
});

module.exports = router;
