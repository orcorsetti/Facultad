import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  list = []
  listCompleted = []
  focus = false

  add(inputControl) {
    if (inputControl.value === ''){
      alert('Ingrese un elemento para agregar')
      return;
    }
    this.list.push(
      {
      description: inputControl.value,
      completed: false
    })
    inputControl.value = ''
  }

  remove(item) {
    if (item.completed){
      const index = this.listCompleted.findIndex(each => each.description===item.description)
      this.listCompleted.splice(index, 1)
    } else {
      const index = this.list.findIndex(each => item.description===each.description)
      this.list.splice(index,1)
    }
  }

  checked(item) {
    item.completed = true
    this.listCompleted.push(item)
    const index = this.list.findIndex(each => item.description===each.description)
    this.list.splice(index,1)
  }

  unchecked(item){
    item.completed = false
    this.list.push(item)
    const index = this.listCompleted.findIndex(each => item.description===each.description)
    this.listCompleted.splice(index,1)
  }
}
