import { Component, Input } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';

@Component({
  selector: 'article-edit',
  template:`  
  <div *ngIf="article">
    <h3>{{article.title}} details!</h3>
    <div><label>Id: </label>{{article._id}}</div>
    <div>
      <label>Title: </label>
      <input [(ngModel)]="article.title" placeholder="title"/>
    </div>
    <div>
      <label>URL: </label>
      <input [(ngModel)]="article.url" placeholder="url"/>
    </div>
  </div>
`

})

export class ArticleEditComponent {

  // Link to our api, pointing to localhost
  API = 'http://localhost:3000';

  constructor(private http: Http){
  }

  //the article associated with this component
  @Input() article: {};

  ngOnInit() {
  }

  getArticle(id) {
    this.http.get(`${this.API}/articles/${id}`)
      .map(res => res.json())
      .subscribe(article => {this.article = article}); 
  }

}

