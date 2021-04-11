import {Reader} from "./Reader";
const input = require('readline-sync');

export class ConsoleReader implements Reader {

    constructor() {
    }

    read(): Array<Array<number>> {
        let n = Number.parseFloat(input.question('Введите размерность матрицы:\n'));
        let matrix = [];
        for(let i = 0; i < n; i++) {
            console.log('Введите строку:')
            matrix.push(input.question('').split(' '));
        }
        return matrix;
    }

}