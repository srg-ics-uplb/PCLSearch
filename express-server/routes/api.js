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
  title: String,
  url: String
});

// create mongoose model
const Article = mongoose.model('Article', articleSchema);

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
		url: req.body.url
	});

	article.save(error => {
		if (error) res.status(500).send(error);

		res.status(201).json({
			message: 'Article created successfully'
		});
	});
});

module.exports = router;
