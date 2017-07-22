import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

//completer module
import { Ng2CompleterModule } from "ng2-completer";

import { AppComponent } from './app.component';
import { MyComponent } from './my.component';
import { ArticleEditComponent } from './article-edit.component';

import { RouterModule, Routes } from '@angular/router';

@NgModule({
  declarations: [
    MyComponent,
    AppComponent,
    ArticleEditComponent
  ],
  imports: [
    Ng2CompleterModule,
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
