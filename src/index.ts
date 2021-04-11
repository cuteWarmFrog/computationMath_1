import {ConsoleReader} from "./Reader/ConsoleReader";
import {FileReader} from "./Reader/FileReader";

const input = require('readline-sync');


let greetings = `Чувствуй себя как дома, но не забывай, что ты в гостях.\n`;
console.log(greetings);

let consoleOrFile = input.question('Введи 1, если хочешь вводить с консоли или 2, если с файла.\n');


//const consoleOrFile = prompt('Введи 1, если хочешь вводить с консоли или 2, если с файла.\n');



const matrix = readMatrix(consoleOrFile);
printMatrix(matrix);



function readMatrix(consoleOrFile: string): Array<Array<number>> {
    switch (consoleOrFile) {
        case '1':
            return readFromConsole();

        case '2':
            return readFromFile();
    }
}

function readFromConsole(): Array<Array<number>> {
    const consoleReader = new ConsoleReader();
    return consoleReader.read();
}

function readFromFile(): Array<Array<number>> {
    const fileReader = new FileReader();
    return fileReader.read();
}

function printMatrix(matrix: Array<Array<number>>): void {
    console.log('\nВаша матрица:')
    console.log((matrix.reduce((out, str: any) => str.join(" ") + '\n', '')));
}


