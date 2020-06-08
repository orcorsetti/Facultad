import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.scss']
})
export class CounterComponent implements OnInit {

  // @Input() description="Sumador por defecto"
  // @Input() count=0
  // @Input() incrementValue=1

  @Input()  config = {
    description: 'Sumador por defecto',
    incrementValue: 1
  }
  @Input() count = 0
  @Input() subtitle = ''
  @Output() countChanged = new EventEmitter<number>()
  @Output() numberClicked = new EventEmitter<number>()

  constructor() { }

  ngOnInit(): void {
  }

  onNumberClicked(){
    this.numberClicked.emit(this.count)
  }

  increment() {
    this.count += this.config.incrementValue
    this.countChanged.emit(this.count)
    
  }

}
