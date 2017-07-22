// Import dependencies
const mongoose = require('mongoose');
const express = require('express');
const router = express.Router();

// MongoDB URL from the docker-compose file
const dbHost = 'mongodb://mongodb/pclsearch';

// Connect to mongodb
mongoose.connect(dbHost);

// create mongoose schema
const articleSchema = new mongoose.Schema({
  id: mongoose.Schema.ObjectId,
  title: String,
  abs: String,
  url: String,
  url2: String,
  xml_headers: String,
  xml_full: String,
  xml_references: String,
  authors: [ {type : mongoose.Schema.ObjectId, ref: 'Author'} ]
});

const authorSchema = new mongoose.Schema({
  id: mongoose.Schema.ObjectId,
  name: String,
  email: String,
  institution: String,
  articles: [ {type : mongoose.Schema.ObjectId, ref: 'Article'}]
});


// create mongoose model
const Article = mongoose.model('Article', articleSchema);
const Author = mongoose.model('Author', authorSchema);

/* GET api listing. */
router.get('/', (req, res) => {
		res.send('PCLSearch API is online.');
});


/*------------------ articles api ------*/

/* GET all articles. */
router.get('/articles', (req, res) => {
	Article.find({}, (err, articles) => {
		if (err) res.status(500).send(error)
		res.status(200).json(articles);
	});
});

/* GET one article. */
router.get('/articles/:id', (req, res) => {
	Article.findById(req.params.id, (err, articles) => {
		if (err) res.status(500).send(error)
		res.status(200).json(articles);
	});
});

/* Create an article. */
router.post('/articles', (req, res) => {
	let article = new Article({
		title: req.body.title,
		abs: req.body.abs,
		url: req.body.url,
		url2: req.body.url2,
        xml_headers: req.body.xml_headers,
        xml_full: req.body.xml_full,
        xml_references: req.body.xml_references,
        authors: req.body.authors,
	});

	article.save(error => {
		if (error) res.status(500).send(error);

		res.status(201).json({
			message: 'Article created successfully'
		});
	});
});

/* Update an article */
router.put('/articles/:id', function (req, res) {
    Article.findByIdAndUpdate(req.params.id, req.body, {new: true}, function (err, article) {
        if (err) return res.status(500).send("There was a problem updating the article.");
        res.status(200).send(article);
    });
});


/*---------------------- authors api -------*/
/* GET all authors. */
router.get('/authors', (req, res) => {
	Author.find({}, (err, authors) => {
		if (err) res.status(500).send(error)
		res.status(200).json(authors);
	});
});


/* GET one author. */
router.get('/authors/:id', (req, res) => {
	Author.findById(req.params.id, (err, authors) => {
		if (err) res.status(500).send(error)
		res.status(200).json(authors);
	});
});


/* Create an author. */
router.post('/authors', (req, res) => {
	let author = new Author({
		name: req.body.name,
		email: req.body.email,
		institution: req.body.institution,
        articles: req.body.articles,
	});

	author.save(error => {
		if (error) res.status(500).send(error);
		res.status(201).json({
			message: 'Author created successfully'
		});
	});
});

/* Update an author */
router.put('/authors/:id', function (req, res) {
    Article.findByIdAndUpdate(req.params.id, req.body, {new: true}, function (err, author) {
        if (err) return res.status(500).send("There was a problem updating the author.");
        res.status(200).send(author);
    });
});

module.exports = router;
