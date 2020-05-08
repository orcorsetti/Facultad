import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-arrayAdder',
  templateUrl: './array-adder.component.html',
  styleUrls: ['./array-adder.component.scss']
})
export class ArrayAdderComponent{

  arreglo = [0,1,2,3,4,5,6]

  agregarElemento () {
    this.arreglo.push(this.arreglo[this.arreglo.length - 1] + 1)

  }
}
