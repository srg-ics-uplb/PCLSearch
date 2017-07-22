import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { CompleterService, CompleterData } from 'ng2-completer';



// Import rxjs map operator
import 'rxjs/add/operator/map';

@Component({
  selector: 'author-selector',
  templateUrl: './author.component.html',
  styleUrls: ['./author.component.css']
})

export class AuthorComponent implements OnInit {
  title = 'app works!';

  // Link to our api, pointing to localhost
  protected API = 'http://localhost:3000';

  // Declare empty list of articles
  protected authors: any[] = [];

  //the selected article
  protected selectedAuthor: {};
  
  //data source
  protected dataService: CompleterData;

  //search string
  protected searchAuthor: string;
  
  protected searchData = [
    {'name':'author 1'},
    {'name':'author 2'},
    {'name':'author 3'}
  ];


  // Angular 2 Life Cycle event when component has been initialized
  ngOnInit() {
    this.getAllAuthors();
    this.dataService = this.completerService.local(this.searchData, 'name', 'name');
  }

  //method to set the selected article
  //event handler
  onSelect(author: {}): void {
    this.selectedAuthor = author;
  }

  // Add one article to the API
  addAuthor(name, email, institution) {
    this.http.post(`${this.API}/authors`, {name, email, institution})
      .map(res => res.json())
      .subscribe(() => {
        this.getAllAuthors();
      }, error => console.log(error))
  }

  // Get all users from the API
  getAllAuthors() {
    this.http.get(`${this.API}/authors`)
      .map(res => res.json())
      .subscribe(authors => {
        console.log(authors)
        this.authors = authors
      }, error => console.log(error))
  }

  constructor(private http: Http, private completerService: CompleterService) {
  }

}
