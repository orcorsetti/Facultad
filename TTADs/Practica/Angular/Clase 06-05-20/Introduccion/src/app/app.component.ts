import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'testApp';
  inicial = 1000;
  value = 0;
  list = ['JavaScript', 'TypeScript', 'Java', 'C#']

  add(increment) {
    this.value += increment
  }

  addElement(){
    this.list.push('NuevoElemento')
  }

  getClassesforDiv(){
    if(this.value > 5){
      return['resaltado']
    }
    return['atenuado']
  }
}

