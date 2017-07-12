import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';

// Import rxjs map operator
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app works!';

  // Link to our api, pointing to localhost
  API = 'http://localhost:3000';

  // Declare empty list of people
  articles: any[] = [];

  constructor(private http: Http) {}

  // Angular 2 Life Cycle event when component has been initialized
  ngOnInit() {
    this.getAllArticles();
  }

  // Add one article to the API
  addArticle(title, url) {
    this.http.post(`${this.API}/articles`, {title, url})
      .map(res => res.json())
      .subscribe(() => {
        this.getAllArticles();
      }, error => console.log(error))
  }

  // Get all users from the API
  getAllArticles() {
    this.http.get(`${this.API}/articles`)
      .map(res => res.json())
      .subscribe(articles => {
        console.log(articles)
        this.articles = articles
      }, error => console.log(error))
  }
}
