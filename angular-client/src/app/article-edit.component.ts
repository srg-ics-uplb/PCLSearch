import { Component } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';

@Component({
  selector: 'article-edit',
  template:`
    <div>
      <h5>{{article.title}}</h5>      
      <button (click)="getArticle('597092e2fa2d6800117afab7')">Edit</button>
    </div>
  `

})

export class ArticleEditComponent {

  // Link to our api, pointing to localhost
  API = 'http://localhost:3000';

  constructor(private http: Http){
  }

  //the article associated with this component
  article: {};

  ngOnInit() {
  }

  getArticle(id) {
    this.http.get(`${this.API}/articles/${id}`)
      .map(res => res.json())
      .subscribe(article => {this.article = article}); 
  }

}

