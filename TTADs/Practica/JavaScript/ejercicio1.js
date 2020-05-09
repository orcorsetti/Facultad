const criterio = (elem) => {
    if (elem > 5) {
        return true
    } else { 
        return false
    }
}

const siVacio = () => {
    let  msg = 'Ningun elemento cumple con la condición'
    return msg
}

const buscar = (array, ftrue, ffalse) => {
    if(array.some(el => ftrue(el)===true)) {
        return array.filter(el => ftrue(el)===true) 
    } else {
        return ffalse()
    }
}

console.log('Ejercicio 1')
let arrayTrue = [1,2,3,4,5,6,7,8,9]
let arrayFalse = [1,2,3,4,5]
console.log(buscar(arrayTrue, criterio, siVacio))
console.log(buscar(arrayFalse, criterio, siVacio))