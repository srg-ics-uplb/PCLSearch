import { Component } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';

@Component({
  selector: 'article-edit',
  template:`
    <div>
      <button (click)="getArticle('59702b25e658510010a05846')">Edit Article</button>
      <h5>{{article.title}}</h5>      
    </div>
  `

})

export class ArticleEditComponent {

  // Link to our api, pointing to localhost
  API = 'http://localhost:3000';

  constructor(private http: Http){
  }

  article: {};

  ngOnInit() {
    this.getArticle('59702b25e658510010a05846');
  }

  getArticle(id) {
    this.http.get(`${this.API}/articles/${id}`)
      .map(res => res.json())
      .subscribe(article => {this.article = article}); 
  }

}

