import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { CompleterService, CompleterData } from 'ng2-completer';



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

  // Declare empty list of articles
  articles: any[] = [];

  //the selected article
  selectedArticle: {};
  
  //data source
  protected dataService: CompleterData;

  //search string
  protected searchStr: string;
  
  protected searchData = [
    {'title':'paper 1'},
    {'title':'paper 2'},
    {'title':'paper 3'}
  ];


  // Angular 2 Life Cycle event when component has been initialized
  ngOnInit() {
    this.getAllArticles();
    this.dataService = this.completerService.local(this.searchData, 'title', 'title');
  }

  //method to set the selected article
  //event handler
  onSelect(article: {}): void {
    this.selectedArticle = article;
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

  constructor(private http: Http, private completerService: CompleterService) {
  }

}
