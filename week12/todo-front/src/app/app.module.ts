import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MainComponent } from './components/main/main.component';
import { ProviderService } from './services/provider.service';
import { HttpClientModule } from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import { TodoComponent } from './components/todo/todo.component';


@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    TodoComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    ProviderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
