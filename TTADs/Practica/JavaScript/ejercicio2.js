console.log('Ejercicio 2')

// Shape - superclass
function Shape() {
    this.x = 0;
    this.y = 0;
  }

  // superclass method
  Shape.prototype.move = function(x, y) {
    this.x += x;
    this.y += y;
    console.info('Shape moved.');
  };


  // Rectangle - subclass
  function Rectangle(base, altura) {
    Shape.call(this); // call super constructor.
    this.base = base; //agrego las variables
    this.altura = altura;
  }

  // subclass extends superclass
  Rectangle.prototype = Object.create(Shape.prototype);
  Rectangle.prototype.constructor = Rectangle;

  Rectangle.prototype.listar = function() {
    console.log('Altura: ', this.altura);
    console.log('Base: ', this.base);
}

    Rectangle.prototype.escalar = function(como, porcentaje) {
        if (como === '+'){
            this.altura+= this.altura * porcentaje / 100
            this.base+= this.base * porcentaje / 100
            console.log(`Rectangulo esclado un ${porcentaje} ${como}`)
        } else {
            this.altura-= this.altura*porcentaje/100
            this.base-= this.base*porcentaje/100
            console.log(`Rectangulo esclado un ${porcentaje} ${como}`)
        }
    };

  var rect = new Rectangle(30 , 50);

  console.log('Is rect an instance of Rectangle?',
    rect instanceof Rectangle); // true
  console.log('Is rect an instance of Shape?',
    rect instanceof Shape); // true
  rect.move(1, 1); // Outputs, 'Shape moved.'
  rect.listar();
  rect.escalar('-',10)
  rect.listar()
  
  console.log('Circulo: ')
  console.log('')

  function Circle (radio) {
      Shape.call(this)
      this.radio = radio
  }

  Circle.prototype = Object.create(Shape.prototype)
  Circle.prototype.constructor = Circle

  Circle.prototype.listar = function() {
    console.log('Radio: ',this.radio)
  }
  Circle.prototype.escalar = function(como, porcentaje) {
        if (como === '+'){
            this.radio += this.radio*porcentaje/100
            console.log(`Circulo escalado un ${porcentaje} ${como}`)
        } else {
            this.radio -= this.radio*porcentaje/100
            console.log(`Circulo escalado un ${porcentaje} ${como}`)
        }
  };

  var circle = new Circle(30)
  circle.listar()
  circle.escalar('+',50)
  circle.listar()

  console.log('Triangulo: ')
  console.log('')

  function Triangle(lado1, lado2, lado3){
        Shape.call(this)
        this.lados = [lado1, lado2, lado3]
  }

  Triangle.prototype = Object.create(Shape.prototype)
  Triangle.prototype.constructor = Triangle

  Triangle.prototype.listar= function(){
      this.lados.forEach((e, i)=> console.log(`Lado ${i+1}: ${e}`))
  }

  Triangle.prototype.escalar = function(como, porcentaje){
    if (como === '+'){
        this.lados = this.lados.map(e => e+= e*porcentaje/100)
        console.log(`Triangulo escalado un ${porcentaje} ${como}`)
    } else {
        this.lados = this.lados.map(e => e-= e*porcentaje/100)
        console.log(`Triangulo escalado un ${porcentaje} ${como}`)
    }
  }

  var tri = new Triangle(15,20,15)
  tri.listar()
  tri.escalar('-', 20)
  tri.listar()