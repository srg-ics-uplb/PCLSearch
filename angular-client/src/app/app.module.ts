import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { ArticleEditComponent } from './article-edit.component';

import { RouterModule, Routes } from '@angular/router';

const appRoutes: Routes = [
  { path: 'articles/:id',      component: ArticleEditComponent },
  {
    path: 'articles',
    component: AppComponent,
  },
  { path: '',
    redirectTo: '/articles',
    pathMatch: 'full'
  },
];


@NgModule({
  declarations: [
    AppComponent,
    ArticleEditComponent
  ],
  imports: [
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    ),
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
