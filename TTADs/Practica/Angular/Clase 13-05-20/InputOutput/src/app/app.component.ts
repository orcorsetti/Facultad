import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'InputOutput';
  counterValue = 0;

  onCountChanged(event){
    this.counterValue= event;
  }

  onSecondNumberClicked(event){
    this.counterValue = 0;
  }

  onThirdNumberClicked(event){
    this.counterValue -= 1;
  }
}
